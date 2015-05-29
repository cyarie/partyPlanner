from django.db import models


# A model for representing RSVPs!
class Rsvp(models.Model):
    name = models.CharField(max_length=255)
    going = models.BooleanField(default=False)
    number_guests = models.IntegerField()
    create_dt = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
