from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    items = models.IntegerField(default=0)
    parent_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural= "Categories"

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.title}"