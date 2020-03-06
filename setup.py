from setuptools import setup
import os

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                            "freecad", "gdt", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.gdt',
      version=str(__version__),
      packages=['freecad',
                'freecad.gdt'],
      maintainer="looooo",
      maintainer_email="sppedflyer@gmail.com",
      description="freecad extension for geometric tolerances",
      install_requires=[],
      include_package_data=True
)
