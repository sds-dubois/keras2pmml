# coding=utf-8
import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.rst') as readme_file:
    long_description = readme_file.read()

setup(
    name='keras2pmml',
    version='0.1.1',
    packages=['keras2pmml'],
    include_package_data=True,
    license='MIT',
    description='Simple exporter of Keras models into PMML',
    long_description=long_description,
    url='https://github.com/sds-dubois/keras2pmml',
    author='Václav Čadek, Sebastien Dubois',
    author_email='vaclavcadek@gmail.com',
    install_requires=[
        'numpy>=1.6.1',
        'SciPy>= 0.9',
        'theano>=0.8.2',
        'keras>=1.0.6',
        'scikit-learn>=0.17.1'
    ],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
