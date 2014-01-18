import os
from setuptools import setup

version = '0.3.8'
shortdesc = 'Various utilities for working with images.'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='ImageUtils',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    author='Jeremy Cantrell',
    author_email='jmcantrell@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    packages=[
        'imageutils',
    ],
    extras_require = dict(
        pil=['PIL'],
        pillow=['Pillow'],
    ),
)
