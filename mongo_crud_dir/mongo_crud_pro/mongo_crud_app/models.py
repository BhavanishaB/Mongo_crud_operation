from djongo import models


class Product( models.Model ):
    name = models.CharField(primary_key=True, max_length=255 )
    description = models.TextField()
    price = models.DecimalField( max_digits=10, decimal_places=2 )

    def __str__(self):
        return self.name
