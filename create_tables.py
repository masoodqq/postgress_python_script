import psycopg2
from sql_queries import create_table_queries, drop_table_queries#, insert_table_queries


def create_database():
    """
    - Creates and connects to the imusicdb
    - Returns the connection and cursor to imusicdb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create imusic database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS imusicdb")
    cur.execute("CREATE DATABASE imusicdb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to imusic database
    conn = psycopg2.connect("host=127.0.0.1 dbname=imusicdb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    - Drops (if exists) and Creates the imusic database. 
    
    - Establishes connection with the imusic database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)
    #insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()