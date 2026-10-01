from django.db import models

# Create your models here.
class LostAndFoundItem(models.Model):

    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
        ('Returned', 'Returned'),
    ]

    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    date_reported = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Lost'
    )
    contact_information = models.CharField(max_length=150)

    def __str__(self):
        return self.item_name