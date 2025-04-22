import psycopg2
from config import load_config
def delete_part(user_name):
    """ Delete part by part """
    rows_deleted  = 0
    sql = 'DELETE FROM journal WHERE user_name = %s'
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (user_name,))
                rows_deleted = cur.rowcount
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted
if __name__ == '__main__':
    deleted_rows = delete_part("Aidyn")
    print('The number of deleted rows: ', deleted_rows)
