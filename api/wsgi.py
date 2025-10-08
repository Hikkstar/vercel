from django.core.wsgi import get_wsgi_application
from mangum import Mangum  # これを使ってサーバレス化

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = get_wsgi_application()
handler = Mangum(application)
