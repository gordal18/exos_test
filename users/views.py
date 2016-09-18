from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import User
from .forms import UserForm
from .utils import is_eligible, get_bizzfuzz

class UserList(ListView):
    model = User
    template_name = 'users/list.html'

class UserDetail(DetailView):
    model = User
    template_name = 'users/detail.html'

class UserCreate(CreateView):
    model = User
    template_name = 'users/create.html'
    form_class = UserForm
    success_url = reverse_lazy('user_list')

class UserUpdate(UpdateView):
    model = User
    template_name = 'users/update.html'
    form_class = UserForm
    success_url = reverse_lazy('user_list')

class UserDelete(DeleteView):
	model = User
	success_url = reverse_lazy('user_list')

def download(request):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    # response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str("Name"),
        smart_str("Email"),
        smart_str("Birthday"),
        smart_str("Eligible"),
        smart_str("Random Number"),
        smart_str("BizzFuzz"),
    ])
    users = User.objects.all()
    for user in users:
    	eligible = 'allowed' if is_eligible(user.birthday) else 'blocked'
        writer.writerow([
            user.get_full_name(),
            user.email,
            user.birthday,
            eligible,
            user.random_number,
            get_bizzfuzz(user.random_number),
        ])
    return response