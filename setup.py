from setuptools import setup, find_packages
from camel.interface.components.camel_logo import print_camel_image


setup(
   name='camel',
   version='0.1.0',
   author='maxwell flitton',
   author_email='maxwellflitton@gmail.com',
   packages=find_packages(exclude=("tests",)),
   scripts=[],
   url="https://github.com/OasisLMF/camel",
   description='basic build automation tool',
   long_description="basic build automation tool",
   package_data={'': ['script.sh']},
   include_package_data=True,
   install_requires=[
       "pyyaml",
       "termcolor"
   ],
   entry_points={
       "console_scripts": [
           "terra-apply=command_engine.run_terra:main",
           "terra-destroy=command_engine.destroy_terra:main",
           "terra-install=command_engine.install_terraform:main"
        ]
   },
)

print_camel_image()
