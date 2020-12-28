import environ


def load_env(file_name='.env'):
    BASE_DIR = environ.Path(__file__) - 2
    ENV_FILE = file_name

    env = environ.Env(DEBUG=(bool, False))
    env.read_env(BASE_DIR(ENV_FILE))
    return env
