from django.db.models.signals import post_save
from django.dispatch import receiver

from company.models import Invite, Notification


@receiver(post_save, sender=Invite)
def notify(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create({
            'text': f'{instance.company.get().name} приглашает вас на работу',
            'user_id': instance.user.get().id
        })


@receiver(post_save, sender=Invite)
def save_notification(sender, instance, **kwargs):
    instance.notifications.save()
