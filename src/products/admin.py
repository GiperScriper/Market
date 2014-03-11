from django.contrib import admin
from .models import Product, Category, ProductImage, Tag, CategoryImage


class TagInline(admin.TabularInline):
	prepopulated_fields = { 'slug' : ('tag',) }
	extra = 1
	model = Tag


class ProductImageInline(admin.TabularInline):
	model = ProductImage

class CategoryImageInline(admin.TabularInline):
	model = CategoryImage


class ProductAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'description', 'current_price', 'order', 'categories')

	inlines = [TagInline, ProductImageInline]
	search_fields = ['title', 'description', 'price']
	list_filter = ['price', 'timestamp']
	prepopulated_fields = { 'slug' : ('title',) }
	readonly_fields = ['timestamp', 'updated']
	
	class Meta:
		model = Product

	def current_price(self, obj):
		if obj.sale_price > 0:
			return obj.sale_price
		return obj.price

	def categories(self, obj):
		categories = []
		for item in obj.category_set.all():
			categories.append(item.title)
		return ", ".join(categories)

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):	
	prepopulated_fields = { 'slug' : ('title',) }
	inlines = [CategoryImageInline]
	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)
