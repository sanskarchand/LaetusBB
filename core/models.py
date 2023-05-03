from django.db import models

class Forum(models.Model):
    # access threads using thread_set
    
    category = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

    # TODO: add various moderator-specific permissions


    def __str__(self):
        return f"<Forum {self.title}, {self.category}>"

