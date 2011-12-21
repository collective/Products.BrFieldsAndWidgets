from setuptools import setup, find_packages
import os

version = open(os.path.join("Products", "BrFieldsAndWidgets", 
                            "version.txt")).read().strip()

setup(name='Products.BrFieldsAndWidgets',
      version=version,
      description="Brazilian fields and widgets to be used with Plone and Archetypes",
      long_description=open(os.path.join("README.rst")).read() + '\n' +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Natural Language :: Portuguese (Brazilian)",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone archetypes widget BrFieldsAndWidgets brazil brasil',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://github.com/collective/Products.BrFieldsAndWidgets',
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
