from django.template import Library

register = Library()


@register.simple_tag
def get_legend(name):
    legend = 'geofazendas/wms?REQUEST=GetLegendGraphic&'
    legend += 'VERSION=1.1.0&'
    legend += 'FORMAT=image/png&'
    legend += 'WIDTH=18&'
    legend += 'HEIGHT=18&'
    legend += f'LAYER=geofazendas:mapas_{name}&'
    legend += 'LEGEND_OPTIONS=fontName:Arial;fontAntiAliasing:true;dpi=200'

    return legend
