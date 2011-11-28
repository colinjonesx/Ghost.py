"""
Ghost.py
--------

Webkit based webclient.

"""
from setuptools import setup, find_packages


setup(
    name='Flask-Dashed',
    version='0.1a',
    url='https://github.com/jean-philippe/Ghost.py',
    license='mit',
    author='Jean-Philippe Serafin',
    author_email='serafinjp@gmail.com',
    description='Webkit based webclient.',
    long_description=__doc__,
    data_files=[('ghost', ['README.rst', 'ghost/utils.js'])],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
