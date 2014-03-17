from django.shortcuts import render, render_to_response, RequestContext, Http404
from .models import Product, Category, ProductImage


def list_products(request):	
	products = Product.objects.filter(active=True)

	return render_to_response('products/all.html', locals(), context_instance=RequestContext(request))

def product(request, productId):
	
	product = Product.objects.get(id=productId)
	images = product.productimage_set.all() # images2 = ProductImage.objects.filter(product=product)
	categories = product.category_set.all()
	
	return render_to_response('products/single.html', locals(), context_instance=RequestContext(request))

def edit_product(request, productId):	
	product = Product.objects.get(id=productId)
	
	if request.user == product.user:
		return render_to_response('products/edit.html', locals(), context_instance=RequestContext(request))
	else:
		raise Http404

