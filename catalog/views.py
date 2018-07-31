from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q

from django.views.generic import ListView, View, DetailView
from django.views.generic.edit import DeleteView, FormView, UpdateView

from . import models
from . import forms


class MainPageView(ListView):
    context_object_name = 'fotos'
    template_name = 'catalog/main.html'

    def get_queryset(self):
        fotos = models.Foto.objects.all()
        return fotos


class DetailPageView(DetailView):
    context_object_name = 'foto'
    template_name = 'catalog/detail.html'

    def get_object(self, queryset=models.Foto.objects.all()):
        foto = super(DetailPageView, self).get_object()
        return foto


class AddPageView(FormView):
    form_class = forms.AddFotoForm
    success_url = reverse_lazy('main')
    template_name = 'catalog/add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.clean_name()
        form.clean_text()
        self.object.save()
        return super(AddPageView, self).form_valid(form)


class UpdatePageView(UpdateView):
    fields = ['name', 'image', 'text']
    context_object_name = 'foto'
    template_name = 'catalog/update.html'
    success_url = reverse_lazy('edit_foto')

    def get_success_url(self, **kwargs):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class SearchPageView(View):
    template_name = 'catalog/search.html'

    def get(self, request):
        query = request.GET.get('query')

        if query:
            qset = (
                    Q(name__startswith=query) |
                    Q(text__startswith=query) |
                    Q(date_added__startswith=query)
            )
            posts = models.Foto.objects.filter(qset)

        else:
            posts = []

        return render(request, self.template_name, {'query': query, 'posts': posts})


class DeletePageView(DeleteView):
    context_object_name = 'foto'
    template_name = 'catalog/delete.html'
    success_url = reverse_lazy('main')

    def get_template_names(self):
        return self.template_name
