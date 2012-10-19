from django.forms.widgets import Select
from django.utils.safestring import mark_safe

class ButtonClassSelect(Select):

    def render(self, name, value, attrs=None, choices=()):
        output = super(ButtonClassSelect, self).render(name=name,
            value=value, attrs=attrs, choices=choices)

        color_swatches = '<div style="display:block;">'
        color_swatches = color_swatches + '<div class="btn btn-mini" style="margin-right: 8px;">Default</div>'
        color_swatches = color_swatches + '<div class="btn btn-primary btn-mini" style="margin-right: 8px;">Primary</div>'
        color_swatches = color_swatches + '<div class="btn btn-info btn-mini" style="margin-right: 8px;">Info</div>'
        color_swatches = color_swatches + '<div class="btn btn-success btn-mini" style="margin-right: 8px;">Success</div>'
        color_swatches = color_swatches + '<div class="btn btn-warning btn-mini" style="margin-right: 8px;">Warning</div>'
        color_swatches = color_swatches + '<div class="btn btn-danger btn-mini" style="margin-right: 8px;">Danger</div>'
        color_swatches = color_swatches + '<div class="btn btn-inverse btn-mini" style="margin-right: 8px;">Inverse</div>'
        color_swatches = color_swatches + '</div>'

        return mark_safe(output + color_swatches)