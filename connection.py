from sqlalchemy import create_engine

def postgres_connection():
    db_string = "postgresql://postgres:34201800@sftp.cftvarydd1mo.us-east-1.rds.amazonaws.com:5432/postgres"
    engine = create_engine(db_string)
    return engine