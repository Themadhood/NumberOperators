from setuptools import setup, find_packages

#from my_pip_package import __version__


setup(
    name='TPC_Error',
    version="1.0.0",#__version__,

    url='https://github.com/Themadhood/Error',
    author='Themadhood Pequot',
    author_email='themadhoodpequot@gmail.com',

    packages=find_packages(),
    #py_modules=['Error'],

    install_requires=[
        "gspread",#manipulates google sheets
        "oauth2client",#logs in to google
        "google-api-python-client",],

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
