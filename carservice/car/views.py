from django.shortcuts import render
from car.forms import carform
from car.models import carmodel
from django.views.generic import ListView, DetailView, UpdateView, CreateView,DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


def carview(request):
    form = carform()
    if request.method == 'POST':
        form = carform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('list')
    return render(request,'car/form.html',{'form':form})



class carlist(ListView):
    model = carmodel

class cardetail(DetailView):
    model = carmodel

class carcreate(CreateView):
    model = carmodel
    fields = '__all__'


class carupdate(UpdateView):
    model = carmodel
    fields = ('car_owner','car_color','car_number','description','service_type','submission_date','year_old','servicing')


class cardelete(DeleteView):
    model = carmodel
    success_url = reverse_lazy('list')




from django.http import HttpResponse
from django.views.generic import View

from carservice.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    carmodel = carmodel.objects.all()
    def get(self, request, *args, **kwargs):
        data = {'carmodel':carmodel}
        pdf = render_to_pdf('car/carmodel_detail.html', data)
        return HttpResponse(pdf, content_type='application/pdf')