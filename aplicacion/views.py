from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect
from django.utils import timezone #para importar la hora , es para el carro y su envio
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
#desde el crud del profe
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages 
from .models import Persona, Producto, Envio, Pedido,Carrito ,Usuario, DetallePedido
from os import path, remove 
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PersonaForm, UpdatePersonaForm, ProductoForm, UpdateProductoForm, CrearCuentaForm #para formularios de persona y productos


def index (request):
    
    Local = Producto.objects.get(nombre="Local")
    Tercero = Producto.objects.get(nombre="Tercero")
    Visita = Producto.objects.get(nombre="Visita")
    
    datos={

        "Tercero":Tercero,
        "Local":Local,
        "Visita":Visita
    }
    
    return render(request, "aplicacion/index.html", datos)

def salir(request):
    logout(request)
    return redirect(to='index')


def about (request):
    return render(request, "aplicacion/about.html")
def admini (request):
    return render(request, "aplicacion/admini.html")

from django.shortcuts import render, get_object_or_404, redirect
from .models import Carrito, Usuario

@login_required
def cart(request):
    user = request.user
    usr = get_object_or_404(Usuario, nombusuario=user)
    carritos = Carrito.objects.filter(usuario_id=usr)
    productos = Producto.objects.all()
    subtotal = sum(c.get_total_price() for c in carritos)

    datos = {
        "carritos": carritos,
        "productos": productos,
        "subtotal": subtotal,
    }

    print("Y aqui")  

    if request.method == 'POST':
        print("Pasa por aca?")  
        id = request.POST.get('id')  
        print(f"Carrito ID: {id}")  
        
        carrito = get_object_or_404(Carrito, id=id, usuario=usr)
        carrito.delete() 

        carritos = Carrito.objects.filter(usuario=usr)
        subtotal = sum(c.get_total_price() for c in carritos)
        datos['carritos'] = carritos
        datos['subtotal'] = subtotal


        return redirect('cart')

    return render(request, "aplicacion/cart.html", datos)
####################################################################
def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, cod_producto=id)

    if request.method == "POST":
        if producto.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+producto.imagen.url))
        producto.delete()
        messages.success(request, 'Producto Eliminado')
        return redirect('productos')

    datos = {
        "producto": producto
    }

    return render(request, 'aplicacion/eliminarproducto.html', datos)
####################################################################

@login_required
def eliminar_carrito(request, id):
    if request.method == 'POST':
        carrito_id = id
        carrito = get_object_or_404(Carrito, id=carrito_id, usuario=request.user.usuario)
        # Delete the cart item
        carrito.delete()
        # Optionally, you can print or log a message to confirm deletion
        print(f'Carrito eliminado correctamente: {carrito_id}')
        # Redirect back to the cart page or any other desired page
        return redirect('cart')
    else:
        # Handle the case where the request method is not POST (optional)
        print(f'No se recibió una solicitud POST para eliminar el carrito con ID: {id}')
        return redirect('cart')  # Redirect to the cart page in case of any issue
    
def checkout (request):
    
    if request.method == 'POST':
        print(f'Solicitud POST recibida para eliminar el carrito con ID: {id}')
        subtotal = request.POST.get('subtotal', 0)  
        print(f'Carrito con ID {id} eliminado exitosamente.')

        return render(request, 'aplicacion/checkout.html', {'subtotal': subtotal})
    
    return render(request, 'aplicacion/checkout.html', {'subtotal': subtotal})

@login_required
def estado (request):
    user = request.user
    usr = get_object_or_404(Usuario, nombusuario=user) 
    pedidos_usuario = Pedido.objects.filter(usuario_id=usr)
    pedidos = Pedido.objects.filter(usuario_id=usr)
    detallepedido= DetallePedido.objects.all()
    datos = {
        'pedidos': pedidos,
        'detallepedido': detallepedido,
    }
    return render(request, "aplicacion/estado.html",datos)


#############################################

##############################################

def detallepedido(request,id):
    detallepedido = get_list_or_404(DetallePedido, pedido_id=id)
    datos = {
        'detallepedido':detallepedido   
    }
    return render(request, "aplicacion/detallepedido.html",datos)

@login_required
def miscompras(request):
    #obtener el carro del usuario en especifico ##terminar 
    user = request.user
    usr = get_object_or_404(Usuario, nombusuario=user) 
    pedidos = Pedido.objects.filter(usuario_id=usr)
    datos = {
        'pedidos': pedidos,
        'detallepedido': detallepedido,
    }

    return render(request, "aplicacion/miscompras.html", datos)

def panelcerrarsesion (request):
    return render(request, "aplicacion/panelcerrarsesion.html")
def panelcontrol (request):
    return render(request, "aplicacion/panelcontrol.html")
#para que se vean los pedidos en panel control estado 
def panelcontrolestadocompra (request):
    pedidos=Pedido.objects.all()
    datos={

        "pedidos":pedidos
    }
    return render(request, "aplicacion/panelcontrolestadocompra.html", datos)

