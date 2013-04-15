from setuptools import setup, find_packages

setup(
    name='my-django-survey',
    version='0.0.4',
    description='A simple extensible survey application for django sites',
    author='Yann Malet, Doug Napoleone',
    author_email='scanner@apricot.com',
    url='',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
