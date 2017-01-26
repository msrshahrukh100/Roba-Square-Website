from django.conf import settings
from django.core.urlresolvers import reverse

from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

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
    show_about_the_author = models.BooleanField(default=True, verbose_name="Select if u wish to display the 'About the Author' section along with your post")
    about_the_author = models.CharField(max_length=200, null=True,blank=True, verbose_name="Write about yourself, which you want to be displayed in the 'About the Author' section")
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


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


class PostViews(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userblogviewed")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postviews")
    ip = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    viewed_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self) :
        return self.post.slug

    class Meta:
        ordering = ['-id']








