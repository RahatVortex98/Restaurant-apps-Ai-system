from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Meal(models.Model):
    name = models.CharField("Name of Meal", max_length=100)
    description = models.TextField("Description of Meal", blank=True,null=True)
    price = models.DecimalField("Price ($)", max_digits=10,decimal_places=2)

    #weather the meal is available in Online

    available = models.BooleanField("Online Availability",default=False)

    stock = models.IntegerField("Stock Count",default=0)

    image = models.ImageField("Meal Image",upload_to="meal_images",default="meal_images/default_meal.jpg")

    def __str__(self):
        return self.name
    
DELIVERY_STATUS_CHOICES =(
    ('pending','PENDING'),
    ('failed','FAILED'),
    ('completed','COMPLETED')

)

class OrderTransaction(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)

    customer = models.ForeignKey(User,on_delete=models.CASCADE)

    amount = models.DecimalField('Amount Paid($)',max_digits=7,decimal_places=2)
    
    status = models.CharField('Delivery Status',max_length=9,choices=DELIVERY_STATUS_CHOICES,default='pending')

    created_at=models.DateTimeField('Date Created',default=now)
    

    