from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from django.views import View

from register_car.forms import RegisterCarForms
from register_car.models import RegisterCar as MRegisterCar


class RegisterCar(View):
    template = "register_car_form.html"
    form = RegisterCarForms

    def get(self, request, action=None, id=None):
        if action and action == "new":
            form_register_car = self.form
            return render(request, self.template, {"form": form_register_car})

        if action and action == "update" and id:
            return self.put(request, id=id)

        if action and action == "delete" and id:
            return self.delete(request, id=id)

        if action and action == "view" and id:
            register_car = MRegisterCar.objects.get(id=id)
            return render(request, "register_car_view.html", {"registercar": register_car})

        registercars = MRegisterCar.objects.all()
        return render(request, "register_car.html", {"registercars": registercars})

    def post(self, request, action=None, id=None):
        if id:
            data = MRegisterCar.objects.get(id=id)
            form_category = self.form(request.POST or None, instance=data)
        else:
            form_category = self.form(request.POST)
        if form_category.is_valid():
            form_category.save()
            return redirect("/registercar")

    def put(self, request, action=None, id=None):
        data = MRegisterCar.objects.get(id=id)
        form_register_car = self.form(initial=model_to_dict(data))
        return render(request, self.template, {"form": form_register_car})

    def delete(self, request, action=None, id=None):
        data = MRegisterCar.objects.get(id=id)
        data.delete()
        return redirect("/registercar")
