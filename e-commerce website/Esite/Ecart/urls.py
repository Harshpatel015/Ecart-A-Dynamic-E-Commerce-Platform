"""
URL configuration for Esite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Ecart import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("test/",views.test),
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("tracker/",views.tracker,name="tracker"),
    path("search/",views.search,name="search"),
    path("productview_category/<prd_category>",views.productview_category,name="productview_category"),
    path("productview_SUB_category/<prd_subcategory>",views.productview_SUB_category,name="productview_SUB_category"),
    path("productdetails_page/<product_id>" , views.productdetails_page , name="productdetails_page"),
    path("confirmation_page/<product_id>",views.confirmation_page,name="confirmation_page"),
    path("shipping_fillup/",views.shipping_fillup,name="shipping_fillup"),
    path("shipping_add_order_displayed/",views.shipping_add_order_displayed,name="order_page"),
    path("shipping_add_edit/<product_id>",views.shipping_add_edit,name="shipping_add_edit"),
    path("succesfullyorderplaced/<product_id>",views.done,name="done")
]



# Serve media files during development
