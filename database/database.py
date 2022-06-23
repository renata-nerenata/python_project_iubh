from sqlalchemy import create_engine

# from src.exception import WrongDataName
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from patterns import create_pattern, create_final_pattern

SQLITE = "sqlite"
TRAIN = "training"
IDEAL = "ideal"
FINAL = "final"


class Database:
    ENGINE = {SQLITE: "sqlite:///{DB}"}
    db_engine = None

    def __init__(self, dbtype, dbname=""):
        """
        :param dbtype: Database type
        :param dbname: name of created database
        """
        if dbname != dbname.lower():
            pass
            # raise WrongDataName(dbname)

        if dbtype in self.ENGINE.keys():
            engine_url = self.ENGINE[dbtype].format(DB=dbname)
            self.db_engine = create_engine(engine_url)
            print(self.db_engine)
        else:
            print("DBType is not found in DB_ENGINE")
        print("DBType is not found in DB_ENGINE")

    def create_db_tables(self):
        """
        Main function for table creation
        :return:
        """
        metadata = MetaData()
        create_pattern(TRAIN, metadata, 4)
        create_pattern(IDEAL, metadata, 50)
        create_final_pattern(FINAL, metadata)
        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error: Some error occurred during table creation")
            print(e)

    def execute_query(self, query=""):
        """
        :param query: Query for execution
        :return:
        """
        if query == "":
            return
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def push_dataframe(self, df, table):
        """
        Push dataframe into database
        :param df: Dataframe
        :param table: Table name in database
        """
        try:
            df.to_sql(table, con=self.db_engine, if_exists="replace", index=False)
        except Exception:
            print("Error: Some error occurred during table insertion")

    def print_all_data(self, table="", query=""):
        query = query if query != "" else "SELECT * FROM '{}';".format(table)
        print(query)
        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row)  # print(row[0], row[1], row[2])
                result.close()
        print("\n")


# Program entry point
def main():
    dbms = Database(SQLITE, dbname="db.sqlite")
    # Create Tables
    dbms.create_db_tables()
    # dbms.push_dataframe(df, table)
    # dbms.print_all_data(USERS)
    # dbms.print_all_data(ADDRESSES)
    # dbms.sample_query() # simple query
    # dbms.sample_delete() # delete data
    # dbms.sample_insert() # insert data
    # dbms.sample_update() # update data


# run the program
if __name__ == "__main__":
    main()
