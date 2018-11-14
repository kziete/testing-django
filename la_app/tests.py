# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from la_app.models import ModeloUno
# Create your tests here.


class WebTest(TestCase):
    def setUp(self):
        modelos = [
            ModeloUno(nombre="Primero"),
            ModeloUno(nombre="Segundo"),
            ModeloUno(nombre="Tercero"),
        ]
        ModeloUno.objects.bulk_create(modelos)

    def test_lista(self):
        resp = self.client.get("/")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["object_list"].count(), 3)

    def test_detalle(self):
        m1 = ModeloUno.objects.all()[0]
        resp = self.client.get("/detalle/%d" % m1.id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["object"].nombre, m1.nombre)

    def test_crear_ok(self):
        data = {
            'nombre': 'holo'
        }
        resp = self.client.post("/agregar", data)
        self.assertEqual(resp.status_code, 302)
    
    def test_crear_fail(self):
        data = {}
        resp = self.client.post("/agregar", data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context["form"].errors), 1)