def crearcuenta (request):
    form=CrearCuentaForm()
    datos={
        "form":form
    }
    if request.method=="POST":
        form=CrearCuentaForm(data=request.POST)
        usr=request.POST["username"]
        existe=User.objects.filter(username=usr).exists()  
        if existe:
            alerta="El usuario ya existe"
            datos={
                "form":form,
                "alerta":alerta
            }
        else:
            if form.is_valid():
                # Guardar el usuario en la tabla User de Django
                usuario_django = form.save()
                
                # Crear la instancia de Usuario y guardarla en la tabla Usuario
                usuario_personalizado = Usuario(nombusuario=usuario_django.username, pwd=usuario_django.password)
                usuario_personalizado.save()
                
                return redirect(to="login")
            datos = {
                "form": form
            }
    return render(request, "registration/crearcuenta.html", datos)

#def sesion (request):
#    return render(request, "aplicacion/sesion.html")

def shop (request):
    
    productos=Producto.objects.all()

    datos={

        "productos":productos
    }
    
    return render(request, "aplicacion/shop.html", datos)

@login_required
def comprar(request, id):
    print("Request method:", request.method)
    producto = get_object_or_404(Producto, cod_producto=id)
    
    if request.method == 'POST' and 'add-to-cart' in request.POST:
        print("Form submitted")
        usuario = Usuario.objects.get(nombusuario=request.user.username)
        envio = Envio.objects.first()
        
        # Buscar si el producto ya está en el carrito del usuario
        carrito_existente = Carrito.objects.filter(usuario=usuario, producto=producto).first()
        
        if carrito_existente:
            # Si el producto ya está en el carrito, aumentar la cantidad en 1
            carrito_existente.cantidad += 1
            carrito_existente.save()
        else:
            # Si el producto no está en el carrito, crear un nuevo item de carrito
            carrito = Carrito(usuario=usuario, envio=envio, producto=producto, cantidad=1)
            carrito.save()
        
        return redirect('cart')
    
    datos = {
        "producto": producto
    }
    
    return render(request, "aplicacion/comprar.html", datos)



@login_required
@require_POST
def thankyou(request):
    if request.method == 'POST':
        primer_nombre = request.POST.get('primer_nombre', '')
        segundo_nombre = request.POST.get('segundo_nombre', '')
        apellido = request.POST.get('apellido', '')
        direccion = request.POST.get('direccion', '')
        correo = request.POST.get('correo', '')
        celular = request.POST.get('celular', '')
        region = request.POST.get('region', '')
        adicional = request.POST.get('adicional', '')

        nombre_cliente = primer_nombre + (' ' + segundo_nombre if segundo_nombre else '') + ' ' + apellido

        
        try:
            user = request.user
            usr = get_object_or_404(Usuario, nombusuario=user) 
            Pedido.objects.create(
                usuario = usr,
                nombre_cliente=nombre_cliente,
                direccion=direccion,
                correo=correo,
                celular=celular,
                region=region,
                adicional=adicional,  
                fecha_pedido=timezone.now(),  
                estado='en_proceso'  
            )
            user = request.user
            usr = get_object_or_404(Usuario, nombusuario=user) 
            carritos_usuario = Carrito.objects.filter(usuario_id=usr)
            print(carritos_usuario)
            
            ultimo_pedido = Pedido.objects.latest('id')
            ultimo_id_pedido = ultimo_pedido.id
            ##** Suponiendo que tienes un producto específico que quieres agregar al detalle de pedido
            #productos = get_object_or_404 (Producto, id=ultimo_id_pedido) ##** Obtén el producto que deseas agregar al detalle
            #crear el detalle con el ultimo id de pedido mas todos los item del usuario logeado
            
            for carrito in carritos_usuario:
                    detalle_pedido = DetallePedido.objects.create(
                        pedido= ultimo_pedido,
                        producto=carrito.producto,
                        cantidad=carrito.cantidad
                    )
                    carrito.delete()

        except Exception as e:
            print(f"Error al procesar pedido: {str(e)}")
            return redirect('index')  

    return render(request, "aplicacion/thankyou.html")

 
def personas(request):
 
    
    personas=Persona.objects.all()

    datos={

        "personas":personas
    }

    return render(request,'aplicacion/personas.html', datos)

def crearpersona(request):
    form=PersonaForm()
    
    if request.method=="POST":
        form=PersonaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona agregada')
            return redirect(to="personas")
    
    datos={
        "form":form
    }
    return render(request, 'aplicacion/crearpersona.html', datos)

def crearproducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona Agregada')
            return redirect('productos') 
    else:
        form = ProductoForm()

    datos = {
        'form': form
    }
    return render(request, 'aplicacion/crearproducto.html', datos)

def modificarpersona(request, id):
    persona = get_object_or_404(Persona, cod_persona=id)

    form = UpdatePersonaForm(instance=persona)
    datos = {
        "form": form,
        "persona": persona
    }

    if request.method == "POST":
        form = UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Pesona Modificada')
            return redirect(to="personas")

    return render(request, 'aplicacion/modificarpersona.html', datos)

