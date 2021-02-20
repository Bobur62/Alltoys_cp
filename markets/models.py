from django.db import models


class Market(models.Model):
    market_name = models.CharField(max_length=100, null=True, blank=True)
    market_special = models.CharField(max_length=150, null=True, blank=True)
    images = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.market_name


class MarketList(models.Model):
    CATEGORY = (
        ('Currently unavailable', 'Currently unavailable'),
        ('Currently available', 'Currently available')
    )
    market = models.ForeignKey(Market, related_name='market', on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to="product_images/", null=True, blank=True)
    product = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY, blank=True)

    def __str__(self):
        return self.product