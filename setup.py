import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(name='bayanat',
      version='0.0.1',
      url='',
      discription="Visualize Arabic Data",
      long_description=readme,
      long_description_content_type='text/markdown',
      author='Zaid Alyafeai, Maged Saeed',
      author_email='arabicmachinelearning@gmail.com',
      license='MIT',
      packages=['bayanat'],
      install_requires=required,
      python_requires=">=3.6",
      include_package_data=True,
      zip_safe=False,
      )
