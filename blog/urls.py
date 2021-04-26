from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article<article_id>/<article_title>', views.single),
    path('search', views.search),
    path('contactus/', views.contactus),
    path('group<group_id>/<group_title>', views.show_group),
    path('aboutus/', views.about_us)
]