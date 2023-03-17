from django.urls import path
from AppPedidos import views


urlpatterns = [
  
    
    path('',views.procesar_pedido, name='procesar_pedido' ),  
    

]