from cms.plugin_pool import plugin_pool
from cms.plugins.link.cms_plugins import LinkPlugin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from models import ButtonLink
from forms import ButtonLinkForm

class ButtonLinkPlugin(LinkPlugin):
    module = 'Bootstrap'
    model = ButtonLink
    form = ButtonLinkForm
    name = _("ButtonLink")
    render_template = "cmsplugin_bootstrap/link.html"

    class Media:
        css = {
            "all": (settings.STATIC_URL + "libs/bootstrap/css/bootstrap.min.css",)
        }

    def render(self, context, instance, placeholder):
        ctx = context
        ctx['button_class'] = instance.button_class
        ctx['button_size'] = instance.button_size
        ctx['disabled'] = instance.disabled
        ctx['block_level'] = instance.block_level
        return super(ButtonLinkPlugin, self).render(ctx, instance, placeholder)
plugin_pool.register_plugin(ButtonLinkPlugin)