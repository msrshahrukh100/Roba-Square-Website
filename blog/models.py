from django.conf import settings
from django.core.urlresolvers import reverse

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch.dispatcher import receiver
from notifications.signals import notify
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from sorl.thumbnail import ImageField
from django.utils.text import slugify


def upload_location(instance, filename):
    return "blogimages/%s/%s" %(instance, filename)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="userblogposts")
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title',unique=True)
    image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field", help_text="A landscape image ie width greater than height for the parallax")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    publish_it = models.BooleanField(default=False)
    draft = models.BooleanField(default=False, verbose_name="Select if it is a draft. Draft posts are not published.")
    show_about_the_author = models.BooleanField(default=True, verbose_name="Select if you wish to display the 'About the Author' section along with your post")
    about_the_author = models.CharField(max_length=200, null=True,blank=True, verbose_name="Write about yourself, which you want to be displayed in the 'About the Author' section")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    url = models.URLField(default='/')


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    def get_views_count(self) :
        return PostViews.objects.filter(post=self).count()

    # def get_markdown_content(self) :
    #     content = self.content
    #     return mark_safe(markdown(content))

    class Meta:
        ordering = ["-timestamp", "-updated"]



@receiver(post_save, sender=Post)
def notify_user_about_post(sender, instance, **kwargs):
    if instance.publish_it :
        verb = "Your blog post on Roba Square recently got pblished !"
        url = instance.url
        imageurl = instance.image.url
        notify.send(instance.user, recipient=instance.user, verb=verb, url=url, imageurl=imageurl)

    # instance.save()





class PostViews(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userblogviewed", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postviews")
    ip = models.CharField(max_length=100)
    session = models.CharField(max_length=100,null=True,blank=True)
    viewed_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self) :
        return self.post.slug

    class Meta:
        ordering = ['-id']




def upload_location_blog_promotion(instance,filename) :
    return "slider_blog_promotion_images/%s"%(filename)

class BlogSlider(models.Model) :
    view_opt = (('center','center'),('left','left'),('right','right'))

    image = ImageField(upload_to = upload_location_blog_promotion, null=False, blank=False ,height_field="height_field", width_field="width_field",help_text="Images to be displayed on the slider")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    header = models.CharField(max_length=100,help_text="The heading to be displayed on the slider.")
    content = models.CharField(max_length=150,help_text="The text content which is to be displayed on the slider.")
    link_text = models.CharField(max_length=100,help_text="The text which is used to link the url, eg. Buy Now, Shop here .")
    link = models.URLField(max_length=200, help_text="The link of the product or category which is targeted to.")
    alignment = models.CharField(max_length=10 ,choices=view_opt, default="left", help_text="How you wish the text to appear on the slider?")

    def __unicode__(self) :
        return self.header

    class Meta :
        verbose_name = "Images on the blog promotion slider"
        verbose_name_plural = "Images on the blog promotion slider"









