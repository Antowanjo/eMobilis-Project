
from django.urls import path
from .views import about, category, contact, home, internship_detail, internship_list, testimonial
from Kenya import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('internship/<int:internship_id>/', internship_detail, name='internship_detail'),
    path('internship-list/', internship_list, name='internship_list'),
    path('testimonial/', testimonial, name='testimonial'),

]

