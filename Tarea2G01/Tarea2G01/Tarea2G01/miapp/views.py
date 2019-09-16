from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def Agendar(request):
	return render(request, 'Agendar.html')

def contacto(request):
	return render(request, 'contacto.html')

def registros(request):
	return render(request, 'registros.html')	

def listo(request):
	diccionario0={}
	return render(request, "listo.html", diccionario0)	

def inicio(request):
	return render(request, 'inicio.html')	

def recuperar(request):
	diccionario={}
	items=request.POST.getlist('inputCheck')
	diccionario["item1"]=items
	return render(request, "mostrar_resultado.html", diccionario)

def inventario(request):
	return render(request, 'inventario.html')

def recuperar_inv(request):
	diccionario2={}
	return render(request, "mostrar_inventario.html", diccionario2)

