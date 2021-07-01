from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import cas
# Create your views here.
def Sante(request):

    cases=cas.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(cases, 9)
    try:
        cass= paginator.page(page)
    except PageNotAnInteger:
        cass = paginator.page(1)
    except EmptyPage:
        cass = paginator.page(paginator.num_pages)
    return render(request, "Sante.html", {'cass':cass})

def education(request):
    cases = cas.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cases, 9)
    try:
        cass = paginator.page(page)
    except PageNotAnInteger:
        cass = paginator.page(1)
    except EmptyPage:
        cass = paginator.page(paginator.num_pages)
    return render(request, "education.html", {'cass': cass})

def autres(request):
    cases = cas.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cases, 9)
    try:
        cass = paginator.page(page)
    except PageNotAnInteger:
        cass = paginator.page(1)
    except EmptyPage:
        cass = paginator.page(paginator.num_pages)

    return render(request, "autres.html", {'cass': cass})

def details(request, id):
    case = get_object_or_404(cas, id=id)
    return render(request, "details.html", {'case': case})

def Accueil(request):
    cass = cas.objects.all()

    #converting the objects set to a list
    cases = list(cass)

    #sorting the list by title in a descendent order(from biggest to smallest)
    cases.sort(key=lambda x: x.titre, reverse=True)

    page = request.GET.get('page', 1)

    #making a paginator of 7 elements
    paginator = Paginator(cases, 7)
    try:
        cass = paginator.page(page)
    except PageNotAnInteger:
        cass = paginator.page(1)
    except EmptyPage:
        cass = paginator.page(paginator.num_pages)
    return render(request, "Accueil.html", {'cass': cass})

def data(request):
    data = request.POST.get('montant')
    context = {{data}}
    print(data)
    return render(request, 'details.html', context)

def about(request):
    return render(request, "Web_About_Us_Y.html")

def association(request):
    return render(request, "Association.html")

