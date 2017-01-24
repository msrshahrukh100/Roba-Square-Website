from django.conf import settings
from django.core.urlresolvers import reverse

from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.safestring import mark_safe
from markdown_deux import markdown
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from django.utils.text import slugify


def upload_location(instance, filename):
    return "blogimages/%s/%s" %(instance, filename)

class Post(models.Model):
    user = models.ForeignKey(User, related_name="userblogposts")
    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title',unique=True)
    image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    publish_it = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def get_markdown_content(self) :
        content = self.content
        return mark_safe(markdown(content))

    class Meta:
        ordering = ["-timestamp", "-updated"]









