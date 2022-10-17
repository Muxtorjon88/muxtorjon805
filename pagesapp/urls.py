from django.urls import path
from .views import HomePageView, HodimlarPageView, YuldashevaPageView, TuychievPageView, ZiyodulloPageView, BulimlarPageView
urlpatterns = [
    path('bulimlar/', BulimlarPageView.as_view(), name='bulimlar'),
    path('ziyodulli/', ZiyodulloPageView.as_view(), name='ziyodullo'),
    path('tuychiev/', TuychievPageView.as_view(), name='tuychiev'),
    path('yuldasheva/', YuldashevaPageView.as_view(), name='yuldasheva'),
    path('hodimlar/', HodimlarPageView.as_view(), name='hodimlar'),
    path('', HomePageView.as_view(), name='home'),
]