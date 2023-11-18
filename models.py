from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Define other fields
new_record = MyModel(field1='Value 1', field2=42)
new_record.save()
all_records = MyModel.objects.all()
record = MyModel.objects.get(pk=1)
filtered_records = MyModel.objects.filter(field1='Value 1')
record = MyModel.objects.get(pk=1)
record.field1 = 'New Value'
record.save()
record = MyModel.objects.get(pk=1)
record.delete()
MyModel.objects.filter(field1='Value 1').delete()
