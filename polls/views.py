from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from pytils.translit import slugify

from .models import Content
from .forms import ContentForm


class ContentView(ListView):
    model = Content
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super().get_context_data(**kwargs)
        content['title'] = 'Mediaportal'
        content['greeting'] = 'Welcome %user_name!'
        return content


class SingleContentView(DetailView):
    model = Content
    template_name = 'single.html'
    fields = '__all__'


class CreateContentView(CreateView):
    model = Content
    template_name = 'add.html'
    form_class = ContentForm
    success_url = reverse_lazy('polls')


def main(request):
    context = {
        'title': 'Mediaportal',
        'greeting': 'Welcome %user_name!'
    }
    return render(request, 'index.html', context)
