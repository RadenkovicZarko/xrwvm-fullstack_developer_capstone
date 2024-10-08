from django.db import models

# Define CarMake model
class CarMake(models.Model):  # Add the missing colon here
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Define CarModel model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    # Car type choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    year = models.IntegerField(default=2023)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
