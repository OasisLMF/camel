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
   extras_require={
      "server": ["Flask>=2.0.3", "Flask-Cors>=3.0.10"]
   },
   entry_points={
       "console_scripts": [
          "cml=camel.interface.entry_points.main_interface:main",
          "cb=camel.basecamp.entry_points.main_interface:main",

          "cml-profile=camel.storage.entry_points.help:profile",
          "cml-profile-create=camel.storage.entry_points.create_profile:main",
          "cml-profile-switch=camel.storage.entry_points.switch_profile:main",
          "cml-profile-delete=camel.storage.entry_points.delete_profile:main",
          "cml-profile-export=camel.storage.entry_points.export_profile:main",
          "cml-profile-import=camel.storage.entry_points.import_profile:main",

          "cml-storage=camel.storage.entry_points.help:storage",
          "cml-storage-create=camel.storage.entry_points.create_storage:main",
          "cml-storage-delete=camel.storage.entry_points.delete_storage:main",
          "cml-storage-get=camel.storage.entry_points.get_storage:main",

          "cml-ssh=camel.ssh_tools.entry_points.help:main",
          "cml-ssh-add=camel.ssh_tools.entry_points.add_ssh:main",
          "cml-ssh-delete=camel.ssh_tools.entry_points.delete_ssh:main",
          "cml-ssh-get=camel.ssh_tools.entry_points.get_all_ssh:main",
          "cml-ssh-enter=camel.ssh_tools.entry_points.ssh_enter:main",

          "cml-key-add=camel.ssh_tools.entry_points.key_add:main",
          "cml-key-delete=camel.ssh_tools.entry_points.key_delete:main",

          "cml-terra=camel.terra.help:main",
          "cml-terra-apply=camel.terra.run_terra:main",
          "cml-terra-destroy=camel.terra.destroy_terra:main",
          "cml-terra-install=camel.terra.install_terraform:main",
          "cml-terra-all=camel.terra.entry_points.get_all:main",

          "cml-tconfig=camel.terra_configs.entry_points.help:main",
          "cml-tconfig-get=camel.terra_configs.entry_points.get_configs:main",
          "cml-tconfig-import=camel.terra_configs.entry_points.import_config:main",
          "cml-tconfig-export=camel.terra_configs.entry_points.export_config:main",
          "cml-tconfig-delete=camel.terra_configs.entry_points.delete_config:main",

          "cml-repo=camel.local.entry_points.help:repo",
          "cml-repo-add=camel.local.entry_points.add_repo:main",
          "cml-repo-update=camel.local.entry_points.update_repo:main",
          "cml-repo-delete=camel.local.entry_points.delete_repo:main",
          "cml-repo-get=camel.local.entry_points.get_all_repos:main",

          "cml-model=camel.models.entry_points.help:main",
          "cml-model-build=camel.models.entry_points.build:main",
          "cml-model-load=camel.models.entry_points.load:main",
          "cml-model-get=camel.models.entry_points.get:main",
          "cml-model-delete=camel.models.entry_points.delete:main",

          "cml-serve=camel.server_entry_point:main",
          
          # this is where we define the entry points for the basecamp

          "cb-project=camel.basecamp.projects.entry_points.help:main",
          "cb-project-create=camel.basecamp.projects.entry_points.create:main",
          "cb-project-update=camel.basecamp.projects.entry_points.update_status:main",
          "cb-project-get=camel.basecamp.projects.entry_points.get:main",
          "cb-project-all=camel.basecamp.projects.entry_points.get_all:api",

          "cb-create=camel.basecamp.entry_points.create:main"
       ]
   },
)
