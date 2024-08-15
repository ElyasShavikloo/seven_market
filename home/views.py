from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import ContactUs
from .forms import ContactUsForm

# def home(request):
#     return render(request, 'home/index.html', {})


class Home(TemplateView):
    template_name = 'home/index.html'


class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUs.objects.create(**form_data)

        return super().form_valid(form)