def modificarproducto(request, id): #******
    producto=get_object_or_404(Producto, cod_producto=id) #**********

    form=UpdateProductoForm(instance=producto)
    datos={
        "form":form,
        "producto":producto
    }

    if request.method=="POST":
        form=UpdateProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto Modificado')
            return redirect(to="productos")
        
    return render(request,'aplicacion/modificarproducto.html',datos)

#ELIMINAR , VER EL CRUD DEL PROFE Y ADAPTARLO A NUESTRA PAGINA
def eliminarpersona(request, id):
    persona = get_object_or_404(Persona, cod_persona=id) 

    datos = {
        "persona": persona
    }

    if request.method == "POST":
        if persona.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','') + persona.imagen.url))
        persona.delete()
       #  "remove(path.join(str(settings.MEDIA_ROOT).replace('media/') persona.imagen.url))) Esto es siempre y cuando que la imagen no sirva"
        messages.error(request, 'Persona eliminada')
        return redirect(to="personas")
    return render(request, 'aplicacion/eliminarpersona.html', datos)


def eliminarproducto(request, id):
    producto = get_object_or_404(Producto, cod_producto=id)

    if request.method == "POST":
        if producto.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+producto.imagen.url))
        producto.delete()
        messages.success(request, 'Producto Eliminado')
        return redirect('productos')

    datos = {
        "producto": producto
    }

    return render(request, 'aplicacion/eliminarproducto.html', datos)

#---------OTRAS VISTAS--------------------#
def alguna_vista(request):
    persona_id = 1 
    return redirect('modificar_persona', id=persona_id)

def modificar_persona(request, id):
    persona = get_object_or_404(Persona, cod_persona=id)

    form = UpdatePersonaForm(instance=persona)
    datos = {
        "form": form,
        "persona": persona
    }

    if request.method == "POST":
        form = UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            return redirect(to="personas")

    return render(request, 'aplicacion/modificarpersona.html', datos)

def productos(request):
    productos=Producto.objects.all()

    datos={

        "productos":productos
    }

    return render(request,'aplicacion/productos.html', datos)

def orden_estado(request, idcompra):
     Envio = get_object_or_404(Envio, idcompra=idcompra)
     datos = {
        "Envio": Envio
    }
     return render(request, 'aplicacion/estado.html', datos)
 
 #Esto es experimental, si se requiere se saca
def panel_control(request):
    # Obtener todos los pedidos ordenados por fecha de pedido descendente
    pedidos = pedidos.objects.all().order_by('-fecha_pedido')
    
    context = {
        'pedidos': pedidos
    }
    
    return render(request, 'panel_control.html', context)

def api_pedidos(request):
    pedidos = Pedido.objects.all()
    data = []
    
    for pedido in pedidos:
        productos_pedido = pedido.productos.all()  # Suponiendo que 'productos' es un campo ManyToManyField en tu modelo Pedido
        
        for producto in productos_pedido:
            data.append({
                'id': pedido.id,
                'nombre_cliente': pedido.nombre_cliente,
                'fecha_pedido': pedido.fecha_pedido,
                'estado': pedido.estado,
                'nombre_producto': producto.nombre,  # Accedes al nombre del producto
                'precio_producto': producto.precio,  # Ejemplo: acceder al precio del producto
                # Agrega más campos del producto que necesites
            })
    return JsonResponse(data, safe=False)

@csrf_exempt
def actualizar_estado_pedido(request, pedido_id, nuevo_estado):
    if request.method == 'POST':
        try:
            pedido = Pedido.objects.get(id=pedido_id)
            pedido.estado = nuevo_estado
            pedido.save()
            return JsonResponse({'status': 'success'}, status=200)
        except Pedido.DoesNotExist:
            return JsonResponse({'error': 'Pedido no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def actualizar_boleta_pedido(request, pedido_id, nueva_boleta):
    if request.method == 'POST':
        try:
            pedido = Pedido.objects.get(id=pedido_id)
            pedido.boleta = nueva_boleta == 'true'
            pedido.save()
            return JsonResponse({'status': 'success'}, status=200)
        except Pedido.DoesNotExist:
            return JsonResponse({'error': 'Pedido no encontrado'}, status=404)
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirigir al usuario a la página de inicio (index)
            return redirect('index')
        else:
            # Manejar el caso de inicio de sesión inválido
            # Puedes agregar lógica para mostrar un mensaje de error en el template login.html
            pass
    
    return render(request, 'login.html')

def actualizar_cantidad(request, id):
    if request.method == "POST":
        producto = get_object_or_404(Producto, cod_producto=id)
        nueva_cantidad = int(request.POST.get('cantidad'))

        carrito = request.session.get('carrito', {})

        if id in carrito:
            carrito[id]['cantidad'] = nueva_cantidad
            carrito[id]['subtotal'] = nueva_cantidad * producto.precio
        else:
            carrito[id] = {'cantidad': nueva_cantidad, 'subtotal': nueva_cantidad * producto.precio}

        request.session['carrito'] = carrito

        total = sum(item['subtotal'] for item in carrito.values())

        return JsonResponse({'subtotal': carrito[id]['subtotal'], 'total': total})
    return redirect('carrito')  