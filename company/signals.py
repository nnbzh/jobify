from django.db.models.signals import post_save
from django.dispatch import receiver

from company.models import Invite, Notification, Respond


@receiver(post_save, sender=Invite)
def invite_created(sender, instance, created, **kwargs):
    if created:
        text = f"You have been invited to the company"
        Notification.objects.create(user=instance.user, text=text)


@receiver(post_save, sender=Respond)
def respond_created(sender, instance, created, **kwargs):
    if created:
        text = f"You have a respond for vacancy"
        Notification.objects.create(user=instance.user, text=text)
