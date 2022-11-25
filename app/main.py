# A MUST import
#-----------------------------------------------------------
import os

# Services module import
# TODO: Import the services you plan to use
#-----------------------------------------------------------
from modules.aws.connector import AWSManager
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
        csvfile = current_dir_path + '\\output\\result.csv'
        #TODO: 
        primary_key_aws = "[PRIMARY KEY]"
        secret_primary_key_aws = "[SECRET PRIMARY KEY]"
        aws_buff.manual_secrets_log_in(primary_key_aws, secret_primary_key_aws)
        with open(csvfile, 'w') as file:
            write = csv.writer(file)
            write.writerows(data)
        aws_buff.set_bucket_name = "testbucket788bsdf"
        aws_buff.establish_connection()
        upload = aws_buff.upload_file(csvfile)
        print(upload)