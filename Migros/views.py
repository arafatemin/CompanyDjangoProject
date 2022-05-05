from django.shortcuts import render
from .models import *
from .forms import *
from django.views import View


def index(request):
    context = {
        "urunler": Urunler.objects.all()[:2],
        "urunListeleri": Urunler.objects.all()[:7],
        'calisanlar': Employee.objects.all()[:3],

    }
    return render(request, 'index.html', context)


def urunler(request):
    context = {
        "urunler": Urunler.objects.all(),
        "employees": Employee.objects.all(),

    }
    return render(request, 'urunler.html', context)

# def urundetail(request, id):
#     context = {
#         "urun": Urunler.objects.get(id=id)
#     }
#     return render(request, 'urun_detail.html', context)


def urundetail(request, slug):
    context = {
        "urun": Urunler.objects.get(slug=slug)
    }
    return render(request, 'urun_detail.html', context)


def urun_listesi(request):
    keyword = request.GET.get("keyword")
    if keyword:
        urunler = Urunler.objects.filter(name__contains=keyword)
        return render(request, "urun-listesi.html", {'urunler': urunler})
    context = {
        "urunler": Urunler.objects.all()
    }
    return render(request, 'urun-listesi.html', context)




def calisanlar(request):
    context = {
        "calisanlar": Employee.objects.all(),
    }
    return render(request, 'calisanlar.html', context)

def calisan_detail(request, slug):
    context = {
        "calisan": Employee.objects.get(slug=slug)
    }
    return render(request, 'calisan-detail.html', context)





def aboutus(request):
    context = {
        "aboutus": AboutUs.objects.all()[:1]
    }
    return render(request, 'aboutUs.html', context)



class ContactUs(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': ContactForm()
        }
        return render(request, 'contactus.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            c_form = form.save(commit=False)
            c_form.save()
            return render(request, 'contactus.html', context={"form": ContactForm()})





