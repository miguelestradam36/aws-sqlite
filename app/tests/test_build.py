import pytest

def test_dependencies():

    import yaml
    import os

    # Repeated values
    filepath = "../src/config/defaults.yaml"
    fullpath = os.path.join(os.path.dirname(__file__), filepath)

    with open(fullpath, 'r') as file:
        global yaml_config
        yaml_config = yaml.safe_load(file)
    
    for module in yaml_config["python"]["global"]["modules"]["standard"]:
        assert __import__(module['import'])

    for module in yaml_config["python"]["services"]["modules"]:
        assert __import__(module['import'])

    for module in yaml_config["python"]["global"]["modules"]["test"]:
        assert __import__(module['import'])