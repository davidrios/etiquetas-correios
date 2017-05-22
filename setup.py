from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='etiquetas-correios',
    version='0.0.1',
    description='Um gerador de etiquetas simples para postagem nos Correios.',
    long_description=long_description,
    url='https://github.com/davidrios/etiquetas-correios',
    author='David Rios',
    author_email='david.rios.gomes@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'attrs'
    ],
    extras_require={
        'sigep': ['zeep'],
        'gerar-html': ['jinja2'],
    },
    package_data={
        'etiquetas_correios': ['templates/**'],
    },
    entry_points={
        'console_scripts': [
            'etiquetas-correios=etiquetas_correios.cli:main',
        ],
    },
)
