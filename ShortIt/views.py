from .forms import url_shortenerForm
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
import random, string
from .models import urlEntry


def url_home(request):
    form = url_shortenerForm()

    if request.method == 'POST':
        form = url_shortenerForm(request.POST)
        original_url = request.POST.get('url')

        if form.is_valid():
            url = 'http://127.0.0.1:8000/'
            slug = ''.join(random.choices(string.ascii_letters, k=4))
            final_url = slug
            finish = urlEntry.objects.create(url=original_url, shortened_url=final_url)
            final_shortened_url = finish.shortened_url
            final_shown_url = url + final_shortened_url

        return render(request, template_name='shortit.html', context={'final_shortened_url': final_shortened_url, 'final_shown_url': final_shown_url})

    context = {'form': form}
    return render(request, template_name='base.html', context=context)


def final_routing(request, finish_id):
    if request.method == 'GET':
        routing_url = urlEntry.objects.get(shortened_url=finish_id)
        return HttpResponseRedirect(routing_url.url)

