# A MUST import
#-----------------------------------------------------------
import os

# Services module import
# TODO: Import the services you plan to use
#-----------------------------------------------------------
from modules.storage_services_module._aws_ import AWSManager
from modules.database.connector import DatabaseConnector
#-----------------------------------------------------------
if __name__ == "__main__":
    import os
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    print(current_dir_path)
    db = r'\modules\database\data\Training.db'
    dbpath = current_dir_path + db
    database = DatabaseConnector()
    database.connect_to_db(dbpath)
    query = """SELECT name FROM sqlite_master WHERE type='table';"""
    global tables
    tables = database.execute_query(query)
    if tables is not []:
        import csv
        data = database.execute_query('SELECT * FROM Invoices;')
        aws_buff = AWSManager()
        filename = r"\..\config\defaults.yaml"
        filepath = current_dir_path + filename
        csvfile = current_dir_path + '\\output\\result.csv'
        aws_buff.secrets_log_in(filepath)
        with open(csvfile, 'w') as file:
            write = csv.writer(file)
            write.writerows(data)
        aws_buff.set_bucket_name = "testbucket788bsdf"
        aws_buff.establish_connection()
        upload = aws_buff.upload_file(csvfile)
        print(upload)