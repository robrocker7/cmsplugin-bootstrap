===============
cmsplugin-bootstrap
===============

Plugins that provide Twitter Bootstrap styles to HTML elements

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

add the following sekizai tags to your base html in their proper places it's recommendend putting the javascript tag in your footer above the </body>

    {% render_block "css" %}
    {% render_block "js" %}

There is a copy of the latest version of Twitter Bootstrap packaged. You can use your own customized version of Twitter Bootstrap or use the packaged version by adding the following to your base::

    {% addtoblock "js" %}  
        <script type="text/javascript" src="{{ STATIC_URL }}libs/bootstrap/js/bootstrap.min.js"></script>
    {% endaddtoblock "js" %}

    {% addtoblock "css" %}
        <link href="{{ STATIC_URL }}libs/bootstrap/css/bootstrap.min.css" rel="stylesheet">
        <link href="{{ STATIC_URL }}libs/bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
    {% endaddtoblock "css" %}
