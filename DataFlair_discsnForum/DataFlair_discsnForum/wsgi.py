
import os
# import views from '../Discussion_Forum'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataFlair_discsnForum.settings')

application = get_wsgi_application()
