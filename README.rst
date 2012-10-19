===============
cmsplugin-bootstrap
===============

Plugins that provide Twitter Bootstrap styles to HTML elements. This library uses the latest version of Twitter Bootstrap: http://twitter.github.com/bootstrap/

Dependencies
------------

* Django >= 1.3
* django-cms >= 2.2
* django-sekizai >= 0.4.2
* South >= 0.7.6

Installation
------------

add the bootstrap plugins to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'cmsplugin_bootstrap_link',
        ...
    )

and then run ``migrate``

add the following sekizai tags to your base html in their proper places it's recommendend putting the javascript tag in your footer above the </body>::

    {% render_block "css" %}
    {% render_block "js" %}

Since you're using this plugin it's assumed you already are using bootstrap and have it included into your template. If not here is the basic structure for the media includes::

    {% addtoblock "js" %}  
        <script type="text/javascript" src="{{ STATIC_URL }}pathtobootstrap/js/bootstrap.min.js"></script>
    {% endaddtoblock "js" %}

    {% addtoblock "css" %}
        <link href="{{ STATIC_URL }}pathtobootstrap/css/bootstrap.min.css" rel="stylesheet">
        <link href="{{ STATIC_URL }}pathtobootstrap/css/bootstrap-responsive.css" rel="stylesheet">
    {% endaddtoblock "css" %}
