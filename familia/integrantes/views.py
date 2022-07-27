from django.shortcuts import render
from integrantes.models import Family

def create_member(request):
    new_member = Family.objects.create(name = 'Martin Ternovic', edad =29)
    context = {
        'new_member': new_member
    }
    return render(request, 'new_member.html', context=context)

def list_member(request):
    members = Family.objects.all() 
    context = {
        'members': members
    }
    return render(request, 'members_list.html', context=context)