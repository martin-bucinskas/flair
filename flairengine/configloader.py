import toml


def load_configs(config_path='config.toml'):
    """ Loads configuration TOML file as a dictionary. """
    parsed_toml = dict()

    try:
        with open('config.toml', 'r') as file:
            parsed_toml = toml.load(file)
            print(parsed_toml)
    except FileNotFoundError:
        print('File not found: ' + config_path)

    return parsed_toml
