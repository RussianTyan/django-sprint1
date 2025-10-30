import os

INSTALLED_APPS = [
    # ... другие приложения Django
    'pages',
    'blog',
    'django.contrib.staticfiles',
]

# указать папку для проектных шаблонов
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates')]

# статика
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'html'),
]
