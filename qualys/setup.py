from setuptools import setup

setup(
    name='qualys',
    packages=['qualys'],
    description='Hello world enterprise edition',
    version='1.2',
    url='https://github.com/andreimuntean7/test_python_repo/qualys',
    author='Andrei Muntean',
    author_email='andreimuntean0795@gmail.com',
    keywords=['pip','qualys','example'],
    install_requires=["python_version>'3.6'",
    "requests>'2.0'",
    "elasticsearch>='8.2'"]
)
