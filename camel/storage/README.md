# Storage 
This module manages the storage throughout the program.

## Profile
When a user uses the program they may want to refer to values such as access keys or a file defining the
configuration around a model run. Each profile has their own directory where config files and keys
can be accessed. Whilst the program is running, it can only use one profile at a time because the program
needs to know where to look to access files and values. The profile being used at one particular time is
known as the "cached profile". We manage the profile by writing the cached profile name in a ```txt```
file in a specific place.

### Creating profile
If we want to create a profile we do the following:
```python
from camel.storage.components.profile_storage import Profile

profile = Profile(name="maxwell")
profile.create_profile()
```
This creates the following directories:

- **profile_base_path**: the directory where everything for the profile is stored
- **keys_path**: the directory where the SSH keys are stored
- **terra_builds_path**: the directory where the terraform builds are stored
- **configs_path**: the directory where the config files are stored such as model runs SSH configs etc

### Deleting profile
If we want to delete a profile we do the following:
```python
from camel.storage.components.profile_storage import Profile

profile = Profile(name="maxwell")
profile.delete_profile()
``` 
This deletes the following directories:

- **profile_base_path**: the directory where everything for the profile is stored
- **keys_path**: the directory where the SSH keys are stored
- **terra_builds_path**: the directory where the terraform builds are stored
- **configs_path**: the directory where the config files are stored such as model runs SSH configs etc

### Caching profile
If we want to cache a profile we do the following:
```python
from camel.storage.components.profile_storage import Profile

profile = Profile(name="maxwell")
profile.cache_profile()
```
This writes the profile name to a ```txt``` file in the ```profile_base_path```.

### Getting cached profile
If we want to get the cached profile we do the following:
```python
from camel.storage.components.profile_storage import Profile

profile = Profile.get_cached_profile()
```
This reads the profile name from a ```txt``` file in the ```profile_base_path``` giving us the name of the cached 
profile.


## Local Profile Variable Storage
In the program we may want to access variables that are stored in the ```STORAGE_VARS123.yml``` file of the 
```configs_path``` belonging to the cached profile. 

### Getting variable dict
Getting a dictionary of all of the variables stored for the profile can be done with the following code:
```python
from camel.storage.components.profile_storage import LocalProfileVariablesStorage
from camel.storage.components.profile_storage import Profile

storage = LocalProfileVariablesStorage()
something: str = storage["something"]
profile: Profile = storage.profile
```

### Adding variable
Adding a variable to the ```STORAGE_VARS123.yml``` file can be done with the following code:
```python
from camel.storage.components.profile_storage import LocalProfileVariablesStorage

storage = LocalProfileVariablesStorage()
storage.add_variable(name="something", value="something")
```
This addition will also update the ```LocalVariableStorage``` from the ```gerund``` package so all gerund commands
will access the variable for the duration of the program.

### Deleting variable
Deleting a variable from the ```STORAGE_VARS123.yml``` file can be done with the following code:
```python
from camel.storage.components.profile_storage import LocalProfileVariablesStorage

storage = LocalProfileVariablesStorage()
storage.delete_variable(name="something")
```
This deletion will also update the ```LocalVariableStorage``` from the ```gerund``` package so all gerund commands
will not access the variable for the duration of the program.

### Updating variable
Updating a variable in the ```STORAGE_VARS123.yml``` file can be done with the following code:
```python
from camel.storage.components.profile_storage import LocalProfileVariablesStorage

storage = LocalProfileVariablesStorage()
storage.add_variable(name="something", value="something else")
```
