from django.shortcuts import redirect, render
from django.views import View

from register_car.form import RegisterCarForms
from register_car.models import RegisterCar




def list_all(request):
    register_car = RegisterCar.objects.all()
    return render(request, 'car_list_all.html', {'register_car': register_car})


def create(request):
    form = RegisterCarForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_all_car')
    return render(request, 'car_form.html', {'form': form})

def update(request, id):
    register_car = RegisterCar.objects.get(id=id)
    form = RegisterCarForms(request.POST or None, instance=register_car)
    if form.is_valid():
        form.save()
        return redirect('list_all_car')
    return render(request, 'car_form.html', {'form':form})

def delete(request, id):
    register_car = RegisterCar.objects.get(id=id)
    register_car.delete()
    return redirect('list_all_car')


