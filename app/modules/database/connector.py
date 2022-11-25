class DatabaseConnector():
    """
    Attributes
    ---
    """
    logging = __import__('logging') #logging module as attribute
    """
    Methods
    ---
    """
    def __init__(self):
        """
        Function that initializes class
        ---
        Params: No arguments/parameters
        Objective: Start logging into file 
        Returns: DatabaseConnector class
        """
        import logging
        logFileFormatter = logging.Formatter(
            fmt=f"%(levelname)s %(asctime)s (%(relativeCreated)d) \t %(pathname)s F%(funcName)s L%(lineno)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        fileHandler = logging.FileHandler(filename='services.log') #configurated file
        fileHandler.setFormatter(logFileFormatter)
        fileHandler.setLevel(level=logging.INFO)
        logging.basicConfig(level=logging.INFO)
        self.logging = logging.getLogger(__name__) #<<<<<<<<<<<<<<<<<<<<
        self.logging.addHandler(fileHandler) #adding configurated file
    
    def connect_to_db(self, db:str="\data\Training.db")->None:
        """
        Class method
        ---
        Params: db (string [Not Required, default="\data\Training.db"])
        Objective: Establish connection to sqlite dabatase 
        Returns: None
        """
        try:
            import sqlite3
            self.con = sqlite3.connect(db)
            self.cur = self.con.cursor()
        except Exception as e:
            self.logging.error("ERROR: {}".format(e))

    def execute_query(self, query:str)->list:
        """
        Class method
        ---
        Params: query (string [Required])
        Objective: Executes query and returns results in list 
        Returns: List
        """
        res = self.cur.execute(query)
        return res.fetchall()
    
    def __del__(self):
        """
        Function that deletes class once all methods have been applied and thread is finalized.
        ---
        Params: No arguments/parameters
        Objective: Close connection to database
        Returns: None
        """
        self.con.close()