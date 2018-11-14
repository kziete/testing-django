# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from models import ModeloUno
# Create your views here.

class ListaView(ListView):
    template_name = "lista.html"
    queryset = ModeloUno.objects.all()

class DetalleView(DetailView):
    template_name = "detalle.html"
    queryset = ModeloUno.objects.all()

class CrearView(CreateView):
    template_name = "crear.html"
    fields = ("nombre",)
    queryset = ModeloUno.objects.all()
    success_url = "/"