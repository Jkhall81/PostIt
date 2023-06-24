from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# create post model
class Post(models.Model):
    user = models.ForeignKey(
        User, related_name='posts',
        on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'{self.user} '
            f'({self.created_at:%Y-%m-%d %H:%M}): '
            f'{self.body}...'
        )


# Create user profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
        blank=True
    )

    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.user.username


# Create profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # have user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)
