from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def home_view(request):
    return render(request, 'index.html')

def validar_usuario(request):
    if request.method == 'POST':
        v_usuario = request.POST.get('usuario')
        v_contrasena = request.POST.get('contrasena')

        user = authenticate(request, username=v_usuario, password=v_contrasena)

        if user is not None:
            login(request, user)
            request.session['usuario_id'] = user.id

            return JsonResponse({
                'success': True,
                'redirect_url': '/inicio_panel/'
            })
        else:
            return JsonResponse({
                'success': False,
                'mensaje': 'Credenciales incorrectas'
            })

    return render(request, 'index.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'inicio_panel.html')

# Aca se agrega la ruta del boton de agregar usuario en el panel de admin

def AD_usuario(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'AD_usuario.html')

def AD_inventario(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'AD_inventario.html')

def AD_ventas(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    return render(request, 'AD_ventas.html')

def AD_categorias(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'AD_categorias.html')

def AD_marcas(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'AD_marcas.html')

def AD_proveedores(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'AD_proveedores.html')

def AD_metodopago(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'AD_metodopago.html')

def AD_descuentos(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'AD_descuentos.html')

def configuración_view(request):
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, 'Complementos/configuración.html')

def cerrar_sesion(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/inicio/')