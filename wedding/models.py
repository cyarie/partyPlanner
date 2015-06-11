from django.db import models
from django.contrib.auth.models import User


# Let's make some models! Only really need to write in one model here, for the people we are going to invite.
class People(models.Model):
    name = models.CharField(max_length=255, default=None)
    address1 = models.CharField(max_length=255, default=None)
    address2 = models.CharField(max_length=255, default=None)
    city = models.CharField(max_length=255, default=None)
    state = models.CharField(max_length=45, default=None)
    zip_code = models.SmallIntegerField(max_length=5, default=None)
    email = models.CharField(max_length=255, default=None)
    comment = models.TextField(default=None)
    created_by = models.ForeignKey(User)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
