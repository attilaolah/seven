from setuptools import find_packages, setup


setup(
    # Package information:
    name='seven',
    version='1.0.0',
    license='PSF License',
    url='http://github.com/aatiis/seven',
    description='Python 2.5 compatibility wrapper for Python 2.7 code.',
    long_description=\
        open('README.rst').read() + '\n\n' + \
        open('CHANGES.rst').read(),
    # Author information:
    author='Attila Olah',
    author_email='attilaolah@gmail.com',
    # Package settings:
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=(),
    include_package_data=True,
    zip_safe=True,
    tests_require=(
        'zope.testing',
    ),
    extras_require={
        'tests': (
            'zope.testing',
        ),
    },
    test_suite = "seven.tests.test_suite",
    # Classifiers:
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
