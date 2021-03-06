# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView, ModelFormSetView
from django_addanother.views import CreatePopupMixin
from django.apps import apps
from inventario.models import *
from .models import *
from .forms import *
from inventario.forms import *

# Create your views here.


class Compras(LoginRequiredMixin, ListView):
    model = Compra
    login_url = "/login/"
    template_name = "contabilidad/compras.html"
    context_object_name = 'compras'


class InsumoInline(InlineFormSet):
    model = CompraInsumo
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class Compra_insumos(LoginRequiredMixin, CreateWithInlinesView):
    model = Compra
    fields = '__all__'
    login_url = "/login/"
    inlines = [InsumoInline]
    success_url = "/compras"
    template_name = "contabilidad/compra_insumos.html"


class ServicioInline(InlineFormSet):
    model = Servicio
    fields = "__all__"
    factory_kwargs = {'extra': 1}


class Compra_servicio(LoginRequiredMixin, CreateWithInlinesView):
    model = Compra
    fields = '__all__'
    login_url = "/login/"
    inlines = [ServicioInline]
    success_url = "/compras"
    template_name = "contabilidad/compra_servicio.html"

    def get_context_data(self, **kwargs):
        context = super(Compra_servicio, self).get_context_data(**kwargs)
        # Envio la variable no_fields al contexto para filtrar los campos del formset de equipamiento
        context['no_fields'] = ["Id", "Compra", "lleno",
                                "carbonatado", "observaciones", "Eliminar", ]
        return context


class EquipamientoInline(InlineFormSet):
    model = Barril
    fields = "__all__"
    factory_kwargs = {'extra': 1}

    def __init__(self, *args, **kwargs):
        try:
            # Selecciono args 3 que contiene el valor de equipamiento
            arg = args[3]
            equipamiento = arg["equipamiento"]
            # uso el valor de equipamiento para seleccionar el modelo dentro de la aplicacion inventario
            if equipamiento == "fermentador":
                self.model = apps.get_model(
                    app_label="inventario", model_name="Fermentador")
            elif equipamiento == "pallet":
                self.model = apps.get_model(
                    app_label="inventario", model_name="Pallet")
        except:
            pass
        return super(EquipamientoInline, self).__init__(*args, **kwargs)


class Compra_equipamiento(LoginRequiredMixin, CreateWithInlinesView):
    model = Compra
    fields = '__all__'
    login_url = "/login/"
    inlines = [EquipamientoInline]
    success_url = "/compras"
    template_name = "contabilidad/compra_equipamiento.html"

    def get_context_data(self, **kwargs):
        context = super(Compra_equipamiento, self).get_context_data(**kwargs)
        # Envio la variable no_fields al contexto para filtrar los campos del formset de equipamiento
        context['no_fields'] = ["Id", "Compra", "Lleno",
                                "Carbonatado", "Observaciones", "Eliminar"]
        return context


class EditInsumoInline(InlineFormSet):
    model = CompraInsumo
    fields = "__all__"
    #factory_kwargs = {'extra': 1}


class Compra_editar(LoginRequiredMixin, UpdateWithInlinesView):
    model = Compra
    login_url = "/login/"
    inlines = [EditInsumoInline]
    fields = '__all__'
    template_name = "contabilidad/compra_edit.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        producto = request.POST.get("producto")
        if producto == "barril":
            formset = BarrilFormSet(self.request.POST, instance=self.object)
        elif producto == "servicio":
            formset = ServicioFormSet(self.request.POST, instance=self.object)
        elif producto == "fermentador":
            formset = FermentadorFormSet(
                self.request.POST, instance=self.object)
        elif producto == "pallet":
            formset = PalletFormSet(self.request.POST, instance=self.object)
        else:
            formset = InsumoFormSet(self.request.POST, instance=self.object)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        elif not form.is_valid():
            return self.form_invalid(form)
        else:
            return self.form_invalid(formset)

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect("/compras")

    def form_invalid(self, form):
        response = form
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def get_context_data(self, **kwargs):
        context = super(Compra_editar, self).get_context_data(**kwargs)
        id = self.kwargs["pk"]
        compra = Compra.objects.get(id=id)
        context['barriles'] = BarrilFormSet(instance=compra)
        context['servicios'] = ServicioFormSet(instance=compra)
        context['fermentadores'] = FermentadorFormSet(instance=compra)
        context['pallets'] = PalletFormSet(instance=compra)
        context['insumos'] = InsumoFormSet(instance=compra)
        context['no_fields'] = ["id", "Compra", "Lleno",
                                "Carbonatado", "Observaciones", "Eliminar"]
        return context
