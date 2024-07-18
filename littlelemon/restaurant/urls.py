from django.contrib import admin 
from rest_framework.routers import DefaultRouter
from django.urls import path ,include
from . import views

router = DefaultRouter()  
router.register(r'tables', views.BookingViewSet)

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()), 
    path('booking/', include(router.urls)),
]