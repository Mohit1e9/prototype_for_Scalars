from django.shortcuts import render
from Screen_01.Utilities import finalScalar
from django.views import View
from django.http import HttpResponse

class Prototype_01(View):
    
    scalar=finalScalar()
    template_name = 'Basix.html'

    def get(self,request):
        return render(request,self.template_name,self.scalar)
    
    def post(self,request):
        return render(request,self.template_name,self.scalar)

