from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin, Page

"""
# Since Models cant be subclassed I will copy and paste the plugin model
from cms.plugins.link.models import Link
class ButtonLink(Link):
    button_class = models.CharField(_("button class"), blank=True, max_length=100, choices=((
        ("", _("default")),
        ("primary", _("primary")),
        ("info", _("info")),
        ("success", _("success")),
        ("warning", _("warning")),
        ("danger", _("danger")),
        ("inverse", _("inverse")),
        ("link", _("link")),
    )))
    button_size = models.CharField(_("button size"), blank=True, max_length=100, choices=((
        ("", _("default")),
        ("large", _("large")),
        ("small", _("small")),
        ("mini", _("mini")),
    )))
"""

class ButtonLink(CMSPlugin):
    """
    A link to an other page or to an external website
    """
    BUTTON_CLASS_CHOICES = (
        ("", _("default")),
        ("primary", _("primary")),
        ("info", _("info")),
        ("success", _("success")),
        ("warning", _("warning")),
        ("danger", _("danger")),
        ("inverse", _("inverse")),
        ("link", _("link")),
    )
    name = models.CharField(_("name"), max_length=256)
    url = models.URLField(_("link"), blank=True, null=True)
    page_link = models.ForeignKey(Page, verbose_name=_("page"), blank=True, null=True, help_text=_("A link to a page has priority over a text link."))
    mailto = models.EmailField(_("mailto"), blank=True, null=True, help_text=_("An email adress has priority over a text link."))
    target = models.CharField(_("target"), blank=True, max_length=100, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )))
    button_class = models.CharField(_("button class"), max_length=100, choices=
            BUTTON_CLASS_CHOICES)
    button_size = models.CharField(_("button size"), max_length=100, choices=((
        ("", _("default")),
        ("large", _("large")),
        ("small", _("small")),
        ("mini", _("mini")),
    )))
    block_level = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    search_fields = ('name',)