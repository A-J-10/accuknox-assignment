import time,threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SampleModel,AuditLog
@receiver(post_save,sender=SampleModel)
def demo(sender,instance,**kwargs):
    print('Signal thread',threading.get_ident())
    time.sleep(1)
    AuditLog.objects.create(message=instance.name)
