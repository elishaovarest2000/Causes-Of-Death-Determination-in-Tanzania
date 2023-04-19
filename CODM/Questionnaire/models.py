from django.db import models
from django.contrib.auth.models import User

# #model logofiles
# class SiteConfiguration(models.Model):
#     logo = models.ImageField(upload_to='images/')
#     # Add other fields for your site configuration model


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
   
class SurveyForm(models.Model):
    form_name= models.CharField(max_length=200)
    verbal_Autopsy= models.TextField(max_length=500)

    def __str__(self):
        return self.form_name


