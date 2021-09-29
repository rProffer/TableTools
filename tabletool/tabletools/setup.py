from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='tabletools',
    author='Robyn Proffer',
    author_email='robynproffer@gmail.com',
    # Needed to actually package something
    packages=['tabletools'],
    # Needed for dependencies
    install_requires=['openpyxl'],
    # *strongly* suggested for sharing
    version='1.0',
    # The license can be anything you like
    license='exla',
    description='tools for interfacing with excel tables',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)