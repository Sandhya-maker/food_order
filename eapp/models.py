from django.db import models
    
class categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class food_items(models.Model):
    img = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=50)
    category= models.ForeignKey(categories,on_delete=models.CASCADE,    null=True,
    blank=True)

    def __str__(self):
        return self.name
    

class food_variants(models.Model):
    img = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    food = models.ForeignKey(
        food_items,
        on_delete=models.CASCADE,
        related_name="variants"
    )

    def __str__(self):
        return self.name
