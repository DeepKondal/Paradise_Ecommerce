from django.test import TestCase
from django.urls import reverse, resolve
from .models import Category, Product
from .views import store,all,categories,product_info,list_category 


#Testing the Category model class
class CategoryTestModels(TestCase):

    def setUp(self):
        # Create a sample Category object for testing
        self.category = Category.objects.create(
            name = 'heavy duty',
            slug = 'heavy-duty'
        )


    #TEST 1    
    def test_category_creation(self):
        #Test if the category was successfully created
        self.assertEqual(self.category.name, 'heavy duty')
        self.assertEqual(self.category.slug, 'heavy-duty')


    #TEST 2
    def test_get_absolute_url(self):
        #Test if the get_absolute_url method returns the expected URL
        expected_url = reverse('list-category', args=[self.category.slug])
        self.assertEqual(self.category.get_absolute_url(), expected_url)



#Testing the Product model class
class ProductModelTest(TestCase):
    def setUp(self):
        # Create a sample Category object for testing
        self.category = Category.objects.create(
            name='heavy duty',
            slug='heavy-duty'
        )

        
        # Create a sample Product object for testing
        self.product = Product.objects.create(
            category=self.category,
            title='Good Product',
            brand='Good Brand',
            description='Sample Description',
            slug='good-product',
            price=00.00,
            image='static/media/images/shirt.jpg',
        )


    #TEST 3
    def test_product_creation(self):
        # Test if the Product object was created successfully
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.title, 'Good Product')
        self.assertEqual(self.product.brand, 'Good Brand')
        self.assertEqual(self.product.description, 'Sample Description')
        self.assertEqual(self.product.slug, 'good-product')
        self.assertEqual(self.product.price, 00.00)
        

    #TEST 4    
    def test_get_absolute_url(self):
        # Test if the get_absolute_url method returns the expected URL
        expected_url = reverse("product-info", args=[self.product.slug])
        self.assertEqual(self.product.get_absolute_url(), expected_url)
