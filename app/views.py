import requests #nos permite leer API
from email import message
from django.shortcuts import render, redirect
from app.forms import ProductoForm
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group

# Create your views here.

# SECCIÓN LISTAR

def index(request):
    return render(request, 'app/index.html')

@login_required
def direccion(request):
    request.session.set_expiry(6000)
    return render(request, 'app/direccion.html')

def iniciarsesion(request):
    return render(request, 'app/iniciar-sesion.html')

@login_required
def perfil(request):
    num_visitas = request.session.get('num_visitas',0)
    request.session ['num_visitas'] = num_visitas + 1
    request.session.set_expiry(3000)
    datos = {'visitas': num_visitas}
    return render(request, 'app/perfil.html',datos)

def detalleproducto(request):       
    return render(request, 'app/detalle-producto.html',)

def producto(request):

    id_user = request.user.id
    productoAll = Producto.objects.all()
    carritoAll = Carrito.objects.all()
    datos = {
        'listaProductos' : productoAll,
        'carritoTodo': carritoAll,
        'id' : id_user      
    }
   

    if request.method == 'POST':
        producto = Producto.objects.get(codigo=request.POST.get('codigo'))
        producto.stock=producto.stock-1        

        codigo = request.POST.get('codigo')
        producto = Producto.objects.get(codigo=codigo)
        if producto == Producto.objects.get(codigo=codigo):
            if producto.stock > 0:
                producto.stock = producto.stock -1
                producto.save()
            else:
                producto.stock == 0
                producto.save()
        producto.save()

        carrito = Carrito()
        # carrito.producto = producto 
        carrito.codigo = request.POST.get('codigo')
        carrito.nombre = request.POST.get('nombre')
        carrito.precio = request.POST.get('precio')        
        carrito.precioSub = request.POST.get('precioSub')    
        carrito.imagen = request.POST.get('imagen')
        carrito.stock = request.POST.get('stock')
        carrito.usuario = id_user

        carrito.cantidad = 1
  

        if Carrito.objects.filter(codigo=request.POST.get('codigo')).exists():
            for x in carritoAll:
                if x.nombre == carrito.nombre:
                    if x.usuario == id_user:                       
                        x.cantidad = x.cantidad + 1
                        x.save()
                    else:            
                        carrito.cantidad = 1
                        carrito.save()
            
        else:            
            carrito.cantidad = 1
            carrito.save() 
        
        
            
    return render(request, 'app/producto.html', datos)

 
#CARRITO 
@login_required
def carrito(request, id):
    carritoAll = Carrito.objects.filter(usuario=id)

    datos = {
        'listarCarrito' : carritoAll,
        'usuario' : 0
    }

    listatotales = carritoAll
    datos['total'] = 0

    usuario = request.user.email
    if Suscriptor.objects.filter(email=usuario).exists():
        datos['usuario'] = 1
        for x in listatotales:
            datos['subtotal'] = round((x.precio * x.cantidad + datos['total'])*0.95)
            datos['total'] = x.precio * x.cantidad + datos['total']
            datos['descuento'] =round(datos['total']*0.05)
    else:
        for y in listatotales:
            datos['total'] = y.precio * y.cantidad + datos['total']

    if request.method == 'POST':
        for x in carritoAll:
            seguimiento = Seguimiento()
            seguimiento.codigo = x.codigo
            seguimiento.nombre = x.nombre
            seguimiento.precio = x.precio
            seguimiento.usuario = x.usuario
            seguimiento.precioSub = x.precioSub
            seguimiento.imagen = x.imagen
            seguimiento.cantidad = x.cantidad
            seguimiento.estado = "Pago aprobado!"
            seguimiento.save()

        carritoAll.delete()   
        datos['mensaje'] = 'pagado'   
        messages.success(request,'Tus productos han sido pagados con exito!')

    return render(request, 'app/carrito.html',datos)


def eliminar_carrito(request,codigo):
    carrito = Carrito.objects.get(codigo=codigo)
    usuario =str(carrito.usuario)
    producto = Producto.objects.get(codigo=carrito.codigo)
    producto.stock += carrito.cantidad 
    producto.save()
    carrito.delete()

    return redirect('/carrito/'+usuario)

#SEGUIMIENTO 

@login_required
def seguimiento(request):
    request.session.set_expiry(6000)

    datos ={ }

    if request.method == 'POST':
        carrito = Carrito()
        carrito.codigo = request.POST.get('codigo')
        carrito.nombre = request.POST.get('nombre')
        carrito.precio = request.POST.get('precio')
        carrito.cantidad = request.POST.get('cantidad')
        carrito.precioSub = request.POST.get('precioSub')    
        carrito.imagen = request.POST.get('imagen')
        estado = request.POST.get('estado')
        print(carrito)
        datos["producto"] = carrito
        datos["estado"] = estado

    return render(request, 'app/seguimiento.html',datos)


