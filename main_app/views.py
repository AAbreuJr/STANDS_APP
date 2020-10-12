from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stand

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def stands_index(request):
    stands = Stand.objects.filter()
    return render(request, 'stands/index.html', {'stands': stands})

class StandCreate(CreateView):
    model = Stand
    fields = '__all__'


def stands_detail(request, stand_id):
    stand = Stand.objects.get(id=stand_id)
    return render(request, 'stands/detail.html', {
        'stand': stand
    })

class StandUpdate(UpdateView):
    model = Stand
    fields = '__all__'

class StandDelete(DeleteView):
    model = Stand
    success_url = '/stands/'
