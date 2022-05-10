from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Migros.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('urunler/', urunler, name="urunler"),
    # path('urunler/<int:id>/', urundetail, name="urun-detail"),
    path('urunler/<slug:slug>/', urundetail, name="urun-detail"),
    path('urun-listesi/', urun_listesi, name="urun-listesi"),
    path('calisanlar/', calisanlar, name="calisanlar"),
    path('calisanlar/<slug:slug>/', calisan_detail, name="calisan-detail"),
    path('aboutus/', aboutus, name="aboutus"),

    path('contactus/', ContactUs.as_view(), name="contactus"),

    path('', include('user.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)