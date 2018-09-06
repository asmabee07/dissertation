from django.db import models


# Create your models here.


class CompleteProfile(models.Model):
    user = models.OneToOneField('auth.User', null=True, blank=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.FloatField(help_text='Required. Enter weight in Kilograms(Kg).')
    height = models.FloatField(help_text='Required. Enter height in meter(m).')
    activity_factor = models.CharField(max_length=30)
    bmi = models.IntegerField(default = 0,null = True)


class BmiMeasurement(models.Model):
    weight_in_g = models.FloatField()
    height_in_meters = models.FloatField()
    measured_at = models.DateField()

    def bmi(self):
        return self.weight_in_kg / self.height_in_meters ** 2


class MealSelection(models.Model):
    meal_name = models.CharField(max_length=25)

    def __str__(self):
        return self.meal_name


class FoodItem(models.Model):
    meal_selection = models.ForeignKey(MealSelection, on_delete=models.SET_NULL, null=True)
    food_name = models.CharField(max_length=100)
    calories = models.CharField(max_length=20)
    total_Carbs = models.CharField(max_length=20)
    protein = models.CharField(max_length=20)
    vitamin_A = models.CharField(max_length=20)
    vitamin_C = models.CharField(max_length=20)
    total_Fat = models.CharField(max_length=20)
    calcium = models.CharField(max_length=20)
    sodium = models.CharField(max_length=20)
    potassium = models.CharField(max_length=20)
    iron = models.CharField(max_length=20)
    sugars = models.CharField(max_length=20)
    cholesterol = models.CharField(max_length=20)

    def __str__(self):
        return self.food_name


class FoodQuantity(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return self.quantity




