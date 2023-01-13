from django.views import generic

from geofazendas.mapas.layers_list import lyr_list


class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['layers'] = lyr_list
        return context


index = IndexView.as_view()
