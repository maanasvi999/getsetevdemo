from django.db import models
from datetime import datetime

class EVCategory(models.Model):
    ev_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length = 200)
    category_slug = models.CharField(max_length = 100, default = 1)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.ev_category


class EVInformation(models.Model):
    ev_title = models.CharField(max_length = 100)
    ev_image = models.ImageField(upload_to ="gallery")
    ev_emi = models.CharField(max_length = 100)
    ev_country = models.CharField(max_length = 100)
    ev_category = models.ForeignKey(EVCategory, default = 1, verbose_name="Category", on_delete = models.SET_DEFAULT)
    ev_summary = models.CharField(max_length = 200)
    ev_slug = models.CharField(max_length = 200, default = 1)
    
    class Meta:
        verbose_name_plural = "Information"
    
    def __str__(self):
        return self.ev_title

class ModelsInfo(models.Model):
    ev_title = models.ForeignKey(EVInformation, default =1, verbose_name = "Information", on_delete = models.SET_DEFAULT)
    ev_model = models.CharField(max_length = 100, default = "No models")
    ev_model_city = models.IntegerField()
    ev_model_hwy = models.IntegerField()
    ev_model_mix = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Customization"
    
    def __str__(self):
        return self.ev_model

class EVHighlights(models.Model):
    ev_title = models.ForeignKey(EVInformation, default =1, verbose_name = "Information", on_delete = models.SET_DEFAULT)
    ev_high1 = models.CharField(max_length = 100)
    ev_high2 = models.CharField(max_length = 100)
    ev_high3 = models.CharField(max_length = 100)
    ev_high4 = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name_plural = "Highlights"
    
    def __str__(self):
        return str(self.ev_title) + " Highlights"

class EVColorCustom(models.Model):
    ev_title = models.ForeignKey(EVInformation, default =1, verbose_name = "Information", on_delete = models.SET_DEFAULT)
    ev_color = models.ImageField(upload_to ="gallery")

    def __str__(self):
        return str(self.ev_title) + " Custom Color"

class Subscribers(models.Model):
    email = models.EmailField()
    def __str__(self):
        return str(self.email) + " "+str(datetime.now())