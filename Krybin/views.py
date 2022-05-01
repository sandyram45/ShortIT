from django.shortcuts import render, redirect
from .forms import boxTextForm
import string, random
from .models import boxText
from django.http import HttpResponseRedirect


def home(request):

    form = boxTextForm()
    if request.method == 'POST':
        form = boxTextForm(request.POST)
        filledText = request.POST.get('text')

        if form.is_valid():

            slug = ''.join(random.choices(string.ascii_letters, k=7))
            finish = boxText.objects.create(text=filledText, copy_url=slug)
            return HttpResponseRedirect(finish.copy_url)

    context = {'form': form}
    return render(request, template_name='krybin.html', context=context)


def final_view(request, slugs):
    form = boxTextForm()
    if request.method == 'GET':
        finished_view = boxText.objects.get(copy_url=slugs)
        form = boxTextForm(instance=finished_view)

    context = {'form': form}
    return render(request, template_name='page.html', context=context)
