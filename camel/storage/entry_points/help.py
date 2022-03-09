from camel.storage.factory import profile_factory


def main():
    for i in profile_factory(help=True):
        print(i)
