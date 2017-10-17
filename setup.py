from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='wsgierror',
      version=version,
      description="WSGI error handling the PerFact way.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='PerFact',
      author_email='',
      url='',
      license='GPL 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
