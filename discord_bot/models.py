# Here you can define django models and use the models in other folders for example
from django.db import models
# Here is a usage example of django models usage in discord.py bot
# This model stores the id of the role in a guild for the role used 
# to mute a member in a server 
class MuteRole(models.Model):
    guild_id = models.CharField(max_length=256,primary_key=True)
    role_id = models.CharField(max_length=256,null=True,blank=True)