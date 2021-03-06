from setuptools import  find_packages, setup
import sys
import os

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='publicdata',
    version='0.3.10',
    url='https://github.com/CivicKnowledge/publicdata',
    license='MIT',
    author='Eric Busboom',
    author_email='eric@busboom.org',
    description='Metatab support code for working with public datasets',
    packages=find_packages(),
    zip_safe=True,
    install_requires=[
        'fs >= 2',
        'rowgenerators',
        'pandas',
        'requests',
        'geoid',
        'tqdm',
        'fuzzy', # For NLSY
        'nltk', # for NLSY
        'stringdist', # For NLSY
        'fredapi' # For FRED
        ],
    entry_points={
        'appurl.urls': [

            "nlsy+ = publicdata.nlsy.appurl:NlsyUrl",
            "fred: = publicdata.fred.appurl:FredUrl"
        ],
        'rowgenerators': [

        ],
        'console_scripts': [
            'nlsy = publicdata.nlsy.__main__:main'
        ],
        'mt.subcommands': [
            'fred=publicdata.fred.cli:fred',
        ]


    },
)

