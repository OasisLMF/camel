from camel.terra_configs.components.config_mapper import TerraConfigMapper


def main():
    print("the following terraform configs are available:")

    profile = TerraConfigMapper.get_cached_profile()

    for config in profile.get_configs():
        print(config.split("/")[-1])
