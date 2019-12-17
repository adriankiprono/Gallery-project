from django.db import models
import datetime as dt
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    
    def __str__(self):
        return self.name
class Location(models.Model):
    loc_name = models.CharField(max_length=30)
    
    def save_loc(self):
        self.save()
        
    def delete_loc(self):
        self.delete()
    
    def __str__(self):
        return self.loc_name
class Image(models.Model):

    image = models.ImageField(upload_to='images/',default='image')
    image_name = models.CharField(max_length=30)
    image_descprition = models.CharField(max_length=150)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_image(cls):
        today = dt.date.today()
        images = cls.objects.all()
        return images
    @classmethod
    def days_image(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images
    @classmethod
    def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images
    @classmethod
    def filter_by_location(cls,location):
        images_locs = cls.objects.filter(location__loc_name=location)
        return images_locs
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete() 
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']