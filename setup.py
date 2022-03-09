from setuptools import setup, find_packages
from camel.storage.components.profile import Profile


Profile.create_storage()


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
          "cml=camel.interface.entry_points.main_interface:main",

          "cml-profile=camel.storage.entry_points.help:profile",
          "cml-profile-create=camel.storage.entry_points.create_profile:main",
          "cml-profile-switch=camel.storage.entry_points.switch_profile:main",
          "cml-profile-delete=camel.storage.entry_points.delete_profile:main",

          "cml-ssh-add=camel.ssh_tools.entry_points.add_ssh:main",
          "cml-ssh-delete=camel.ssh_tools.entry_points.delete_ssh:main",
          "cml-ssh-get=camel.ssh_tools.entry_points.get_all_ssh:main",
       ]
   },
)
