# python setup.py bdist or bdist_egg
# python setup.py register
# python setup.py bdist upload
from setuptools import setup

setup(
     name='whoislookup',
     version='0.1',
     description='A simple whois lookup script',
     author='Muhammad M Rahman',
     author_email='mmrs151@gmail.com',
     url='https://github.com/mrahma01/py-whois-lookup',
     py_modules=['whoislookup'],
     classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Internet",
      ],
     keywords='whois lookup',
     license='GPL',
     install_requires=[
         'setuptools',
         ],
     )
