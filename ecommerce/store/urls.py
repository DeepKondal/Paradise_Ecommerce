from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.store,name='store'),
    path('all',views.all,name='all'),

    path('product/<slug:product_slug>',views.product_info,name='product-info'),

    path('category/<slug:category_slug>',views.list_category,name='list-category')
        

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)