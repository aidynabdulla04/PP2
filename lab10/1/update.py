import psycopg2
from config import load_config
def update_vendor(phone,user_name):
    """ Update vendor name based on the vendor id """
    updated_row_count = 0
    sql = """ UPDATE journal
                SET user_name = %s
                WHERE phone = %s"""
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (user_name, phone))
                updated_row_count = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count
if __name__ == '__main__':
    update_vendor("8707555656", "3M Co.")
