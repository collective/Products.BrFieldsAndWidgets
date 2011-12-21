from setuptools import setup, find_packages
import os

version = open(os.path.join("Products", "BrFieldsAndWidgets", "version.txt")).read().strip()

setup(name='Products.BrFieldsAndWidgets',
      version=version,
      description="Brazilian fields and widgets to be used with Plone and Archetypes",
      long_description=open(os.path.join("Products", "BrFieldsAndWidgets", "README.txt")).read().decode('UTF8').encode('ASCII', 'replace') + '\n' +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone archetypes widget BrFieldsAndWidgets brazil',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='http://plone.org/products/Products.BrFieldsAndWidgets',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.brasil.vocab>=0.8',
      ],
      extras_require={
        'test': ['plone.app.testing'],
        },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
