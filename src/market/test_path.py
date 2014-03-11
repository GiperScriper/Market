import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

print BASE_DIR

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
print MEDIA_ROOT