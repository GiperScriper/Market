from django.conf import settings
from django.conf.urls import patterns, include, url



urlpatterns = patterns('products.views',
    
    #url(r'^$', 							'list_products', name='all_products'),
    url(r'^(?P<productId>\d+)/$', 		'product', name='single_product'),
    url(r'^(?P<productId>\d+)/edit/$', 		'edit_product', name='edit_product'),
    
)
