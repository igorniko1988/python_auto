import os
import yaml
import sys
from pathlib import Path
from yaml.loader import SafeLoader

root = Path(__file__)
print(root.parent.parent.joinpath('config.local.yaml'))

def read_from_yaml(file, env_var):
    with open(file) as f:
        data = yaml.load(f, Loader=SafeLoader)
        var = data[env_var]
    return var


def get(env_var, default):
    env = os.environ.get('env', 'local')
    os_env_var = os.environ.get(env_var)
    if os_env_var:
        return os_env_var
    if env:
        from_file = read_from_yaml(f'config.{env}.yaml', env_var=env_var)
        if from_file:
            return from_file
    return default

