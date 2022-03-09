from camel.utils.entry_point_factory import entry_point_factory, help_factory


def profile_factory(help=False):
    entry_points = [
        ("create", "create_profile", "creates a new profile")
    ]
    if help is False:
        return entry_point_factory(module="profile", commands=entry_points, directory="storage")
    return help_factory(module="profile", commands=entry_points)
