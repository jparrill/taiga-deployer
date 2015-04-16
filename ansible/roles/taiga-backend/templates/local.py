from .common import *

MEDIA_URL = "{{ scheme }}://{{ host_fqdn }}/media/"
STATIC_URL = "{{ scheme }}://{{ host_fqdn }}/static/"
ADMIN_MEDIA_PREFIX = "{{ scheme }}://{{ host_fqdn }}/static/admin/"
SITES["front"]["scheme"] = "{{ scheme }}"
SITES["front"]["domain"] = "{{ host_fqdn }}"

SECRET_KEY = "taiga_localdomain"

DEBUG = True
TEMPLATE_DEBUG = False
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "no-reply@{{ host_fqdn }}"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Uncomment and populate with proper connection parameters
# for enable email sending.
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_USE_TLS = False
#EMAIL_HOST = "localhost"
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_PORT = 25

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
