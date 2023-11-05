# setup.py
from setuptools import setup, find_packages

setup(
    name='pca_inputter',
    version='0.1.1',
    author='Aleksa Mihajlovic',
    author_email='mihajlovic.aleksa@gmail.com',
    packages=find_packages(),
    url='https://github.com/maleckicoa/pca_inputter/',
    license='LICENSE.txt',
    install_requires=[
        'pandas>=1.3.5',
        'numpy>=1.17.3',
        'scikit-learn>=0.22.2'],
    description='Package for handling missing values in numerical datasets',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Content type of the long description
    python_requires='>=3.7.1',
)



