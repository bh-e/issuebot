from setuptools import setup, find_packages


setup(
    
    name='issuebot',
    version='1.2.0',
    description='Collect issues via webhooks and send as message to MUC',
    long_description='A bot that receives triggered webhooks from remote git repository, parse the content and send as message to a specified MUC',
    url='https://github.com/bh-e/issuebot',
    author='Abhijith PA',
    author_email='abhijith@openmailbox.org',
    license='GPL-3+',
    scripts = ['issuebot'],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ],
    install_requires=['flask','sleekxmpp'],
       )
