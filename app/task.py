from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"


from .models import StoreUrl

aa = StoreUrl.objects.all()
import pdb;

pdb.set_trace()
for created_date in aa:
    created_date.cre
print(aa)
