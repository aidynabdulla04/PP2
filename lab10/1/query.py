import psycopg2
from config import load_config
def get_vendors():
    """ Retrieve data from the journal table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_name,phone FROM journal ORDER BY user_name")
                row = cur.fetchone()
                while row is not None:
                    print(row)
                    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    get_vendors()
