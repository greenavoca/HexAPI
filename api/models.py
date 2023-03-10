from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.db.models.signals import post_save
from django.dispatch import receiver


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg'))])
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(200, 200)])
    owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE, editable=False)


class UserProfile(models.Model):

    MEMBERSHIP = (
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('ENTERPRISE', 'Enterprise')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.CharField(max_length=10, choices=MEMBERSHIP, default='BASIC')
    basic_thumbnail_height = models.PositiveIntegerField(default=200)
    premium_thumbnail_height = models.PositiveIntegerField(default=400)

    def __str__(self):
        return f'{self.user.username} ({self.membership})'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    UserProfile.objects.create(user=instance)





