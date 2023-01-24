from django.views import generic
from django.shortcuts import redirect, get_object_or_404, resolve_url
from django.http import JsonResponse
from django.contrib import messages

from taggit.models import Tag

from geofazendas.artigos.models import Artigo

from geofazendas.sindicatos.mixins import SindicatoRequiredMixin
from geofazendas.sindicatos.forms import ArtigoForm


class ArtigoListView(SindicatoRequiredMixin, generic.ListView):

    template_name = 'sindicatos/artigo_list.html'
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.artigos.all()

    def artigos_populares(self):
        return Artigo.objects.order_by('-views')

    def artigos_recentes(self):
        return Artigo.objects.order_by('-data_publicacao')

    def tags(self):
        return Tag.objects.all()


class ArtigoCreateView(SindicatoRequiredMixin, generic.CreateView):

    template_name = 'sindicatos/artigo_form.html'
    form_class = ArtigoForm

    def form_valid(self, form):
        article = form.save(commit=False)
        article.criado_por = self.request.user
        article.save()
        form.save_m2m()
        messages.success(self.request, 'Publicação criada com sucesso!')
        return redirect('sindicatos:artigo_list')


class ArtigoUpdateView(SindicatoRequiredMixin, generic.UpdateView):

    template_name = 'sindicatos/artigo_form.html'
    form_class = ArtigoForm

    def get_queryset(self):
        return self.request.user.artigos.all()

    def get_success_url(self):
        messages.success(self.request, 'Publicação atualizada com suecsso!')
        return resolve_url('sindicatos:artigo_list')


class ArtigoDeleteView(SindicatoRequiredMixin, generic.View):

    def post(self, request, pk):
        article = get_object_or_404(self.request.user.artigos.all(), pk=pk)
        article.delete()
        return JsonResponse({'success': True})


artigo_list = ArtigoListView.as_view()
artigo_create = ArtigoCreateView.as_view()
artigo_update = ArtigoUpdateView.as_view()
artigo_delete = ArtigoDeleteView.as_view()
