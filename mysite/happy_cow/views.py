from django.http import HttpResponse
from django.shortcuts import render, redirect
from .blockchain import blockchain
import requests
import json
import datetime


auth = {
    '1': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTgzMTczNTcsIm5vbWUiOiJQcm9kdXRvcjEiLCJvcmciOiJQcm9kdXRvciIsImlhdCI6MTU1ODI4MTM1N30.d3rL1PQr0DWBKrybIvipIdP70HAhhHI1wOo6QQ5MXV8',
    '2': 2,
}

alias = {
    '1': 'produtormsp',
    '2': 2,
}


def produtor_view(request, id_produtor):

    if request.method == "GET":
        context = {'id': id_produtor}
        # context['bois'] = blockchain.get_allcattle(id_produtor)
        return render(request, 'happy_cow/producer_home.html', context)

    # elif request.method == "POST":
    #     # functionality 2
    # elif request.method == "PUT":
    #     # functionality 3
    # elif request.method == "DELETE":
    #     # functionality 4


def produtor_criar(request, id_produtor):

    context = {'id': id_produtor}

    if request.method == "POST":

        jwt = auth[id_produtor]
        context = {'id': id_produtor}
        prod = alias[id_produtor]

        blockchain.create_cattle(
            producer_id=prod, race=request.POST['raca'], father=request.POST['father'], mother=request.POST['mother'], weight=request.POST['weight'], jwt=jwt)

        return redirect('produtor_view', id_produtor=id_produtor)
    elif request.method == "GET":
        return render(request, 'happy_cow/producer_add.html', context)
    else:
        return redirect('produtor_view')


def produtor_cattle(request, id_produtor):

    if request.method == "GET":
        jwt = auth[id_produtor]
        prod = alias[id_produtor]

        context = {'id': id_produtor}
        context['bois'] = blockchain.get_all_cattle(prod, jwt)
        print(context['bois'])
        return render(request, 'happy_cow/producer_view.html', context)


def transfer2producer(request, id_produtor, id_boi):

    if request.method == "GET":
        context = {'id': id_produtor}
        context['producers'] = blockchain.get_all_cattle(id_produtor)
        return render(request, 'happy_cow/producer_transfer_producer.html', context)
    elif request.method == "POST":
        peso = int(request.POST['peso'])

        return HttpResponse(200)


def transfer2frigo(request, id_produtor):
    pass
