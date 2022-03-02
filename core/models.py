from django.db import models
from django.contrib.auth.models import User

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
    
    thanked_by = models.ManyToManyField(User)
    flagged = models.BooleanField(default=False)



# using this since User is provided by django
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField('date joined')
    reputation = models.IntegerField('reputation points')


class Attachment(models.Model):
    """
    This represents an uploaded file
    """
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    file = models.FileField('actual file')
    
     
