from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name = "followed_by", symmetrical = False, blank = True
    )

    def __str__(self):
        return self.user.username
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
       Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()   

class Dweet(models.Model):
    user = models.ForeignKey( User, related_name="dweets", on_delete=models.DO_NOTHING )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(f"{self.user}" f"({self.created_at:%Y-%m-%d %H: %M}): " f"{self.body[ :30]}...")         