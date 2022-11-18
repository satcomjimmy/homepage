from cProfile import label
import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Grocery(models.Model):
    def __str__(self):
        return self.grocery_name
        """ in every model you should define the standard Python class method __str__() 
        to return a human-readable string for each object. This string is used to represent 
        individual records in the administration site (and anywhere else you need to refer to a model instance). 
        Often this will return a title or name field from the model. """
    grocery_name = models.CharField(max_length=200)
    grocery_desc = models.CharField(max_length=200, blank=True, help_text="Description")
    when_needed = models.DateField('date needed')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

class Chef(models.Model):
    def __str__(self):
        return self.chef_name
    mom = 'Mom'
    dad = 'Dad'
    kat = 'Kat'
    isaac = 'Isaac'
    chef_name_choices = [('mom','Mom'), ('dad', 'Dad'), ('kat', 'Kat'), ('isaac', 'Isaac'),]
    chef_name = models.CharField(max_length=20, choices=chef_name_choices)

class Meal(models.Model):
    def __str__(self):
        return self.food_name
    food_name = models.CharField(max_length=200)
    when_cooking = models.DateField('date of the meal')
    # whos_cooking = models.ForeignKey(Chef, on_delete=models.CASCADE)

class WhenNeeded(models.Model):
    def __str__(self):
        return self.when_needed_text
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    when_needed_text = models.CharField(max_length=200)
    what_meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
