from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.

class LocationTestClass(TestCase):
    
    def setUp(self):
        self.king = Location(loc_name = 'kakamega', id=1)
        
        
  #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.king,Location)) 

    def test_save_method(self):
        self.king.save_loc()
        editors = Location.objects.all()
        self.assertTrue(len(editors)>0)
        
    def test_delete_method(self):
        self.king.delete_loc()
        locations = Location.objects.all()
        self.assertTrue(len(locations) is 0)
        
    def test_display_all(self):
        kong = Location(loc_name='texas')
        kong.save_loc()
        self.james.save_loc()
        locations = Location.objects.all()
        print(len(locations))
        self.assertTrue(len(locations),2)

         
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
class CategoryTestClass(TestCase):
    
    def setUp(self):
        self.category = Category(name = 'kong', id=1)
        
        
  #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category)) 

    def test_save_method(self):
        self.category.save_category()
        catego = Category.objects.all()
        self.assertTrue(len(catego)>0)
        
    def test_delete_method(self):
        self.category.delete_category
        cat = Category.objects.all()
        self.assertTrue(len(cat) is 0)
        
    def test_display_all(self):
        dan = Category(name='animal')
        dan.save_category()
        one = Category.objects.all()
        print(len(one))
        self.assertTrue(len(one),2)

         
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
        
class ImageTestClass(TestCase):
    
    def setUp(self):
        self.kakamega = Location(loc_name='kakamega')
        self.nature = Category(name='plant')
        self.image = Image(image='images/lagoon.jpeg',image_name='kong', image_descprition='he is cool',location=self.kakamega,category=self.plant, id=1)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    def test_get_image_today(self):
        today_image = Article.todays_images()
        self.assertTrue(len(today_images)>0)
    

        
        


