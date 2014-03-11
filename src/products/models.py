from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	
	user = models.ForeignKey(User, null=True, blank=True)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=700)
	price = models.DecimalField(max_digits=15, decimal_places=2)
	sale_price = models.DecimalField(max_digits=15, decimal_places=2)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	order = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-order']


class ProductImage(models.Model):
	
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to="products/image/")
	title = models.CharField(max_length=200, null=True, blank=True)
	featured_image = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title


class Tag(models.Model):

	product = models.ForeignKey(Product)
	tag = models.CharField(max_length=50)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.tag


class Category(models.Model):
	
	products = models.ManyToManyField(Product)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=700)	
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Category'
		verbose_name_plural = u'Categories'


class CategoryImage(models.Model):

	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to="category/image/")
	title = models.CharField(max_length=200, null=True, blank=True)
	featured_image = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Category Image'
		verbose_name_plural = u'Category Images'





