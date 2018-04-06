# coding=utf-8
from setuptools import setup, find_packages


# read readme file
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='bnbphoneticparser',
    version='0.1.5',
    python_requires='>3.0.0',
    packages = find_packages(exclude='tests'),
    url='https://github.com/porimol/bnbphoneticparser',
    license='MIT License',
    author='Porimol Chandro',
    author_email='porimolchandroroy@gmail.com',
    description='Bengali Phonetic Parser',
    long_description=long_description,
    keywords = ['NLP', 'Python', 'Bengali', 'Banglish'],
)
