from django.db import models


# Create your models here.
OPTIONS = (
    ('yes','Yes'),
    ('no','No')
)

PROVIDERS = (
    ('adobe','Adobe'),
    ('liveramp', 'LiveRamp'),
    ('neustar', 'Neustar'),
    ('oracle blue kai', 'Oracle Blue Kai'),
    ('salesforce (krux)', 'Salesforce (Krux)'),
    ('none of the above', 'None of the Above')
)

class MyModel(models.Model):
    y_n = models.CharField(
        max_length=6, 
        choices=OPTIONS
    )
    providers = models.CharField(
        max_length = 50, 
        choices=PROVIDERS
    )



