# coding=utf-8
from setuptools import setup, find_packages


# read readme file
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='bnbphoneticparser',
    version='0.1.0',
    install_requires = ['BengaliPhoneticParser'],
    package_dir = {
        '': 'BengaliPhoneticParser'
    },
    packages = find_packages('BengaliPhoneticParser', exclude='tests'),
    url='https://github.com/porimol/BengaliPhoneticParser',
    license='MIT License',
    author='Porimol Chandro',
    author_email='porimolchandroroy@gmail.com',
    description='Bengali Phonetic Parser',
    long_description=long_description,
    keywords = [
        'NLP',
        'Python',
        'Bengali to Banglish',
        'Banglish to Bengali'
    ],
)
