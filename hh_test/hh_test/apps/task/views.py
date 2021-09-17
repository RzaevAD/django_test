from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import VirtualMachineInterfaces as VMI
from django.contrib.auth.decorators import login_required

import json


def login(request):
    return render(request, 'login.html')


@login_required
def index(request):
    vmi = VMI.objects.all()
    # return HttpResponse(vmi)
    return render(
        request,
        'index.html',
        context={'vmi': vmi},
    )


@login_required
def updateIP(request, pk):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        obj = get_object_or_404(VMI, pk=pk)
        obj.ip = json_data['ip']
        obj.save()
    return HttpResponseRedirect('/')
