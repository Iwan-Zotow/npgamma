from setuptools import setup

setup(
    name = "npgamma",
    version = "0.3.2",
    author = "Simon Biggs",
    author_email = "mail@simonbiggs.net",
    description = "Perform a gamma evaluation comparing two arbitrarily sized dose grids",
    long_description = "Using numpy to find the gamma index / gamma evaluation. This gamma index is often used in Medical Physics. Example of the code in action can be found [here](http://nbviewer.ipython.org/github/SimonBiggs/npgamma/blob/master/example.ipynb). USE AT YOUR OWN RISK"
    keywords = ["radiotherapy", "gamma evaluation", "gamma index", "distance to agreement", "medical physics"],
    url = "https://github.com/SimonBiggs/npgamma/",
    dowload_url = "https://github.com/SimonBiggs/npgamma/tarball/0.1",
    packages = ["npgamma"],
    license='AGPL3+',
    classifiers = [],
)
