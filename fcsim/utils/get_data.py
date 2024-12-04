import os
import pkg_resources
from pathlib import Path


def get_data(filename):
    """ Finds the directory of the package.
    """
    filepath = Path(pkg_resources.resource_filename('fcsim', 'data/' + filename)).resolve()
    if filepath.exists():
        return filepath
    else:
        raise FileNotFoundError(f'{filename} does not exist...')