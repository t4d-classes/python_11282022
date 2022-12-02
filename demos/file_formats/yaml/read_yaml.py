""" yaml demo module """

import pathlib
import yaml


with open(pathlib.Path("config.yaml")) as sample_file:

    config = yaml.load(sample_file, Loader=yaml.SafeLoader)

    print(config)
