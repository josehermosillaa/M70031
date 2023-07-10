from django.shortcuts import render, redirect, HttpResponse
from .forms import EmpleadoForm
from .models import Empleado

# Create your views here.
def insertar_emp_view(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crudapp/mostrar/')
    form = EmpleadoForm()
    context = {'form':form}
    return render(request, 'crudapp/insertar.html', context)




def mostrar_emp_view(request):
    empleados = Empleado.objects.all()
    num_visitas =request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visitas+1
    context = {
        'empleados': empleados,
        'num_visitas':num_visitas,
    }
    return render(request, 'crudapp/mostrar.html', context)

def editar_emp_view(request,pk):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        print(request.POST)
        if form.is_valid():
            empleado = Empleado.objects.get(id=pk)
            empleado.emp_id = request.POST['emp_id']
            empleado.emp_nombre = request.POST['emp_nombre']
            empleado.emp_correo = request.POST['emp_correo']
            empleado.emp_designacion = request.POST['emp_designacion']
            empleado.save()
            return redirect('/crudapp/mostrar/')
    empleado = Empleado.objects.get(id=pk)
    form = EmpleadoForm(instance=empleado)
    context = {'form':form, 'empleado':empleado} 
    return render(request, 'crudapp/editar.html',context)


def eliminar_emp_view(request,pk):
    empleado = Empleado.objects.get(id=pk)
    if request.method == "POST":
        empleado.delete()

        return redirect('/crudapp/mostrar/')
    context={'empleado':empleado}
    return render(request, 'crudapp/eliminar.html', context)

def empleado_detalle_view(request, pk):
    empleado = Empleado.objects.get(id=pk)
    context = {'empleado':empleado}
    return render(request, 'crudapp/detalle.html',context=context)