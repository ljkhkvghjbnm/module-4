from django.shortcuts import render, reverse, redirect

from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
#     return HttpResponse("""
#         <h1>Все супер</h1>
#         <a class="navbar-brand" href="lesson_4/">
#             Домашняя работа 4 занятия
#         </a>
#     """)
#
# def lesson(request):
#     return HttpResponse("""
#         <h1> Вот и домашка </h1>
#     """)
    advertisement=Advertisement.objects.all()
    context={'advertisements':advertisement}

    return render(request, 'index.html',context=context)

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisement_post(request):
    if request.method=='POST':
        form=AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement= Advertisement(**form.cleaned_data)
            advertisement.user=request.user
            advertisement.save()
            url=reverse('main-page')
            return redirect(url)
    else:
        form=AdvertisementForm()
    context={'form':form}
    return render(request,"advertisement-post.html",context=context)
