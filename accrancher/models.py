from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime
from django.db.models.signals import post_save
from django.utils.text import slugify
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)
    bio = models.TextField(blank=True)
    join_date=models.DateTimeField(blank=True,default=datetime.datetime.now)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.user:
    #         self.user = eval(self.slug)




    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
            return '%s' %(self.user)


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)


class SaveChkbox(models.Model):
    stacknames = models.CharField(max_length=50, blank=False)
    usernames = models.TextField()
    class Meta:
        db_table = "name_stack"
    def __str__(self):
        return self.stacknames
