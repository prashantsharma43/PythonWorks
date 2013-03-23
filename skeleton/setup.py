try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Prashant',
    'url': 'www.google.com/code/887821',
    'download_url': 'Where to download it.',
    'author_email': 'prashantsharma43@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'PyPy My Way'
}

setup(**config)
