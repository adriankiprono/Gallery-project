from django.test import TestCase
from .models import *
# Create your tests here.

class LocationTestClass(TestCase):
    
    def setUp(self):
        self.james = Location(loc_name = 'nakuru', id=1)
        
        
  #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Location)) 

    def test_save_method(self):
        self.james.save_loc()
        editors = Location.objects.all()
        self.assertTrue(len(editors)>0)
        
    def test_delete_method(self):
        self.james.delete_loc()
        locations = Location.objects.all()
        self.assertTrue(len(locations) is 0)
        
    def test_display_all(self):
        dan = Location(loc_name='uganda')
        dan.save_loc()
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
        self.category = Category(name = 'dan', id=1)
        
        
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
        dan = Category(name='general')
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
        self.nakuru = Location(loc_name='nakuru')
        self.nature = Category(name='general')
        self.image = Image(image='images/lagoon.jpeg',image_name='dan', image_descprition='he is cool',location=self.nakuru,category=self.nature, id=1)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image)) 

        
        


