
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings as django_settings



class Profile(models.Model):
    user = models.OneToOneField(User)
    public_email = models.EmailField(null=True, blank=True)
    location = models.CharField(max_length=50)


    class Meta:
        db_table = 'auth_profile'


    def get_picture(self):
        no_picture = django_settings.STATIC_URL + 'img/user.png'
        try:
            filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + self.user.username + '.jpg'
            picture_url = django_settings.MEDIA_URL + 'profile_pictures/' + self.user.username + '.jpg'
            if os.path.isfile(filename):
                return picture_url
            else:
                return no_picture
        except Exception:
            return no_picture

    def get_screen_name(self):
        try:
            if self.user.get_full_name():
                return self.user.get_full_name()
            else:
                return self.user.username
        except:
            return self.user.username



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
