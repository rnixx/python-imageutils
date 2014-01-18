Installation
------------

You can install ``ImageUtils`` with ``pip``::

    pip install PIL (or pip install Pillow)
    pip install ImageUtils

or you can add ``ImagUtils`` as dependency of another package in it's 
``setup.py``::

    setup(
        ...
        install_requires=['ImageUtils[pillow]']
        ...
    )

**Note**: Defining extra requirements in square brackets also fetches
dependencies. Possible extra requirement names are ``pil`` and ``pillow``.
