# setup.py
from setuptools import setup, find_packages

setup(
    name='pca_data_inputer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'scikit-learn>=0.22.0'],

    author='Aleksa Mihajlovic',  # Replace with your name
    author_email='mihajlovic.aleksa@gmail.com',  # Replace with your email address
    description='Package for handling missing values in numerical datasets',  # Short description of your package
    long_description=open('README.md').read(),  # Long description read from the README.md
    long_description_content_type='text/markdown',  # Content type of the long description
    url='https://github.com/maleckicoa/pca_data_inputter',  # Replace with the URL of your package repository
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development status of the package
        'Intended Audience :: Developers',  # Target audience
        'Natural Language :: English',  # Language
        'Programming Language :: Python :: 3',  # Supported Python versions
        'Programming Language :: Python :: 3.7',  # Supported Python versions
        'Programming Language :: Python :: 3.8',  # Supported Python versions
        'Programming Language :: Python :: 3.9',  # Supported Python versions
        # Add other Python versions if necessary
    ],
    python_requires='>=3.7',  # Minimum version of Python required
    # If you want to include non-code files (like the CSV you mentioned), they need to be specified
    #include_package_data=True,
    #package_data={'mypca_package': ['data/*.csv']},  # Assuming 'data' is a directory with CSV files
    # If you want to create scripts to run your PCA imputation from the command line, specify them in entry_points
)