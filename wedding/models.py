from django.db import models
from django.contrib.auth.models import User


# Let's make some models! Only really need to write in one model here, for the people we are going to invite.
class People(models.Model):
    name = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=45)
    zip_code = models.SmallIntegerField(max_length=5)
    email = models.CharField(max_length=255)
    comment = models.TextField()
    created_by = models.ForeignKey(User)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
