from django.db import models

RATING_CHOICES = [
    (0, ""),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
    (9, "9"),
    (10, "10"),
]

# Create your models here.
class Wishlist(models.Model):
    name = models.CharField(max_length=100, null=True)

class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    purchased = models.BooleanField(default=False)
    hyperlink = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