#MIS PEDIDOS 

@login_required
def pedido(request,id):

    seguimientoAll = Seguimiento.objects.filter(usuario=id)
    datos={
        'listaCompras' : seguimientoAll

    }
   
    return render(request, 'app/pedido.html',datos)

#PRODUCTOS API

def productoApi(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()     
    datos = {        
        'listaJson' : response,
        
        
    }
    

    if request.method == 'POST':
        producto = Producto.objects.get(codigo=request.POST.get('codigo'))
        producto.stock=producto.stock-1
        producto.save()

        carrito = Carrito()
        # carrito.producto = producto 
        carrito.codigo = request.POST.get('codigo')
        carrito.nombre = request.POST.get('nombre')
        carrito.precio = request.POST.get('precio')        
        carrito.precioSub = request.POST.get('precioSub')    
        carrito.imagen = request.POST.get('imagen')
        carrito.stock = request.POST.get('stock')


        carrito.cantidad = 1
        
    return render(request, 'app/producto-api.html', datos)

def apiRick(request):
    response2 = requests.get('https://rickandmortyapi.com/api/character').json()   
    datos = {        
        'listaRick' : response2['results']       
    
    }
            
    return render(request, 'app/rickandmorty.html', datos)

# SECCIÓN FORMULARIOS

# LISTAR PRODUCTOS

@permission_required('app.view_producto')
def listar_producto(request):
    request.session.set_expiry(3600)
    productoAll = Producto.objects.all()
    datos = {
        'listaProductos' : productoAll
    }

    return render(request, 'app/listar_producto.html', datos)

# AGREGAR PRODUCTOS
@permission_required('app.add_producto')
def agregar_producto(request):
    request.session.set_expiry(3600)
    datos = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
        
    return render(request, 'app/agregar_producto.html', datos)

# MODIFICAR PRODUCTOS 
@permission_required('app.change_producto')
def modificar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario
        else :
            datos['mensaje'] = formulario.errors
    return render(request, 'app/modificar_producto.html', datos)
 

# ELIMINAR PRODUCTOS 
@permission_required('app.delete_producto')
def eliminar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_producto")


# REGISTRO DE USUARIOS 
def registro(request):
    datos = {
        'form' : UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Te has registrado exitosamente!'
        else :
            datos['mensaje'] = formulario.errors
    
    return render(request, 'app/registro.html', datos)


#LISTAR USUARIO 

@permission_required('app.view_user')
def listar_usuario(request):
    request.session.set_expiry(3600)
    registroAll = User.objects.all()
    datos = {
        'listarUsuario' : registroAll
    }
    return render(request, 'app/listar_usuario.html', datos)

# ELIMINAR USUARIO 
@permission_required('app.delete_usuario')
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    

    return redirect(to="listar_usuario")

#MODIFICAR USUARIO 
@permission_required('app.change_usuario')
def modificar_usuario(request, id):
    usuario = User.objects.get(id=id)
    datos = {
        'form' :FormularioUserResgistro(instance=usuario)
    }
    if request.method == 'POST':
        formulario = FormularioUserResgistro(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario modificado correctamente!'
            datos['form'] = formulario
        else :
            datos['mensaje'] = formulario.errors
    return render(request, 'app/modificar_usuario.html', datos)
 
#SUSCRIPCION
@login_required
def sub(request):
    datos = {
        'form' : SuscriptorForm(),
        'usuario' : 0
    }
    usuario = request.user.email
    if Suscriptor.objects.filter(email=usuario).exists():
        datos['usuario'] = 1
    
    
    if request.method == 'POST':
        if request.POST.get('email') == 'asdasd':
            desub = Suscriptor.objects.filter(email=usuario)
            desub.delete()
            datos['usuario'] = 0
        
        else:
            sus = Suscriptor()
            sus.email = request.POST.get('email')
            sus.sub = True
            sus.save()
            datos['usuario'] = 1
       
    return render(request, 'app/sub.html',datos)


#REGISTRO DE USUARIOS

def registro_usuario(request):       
    datos = {
        'form' : FormularioUserResgistro()
    }
    if request.method == 'POST':
        formulario = FormularioUserResgistro(data=request.POST)
        if formulario.is_valid():           
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/registro_usuario.html',datos)

