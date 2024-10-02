from django.http import HttpResponse
from django.shortcuts import render

def cadastrar_vendedor(request):
    return HttpResponse("Página de cadastro de vendedor")

def liberar_descontos(request):
    return HttpResponse("Página de liberar descontos")

