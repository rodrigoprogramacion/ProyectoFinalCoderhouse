from django.urls import path
from AppProyectoFinal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home' ),       
    path('quienesSomos/',views.quienesSomos, name='quienesSomos' ),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)