from django.db import models
from core.models import Forum
from django.contrib.auth.models import User

class Thread(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
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

class Attachment(models.Model):
    """
    This represents an uploaded file
    """
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    file = models.FileField('actual file')
    
 
