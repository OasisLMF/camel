from setuptools import setup, find_packages
from camel.storage.components.profile import Profile
from camel.storage.factory import profile_factory

Profile.create_storage()

entry_points = profile_factory()
entry_points.append("cml=camel.interface.entry_points.main_interface:main")

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
       "console_scripts": entry_points
   },
)
