# -*- coding: utf-8 -*-
# Django settings for GeoNode project.
from urllib import urlencode
import os
import geonode

_ = lambda x: x

DEBUG = True
SITENAME = "Open Data for the Horn"
SITEURL = "http://localhost:8000/"
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#added this to have the GeoNode root setting here
GEONODE_ROOT = os.path.dirname(geonode.__file__)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT,"..","..","..","development.db")
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Not used with sqlite3.
DATABASE_PORT = ''             # Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Español'),
    ('it', 'Italiano'),
    ('fr', 'Français'),
)

SITE_ID = 1

# Setting a custom test runner to avoid running the tests for some problematic 3rd party apps
TEST_RUNNER='django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
      '--verbosity=2',
      '--cover-erase',
      '--nocapture',
      '--with-coverage',
      '--cover-package=geonode',
      '--cover-inclusive',
      '--cover-tests',
      '--detailed-errors',
      '--with-xunit',

# This is very beautiful/usable but requires: pip install rudolf
#      '--with-color',

# The settings below are useful while debugging test failures or errors

#      '--failed',
#      '--pdb-failures',
#      '--stop',
#      '--pdb',
      ]

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")
#also changed this to enable the new debian installers
MEDIA_ROOT = '/var/www/geonode/uploaded'


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = "/site_media/media/"
#also changed this to enable the new change to media_root
MEDIA_URL = '/uploaded/'

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
#STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")
STATIC_ROOT = '/var/www/geonode/static/'
# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
#STATIC_URL = "/media/"
STATIC_URL = '/static/'

# Additional directories which hold static files
#STATICFILES_DIRS = [
#    os.path.join(PROJECT_ROOT, "media"),
#]
#added this because of the change in the location of the media due to the debian installs
STATICFILES_DIRS = [
'/etc/geonode/media',
os.path.join(PROJECT_ROOT,"media"),
os.path.join(GEONODE_ROOT,"media"),
]

GEONODE_UPLOAD_PATH = os.path.join(STATIC_URL, "upload/")

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = os.path.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'myv-y4#7j-d*p-__@j#*3z@!y24fz8%^z2v6atuy4bo9vqr1_a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "geonode.maps.context_processors.resource_urls",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

# This isn't required for running the geonode site, but it when running sites that inherit the geonode.settings module.
#LOCALE_PATHS = (
#    os.path.join(PROJECT_ROOT, "locale"),
#    os.path.join(PROJECT_ROOT, "maps", "locale"),
#)
LOCALE_PATHS = (
     os.path.join(PROJECT_ROOT,"locale"),
     os.path.join(GEONODE_ROOT,"locale"),
     os.path.join(GEONODE_ROOT,'maps','locale'),
)
#also changed the root_urlconf
ROOT_URLCONF = 'horndata.urls'

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
#TEMPLATE_DIRS = (
#    os.path.join(PROJECT_ROOT,"templates"),    
#)
TEMPLATE_DIRS = (
'/etc/geonode/templates',
os.path.join(PROJECT_ROOT,'templates'),
os.path.join(GEONODE_ROOT,'templates'),
)

# The FULLY QUALIFIED url to the GeoServer instance for this GeoNode.
GEOSERVER_BASE_URL = "http://localhost:8001/geoserver/"

# The username and password for a user that can add and edit layer details on GeoServer
#GEOSERVER_CREDENTIALS = "geoserver_admin", GEOSERVER_TOKEN
#commented what was above inorder to use the SECRET KEY
GEOSERVER_CREDENTIALS = "geoserver_admin", SECRET_KEY
# The FULLY QUALIFIED url to the GeoNetwork instance for this GeoNode
GEONETWORK_BASE_URL = "http://localhost:8001/geonetwork/"

# The username and password for a user with write access to GeoNetwork
GEONETWORK_CREDENTIALS = "admin", "admin"

AUTHENTICATION_BACKENDS = ('geonode.core.auth.GranularBackend',)

GOOGLE_API_KEY = "ABQIAAAAkofooZxTfcCv9Wi3zzGTVxTnme5EwnLVtEDGnh-lFVzRJhbdQhQgAhB1eT_2muZtc0dl-ZSWrtzmrw"
LOGIN_REDIRECT_URL = "/"

DEFAULT_LAYERS_OWNER='admin'

# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (-84.7, 12.8)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 7

DEFAULT_LAYER_SOURCE = {
    "ptype":"gxp_wmscsource",
    "url":"/geoserver/wms",
    "restUrl": "/gs/rest"
}

MAP_BASELAYERS = [{
    "source": {"ptype": "gx_olsource"},
    "type":"OpenLayers.Layer",
    "args":["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  },{
    "source": { "ptype":"gx_olsource"},
    "type":"OpenLayers.Layer.OSM",
    "args":["OpenStreetMap"],
    "visibility": True,
    "fixed": True,
    "group":"background"
  },{
    "source": {"ptype":"gx_olsource"},
    "type":"OpenLayers.Layer.WMS",
    "group":"background",
    "visibility": False,
    "fixed": True,
    "args":[
      "bluemarble",
      "http://maps.opengeo.org/geowebcache/service/wms",
      {
        "layers":["bluemarble"],
        "format":"image/png",
        "tiled": True,
        "tilesOrigin":[-20037508.34,-20037508.34]
      },
      {"buffer":0}
    ]

}]

# NAVBAR expects a dict of dicts or a path to an ini file
NAVBAR = \
{'maps': {'id': '%sLink',
               'item_class': '',
               'link_class': '',
               'text': 'Maps',
               'url': 'geonode.maps.views.maps'},
 'data': {'id': '%sLink',
          'item_class': '',
          'link_class': '',
          'text': 'Data',
          'url': "geonode.maps.views.browse_data"},
#  'index': {'id': '%sLink',
#            'item_class': '',
#            'link_class': '',
#            'text': 'Featured Map',
#            'url': 'geonode.views.index'},
 'master': {'id': '%sLink',
            'item_class': '',
            'link_class': '',
            'text': 'This page has no tab for this navigation'},
 'meta': {'active_class': 'here',
          'default_id': '%sLink',
          'default_item_class': '',
          'default_link_class': '',
          'end_class': 'last',
          'id': '%sLink',
          'item_class': '',
          'link_class': '',
          'visible': 'data\nmaps'}}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'staticfiles',
    'django_extensions',
    'registration',
    'profiles',
    'avatar',
    'geonode.core',
    'geonode.maps',
    'geonode.proxy',
    'geonode'
)

def get_user_url(u):
    from django.contrib.sites.models import Site
    s = Site.objects.get_current()
    return "http://" + s.domain + "/profiles/" + u.username


ABSOLUTE_URL_OVERRIDES = {
    'auth.user': get_user_url
}

AUTH_PROFILE_MODULE = 'maps.Contact'
REGISTRATION_OPEN = False

SERVE_MEDIA = DEBUG;

#GEONODE_CLIENT_LOCATION = "http://localhost:8001/geonode-client/"
GEONODE_CLIENT_LOCATION = "/media/static/"

#Import uploaded shapefiles into a database such as PostGIS?
DB_DATASTORE=False

#Database datastore connection settings
DB_DATASTORE_NAME = ''
DB_DATASTORE_USER = ''
DB_DATASTORE_PASSWORD = ''
DB_DATASTORE_HOST = ''
DB_DATASTORE_PORT = ''
DB_DATASTORE_TYPE=''

try:
    from local_settings import *
except ImportError:
    pass

