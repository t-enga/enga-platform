from django.shortcuts import render, redirect, get_object_or_404
from boardmci.models import Mci,Mdp,Part
from django.http import JsonResponse


# Create your views here.

def board_mci (request):
    
    return render (request,'board_mci.html')

def get_mdps(request):
    mci_id = request.GET.get('mci_id')
    mdps = Mdp.objects.filter(id_mci=mci_id)
    data = [{'id_mdp': mdp.id_mdp, 'mdp_name': mdp.mdp_name} for mdp in mdps]
    return JsonResponse(data, safe=False)