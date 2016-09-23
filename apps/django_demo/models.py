from __future__ import unicode_literals

from django.db import models
from ..new_login.models import User
# Create your models here.
class PokeManager(models.Manager):
    def addPoke(self, user_id):
        new_poke = self.create(user=user_id)
        return new_poke

class Pokes(models.Model):
    user = models.ForeignKey(User, related_name='userPokes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pokeMgr=PokeManager()
