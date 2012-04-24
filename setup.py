from setuptools import setup

version = '0.4.6dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('TODO.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'python-dateutil >= 1.5,< 2.0',  # Needed because of celery
    'celery',
    'django-celery',
    'django-kombu',
    'django-extensions',
    'django-nose',
    'lizard-map >= 3.24',
    'lizard-ui >= 3.0',
    'pkginfo',
    'networkx >= 1.6',
    ],

tests_require = [
    ]

setup(name='lizard-riool',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='TODO',
      author_email='TODO@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['lizard_riool'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
        'console_scripts': [],
        'lizard_map.adapter_class': [
          '.rib = lizard_riool.layers:RibAdapter',
          '.rmb = lizard_riool.layers:RmbAdapter',
          'lizard_riool_lost_capacity = lizard_riool.layers:RmbLostStorageAdapter',
        ]
      },
)
