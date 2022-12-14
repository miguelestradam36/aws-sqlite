class SetUpExecuter():
    """
    Attributes
    ---
    """
    filepath = "..\\..\\..\\config\\defaults.yaml" #file path for configuration files
    venv_prefix = "python -m" #can be modified to execute from venv
    os = __import__('os') #os module as attribute
    log = __import__('logging') #logging module as attribute
    """
    Methods
    ---
    """
    def __init__(self):
        """
        Function that intiliazes class 
        ---
        Params: No arguments/parameters
        Objective: Save logger file and check modules into environment in class creation
        Returns: SetUpExecuter class
        """
        import logging
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fileHandler = logging.FileHandler(filename='test.log')
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(__name__) #<<<<<<<<<<<<<<<<<<<<
        self.log.addHandler(fileHandler)

        self.read_defaults()
        self.install_test_modules()
        self.install_services()
        self.install_api_modules()

    def install_services(self)->None:
        """
        Class method
        ---
        Params: No arguments/parameters
        Objective: Checks modules into environment
        Returns: None
        """
        print("Checking in to api-connection and app installations...")
        for module in self.yaml_config["python"]["global"]["modules"]["standard"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))
    def install_test_modules(self)->None:
        """
        Class method
        ---
        Params: No arguments/parameters
        Objective: Checks test modules into environment
        Returns: None
        """
        self.log.info("Checking in to services installation...")

        import sys

        module_ = 'pytest-virtualenv'

        if module_ in sys.modules:
            self.log.info("Checking {} module into venv".format(module_))
        else:
            self.log.info("Installing {} module into venv".format(module_))
            self.os.system("{} pip install {}".format(self.venv_prefix, module_))    

        for module in self.yaml_config["python"]["global"]["modules"]["test"]:
            try:
                self.log.info("Checking {} module into venv".format(module["import"]))
                assert __import__(module["import"])
            except ImportError as error:
                self.log.info("Installing {} module into venv".format(module["install"]))
                self.os.system("{} pip install {}".format(self.venv_prefix, module["install"]))

    def read_defaults(self)->None:
        """
        Class method
        ---
        Params: No arguments/parameters
        Objective: Reads values from YAML file
        Returns: None
        """
        fullpath = self.os.path.join(self.os.path.dirname(__file__), self.filepath)

        try:
            self.log.info("Checking {} module into venv".format("yaml"))
            assert __import__("yaml")
        except ImportError as error:
            self.log.info("Installing {} module into venv".format("PyYaml"))
            self.os.system("{} pip install {}".format(self.venv_prefix,"pyyaml"))
        finally:
            yaml = __import__("yaml")
        
        self.log.info("Reading configuration variables on YAML...")
        with open(fullpath, 'r') as file:
            self.yaml_config = yaml.safe_load(file)