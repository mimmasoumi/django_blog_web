from django.urls import path
from .views import AboutUs, ContactUs, Index, Search, ShowGroup, Single


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('article<int:article_id>/<str:article_title>', Single.as_view()),
    path('search', Search.as_view()),
    path('contactus/', ContactUs.as_view()),
    path('group<group_id>/<str:group_title>', ShowGroup.as_view()),
    path('aboutus/', AboutUs.as_view())
]
