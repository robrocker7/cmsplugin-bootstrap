from cms.plugins.link.forms import LinkForm

from widgets import ButtonClassSelect
from models import ButtonLink

class ButtonLinkForm(LinkForm):

    class Meta:
        widgets = {
            'button_class': ButtonClassSelect(choices=ButtonLink.BUTTON_CLASS_CHOICES)
        }