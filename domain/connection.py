from domain.credentials import *
from sqlalchemy import create_engine


class Database():
    connection = create_engine(f"postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}")

    def __init__(self):
        self.connection = self.connection.connect()
        print("Lab2")


if __name__ == "__main__":
    db_con = Database()
