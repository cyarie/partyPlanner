from django.db import models


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

    def __unicode__(self):
        return self.name
