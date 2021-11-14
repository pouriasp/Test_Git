from django.shortcuts import render

from dodoTA.forms import form1
from dodoTA.models import havijpolomorgh
# Create your views here.
def test(request):
    return render(request, 'doseTAhafta.html')
def testinput(request):
    havij=havijpolomorgh()
    havij.save()
    return render(request,"doseTAhafta.html")
def show_shalgham(request):
    h=havijpolomorgh.objects.all()
    return render(request, "doseTAhafta.html", {"friends":h})
def form2(request):
    form=form1()
    if
    return render(request, "formsavegar.html",{"myform":form})
