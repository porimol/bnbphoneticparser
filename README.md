# Bengali Phonetic Parser

This package will help you to convert Bengali text to Banglish as well as Banglish to Bengali


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development, testing purposes and as well as in production machine. See deployment for notes on how to deploy the project on a live system.


### Python Version
Minimum python version should have 3.x.x or upper

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
$[sudo] pip install bnbphoneticparser
```

OR, git clone

```
$ git clone https://github.com/porimol/bnbphoneticparser.git

$ cd bnbphoneticparser
$ python setup.py install
```

### Example

#### Bengali to Banglish Example
```python
# coding=utf-8
from BengaliPhoneticParser import BengaliToBanglish


bengali2banglish = BengaliToBanglish()
bengali_text = "আমি বাংলাদেশি"
print(bengali2banglish.parse(bengali_text.strip()))
```

#### Bengali to Banglish Output
```
aMi bangLadESi
```

#### Banglish to Bengali Example
```python
# coding=utf-8
from BengaliPhoneticParser import BanglishToBengali


banglish2bengali = BanglishToBengali()
banglish_text = "ami banglay gan gai"
print(banglish2bengali.parse(banglish_text.strip()))
```

#### Banglish to Bengali Output
```
আমি বাংলায় গান গাই
```

## Running the tests

Test Banglish to Bengali

```python
pytest tests/testbenglishtobanglish.py
```

Test Bengali to Banglish

```python
pytest tests/testbanglishtobengali.py
```

## Authors

* **[Porimol Chandro](https://github.com/porimol)**

See also the list of [contributors](https://github.com/porimol/BengaliPhoneticParser/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


Credit
---------

[Bangla Phonetic Parser Python](https://github.com/ShuvenduBikash/Bangla_phonetic_parser_Python) open source project.

[Author :- Shuvendu Bikash](https://github.com/ShuvenduBikash)
