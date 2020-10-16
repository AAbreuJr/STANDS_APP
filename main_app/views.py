from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stand

# Create your views here.
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/about/')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def landing(request):
    return render(request, 'landing.html')

@login_required
def stands_index(request):
    stands = Stand.objects.filter(user = request.user)
    return render(request, 'stands/index.html', {'stands': stands})


class StandCreate(LoginRequiredMixin, CreateView):
    model = Stand
    fields = ['name','company', 'type', 'strings', 'make', 'cost']

    def form_valid(self, form):
        # Assign the logged in user
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)

@login_required
def stands_detail(request, stand_id):
    stand = Stand.objects.get(id=stand_id)
    return render(request, 'stands/detail.html', {
        'stand': stand
    })

class StandUpdate(LoginRequiredMixin, UpdateView):
    model = Stand
    fields = ['name','company', 'type', 'strings', 'make', 'cost']

class StandDelete(LoginRequiredMixin, DeleteView):
    model = Stand
    success_url = '/stands/'

def about(request):
    return render(request, 'about.html')