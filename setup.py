import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-bootstrap",
    version = "0.1",
    url = 'http://github.com/robrocker7/cmsplugin-bootstrap',
    license = 'BSD',
    description = "django-cms plugins to integrate twitter bootstrap",
    long_description = read('README.rst'),
    author = 'Robert Johnson',
    author_email = 'robrocker7@gmail.com',
    packages = find_packages(),
    #package_dir = {'':'src'},
    classifiers = [
        'Development Status :: 1 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.3",
        "django-cms >= 2.2",
        "django-sekizai >= 0.4.2",
        "South >= 0.7.6"
    ],
    include_package_data=True,
    zip_safe = False,
)