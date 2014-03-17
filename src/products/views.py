from django.shortcuts import render, render_to_response, RequestContext, Http404, HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.forms.models import modelformset_factory

from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm

def list_products(request):	
	products = Product.objects.filter(active=True)

	return render_to_response('products/all.html', locals(), context_instance=RequestContext(request))

def product(request, productId):
	
	product = Product.objects.get(id=productId)
	images = product.productimage_set.all() # images2 = ProductImage.objects.filter(product=product)
	categories = product.category_set.all()
	
	return render_to_response('products/single.html', locals(), context_instance=RequestContext(request))


def add_product(request):	
	form = ProductForm(request.POST or None)
	if form.is_valid():
		product = form.save(commit=False)
		product.user = request.user
		product.slug = slugify(form.cleaned_data['title'])
		product.save()

		return HttpResponseRedirect('/products/{0}'.format(product.id))

	return render_to_response('products/edit.html', locals(), context_instance=RequestContext(request))


def manage_product_image(request, productId):
	try:
		product = Product.objects.get(id=productId)
	except:
		product = False

	if request.user == product.user:
		ProductImageFormset = modelformset_factory(ProductImage, form=ProductImageForm, can_delete=True)
		
		queryset = ProductImage.objects.filter(product=product)
		formset = ProductImageFormset(request.POST or None, request.FILES or None, queryset=queryset)
		form = ProductImageForm(request.POST or None, instance=product)

		if formset.is_valid():
			for form in formset:
				instance = form.save(commit=False)
				instance.product = product
				instance.save()
			if formset.deleted_forms:
				formset.save()

		#if request.method == 'POST':
		#	formset = ProductImageFormset(request.POST, request.FILES)

		return render_to_response('products/manage_images.html', locals(), context_instance=RequestContext(request))
	else:
		raise Http404
	

def edit_product(request, productId):	
	product = Product.objects.get(id=productId)
	
	if request.user == product.user:
		form = ProductForm(request.POST or None, instance=product)

		if form.is_valid():
			product_edit = form.save()

		return render_to_response('products/edit.html', locals(), context_instance=RequestContext(request))
	else:
		raise Http404

