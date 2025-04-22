import psycopg2
from config import load_config
def insert_vendor(user_name,phone):
    sql = """INSERT INTO journal(user_name,phone)
             VALUES(%s,%s);"""
    vendor_id = None
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (user_name,phone))
                # get the generated id back
                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return vendor_id
if __name__ == '__main__':
    insert_vendor("3M Co.","87075698477")
    insert_vendor("Aidyn","87875698477")
