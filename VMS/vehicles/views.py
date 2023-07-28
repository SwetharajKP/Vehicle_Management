from django.shortcuts import render,get_object_or_404,redirect
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html',{'vehicles':vehicles})

def vehicle_detail(request,vehicle_id):
    vehicle = get_object_or_404(Vehicle,pk=vehicle_id)
    return render(request,'vehicles/vehicle_detail.html',{'vehicle':vehicle})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request,'vehicles/vehicle_form.html',{'form':form})

def vehicle_update(request,vehicle_id):
    vehicle = get_object_or_404(Vehicle,pk=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST,instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/vehicle_form.html',{'form': form})

def vehicle_delete(request,vehicle_id):
    vehicle = get_object_or_404(Vehicle,pk=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_confirm_delete.html',{'vehicle':vehicle})