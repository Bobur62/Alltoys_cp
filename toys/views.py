from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from toys.models import Toy


# Base Views
# 1. View
# 2. TemplateView
# 3. RedirectView
# ***************************************************************************************************************

# def dashboard(request):
#     return render(request, "toys/dashboard.html", context={"welcome_text" : "welcome alltoys page"})


class DashboardView(View):
    def get(self, request):
        return render(request, "toys/dashboard.html", context={"welcome_text": "welcome alltoys page"})

    # ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    # def post(self, request):
    #
    #     return render(request, "toys/dashboard.html", context={"welcome_text": "welcome alltoys page"})


# *************************************************************************************************************

# def get_toys(request):
#     toys = Toy.objects.all()
#     toys = toys.filter(created_at__year=timezone.now().year)
#     # toys = toys.exclude(name__startswith="Car")   #filter qilingan datalardan keraksizlarini ajratib tashlaydi
#     toys = toys.select_related("user")            #qayta qayta vapros qilishni oldini oladi va bazadan malumotlarni barchasini olib cashlab oladi bu selcted_relted ONEANDoNE VA fOREaNDkEY LAR UN ISHLATAMIZ
#     toys = toys.prefetch_related("tags")            #alohida vapros jonatib malumotlani cashlab oladi faqat ManyToMany boglanishlarga ishlatamiz
#     return render(request, "toys/toys.html", context={"toys": toys})


# class GetToysView(TemplateView):
#     template_name = "toys/toys.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         toys = Toy.objects.all()
#         toys = toys.select_related("user")
#         toys = toys.prefetch_related("tags")
#         context['toys'] = toys
#         return context


# Generic display views
# 2. ListView

class ToysListView(ListView):
    model = Toy
    template_name = "toys/toys.html"

    def get_queryset(self):
        toys = Toy.objects.filter(created_at__year=timezone.now().year)
        toys = toys.select_related("user")
        toys = toys.prefetch_related("tags")

        return toys


# **************************************************************************************************************


# def get_toy_detail(request, **kwargs):
#     try:
#         toy = Toy.objects.get(pk=kwargs.get("id"))
#     except Toy.DoesNotExist:
#         return redirect("toys:toys")
#     return render(request, "toys/toy_detail.html", context={"toy": toy})

# Generic display views
# 1. DetailView


class ToyDetailView(DetailView):
    model = Toy
    template_name = "toys/toy_detail.html"

# *************************************************************************************************************
# Generic display views
# 3. CreateView


class ToyCreateView(CreateView):
    model = Toy
    # template_name = 'toy_form.html'
    fields = ['name', 'description', 'price']
    success_url = "/toys/"





# *****************************
# Generic display views       *
# 1. DetailView               *
# 2. ListView                 *
# 3. CreateView               *
# *****************************
