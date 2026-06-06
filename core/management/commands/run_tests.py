from django.core.management.base import BaseCommand
from django.db import transaction
import threading,time
from core.models import SampleModel,AuditLog,Rectangle
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        print('Caller thread',threading.get_ident())
        st=time.time()
        try:
            with transaction.atomic():
                SampleModel.objects.create(name='test')
                raise Exception()
        except: pass
        print('Elapsed',time.time()-st)
        print('Sample',SampleModel.objects.count())
        print('Audit',AuditLog.objects.count())
        print(list(Rectangle(10,5)))
