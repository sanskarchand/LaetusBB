from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# using this since User is provided by django
class Profile(models.Model):

    class Level(models.TextChoices):
        ADMIN = 'GOD', _('God')
        MOD = 'MOD', _('Janny')
        POWERUSER = 'LEET', _('Patrician')
        USER = 'PLEB', _('Plebeian')
        BANNED = 'B&', _('Forsaken')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #TODO: remove; auth.User already has a joined date
    join_date = models.DateTimeField('date joined')
    reputation = models.IntegerField('reputation points')
    level =  models.CharField(max_length=5, choices=Level.choices, 
                        default=Level.USER)
    
    avatar = models.ImageField(default='laetusbb_def_avatar.png')
    signature = models.CharField(max_length=512, null=True)


