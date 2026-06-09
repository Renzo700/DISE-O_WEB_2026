from django.urls import path
from .views import home_view, validar_usuario, dashboard_view, AD_usuario, AD_inventario, AD_ventas, AD_categorias, AD_marcas, AD_proveedores, AD_metodopago, AD_descuentos, cerrar_sesion, configuración_view
urlpatterns = [
    path('inicio/', home_view, name='home'),
    path('validar/', validar_usuario, name='validar_usuario'),
    path('inicio_panel/', dashboard_view, name='inicio_panel'), # <-- NUEVA RUTA PARA EL PANEL
    path('usu/', AD_usuario, name='usuario'),
    path('inven/', AD_inventario, name='inventario'), # <-- NUEVA RUTA PARA EL PANEL
    path('ventas/', AD_ventas, name='ventas'),
    path('categorias/', AD_categorias, name='categorias'),
    path('marcas/', AD_marcas, name='marcas'),
    path('proveedores/', AD_proveedores, name='proveedores'),
    path('metodos-pago/', AD_metodopago, name='metodos_pago'),
    path('descuentos/', AD_descuentos, name='descuentos'),
    path('cerrar/', cerrar_sesion, name='cerrar'),
     path('configuración/', configuración_view, name='configuración'),
]

