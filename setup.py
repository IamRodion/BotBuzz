from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='BotBuzz',
    version='0.1.0',
    packages=find_packages(), #['BotBuzz']
    install_requires=[
        'requests==2.32.3',
    ],
    author='Rodion',
    author_email='pablotapias98@gmail.com',
    description='Una librería para interactuar de forma simple con la API de Telegram',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/IamRodion/BotBuzz',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

"""
Para crear la carpeta dist con los paquetes para los releases y binarios:
python setup.py bdist_wheel sdist
"""