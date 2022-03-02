from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Forum(models.Model):
    # access threads using thread_set
    
    category = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

class Thread(models.Model):
    # many-to-one
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    sticky = models.BooleanField(default=False)

class Post(models.Model):
    #NOTE: CASCADE too severe? SET_NULL?
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=256)
    content = models.TextField('raw post content')
    edit_date = models.DateTimeField('date edited')
    pub_date = models.DateTimeField('date published')
    
    # related_name is for reverse rel, user.thankedby_set() instead of 
    #   user.post_set(), which clashes with the _author_ field
    thanked_by = models.ManyToManyField(User, related_name='thankedby')
    flagged = models.BooleanField(default=False)



# using this since User is provided by django
class Profile(models.Model):

    class Level(models.TextChoices):
        ADMIN = 'GOD', _('God')
        MOD = 'MOD', _('Janny')
        USER = 'PLEB', _('Plebeian')
        BANNED = 'B&', _('Forsaken')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField('date joined')
    reputation = models.IntegerField('reputation points')
    level =  models.CharField(max_length=5, choices=Level.choices, 
                        default=Level.USER)
    
    avatar = models.ImageField('avatar image')
    signature = models.CharField(max_length=512)


class Attachment(models.Model):
    """
    This represents an uploaded file
    """
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    file = models.FileField('actual file')
    
     
