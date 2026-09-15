from database.DB_connect import DBConnect
from model.airport import Airport
from model.state import State


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_all_airports(num_voli):
        conn = DBConnect.get_connection()
        #  {airport_id: (out_voli, in_voli)}
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.id as airport_id, COUNT(f.id) as out_voli, (select count(f.id) from flights f  where a.id = f.DESTINATION_AIRPORT_ID group by a.state,a.id having COUNT(f.id)>%s order by a.STATE asc) as in_voli
from airports a, flights f 
where a.id = f.ORIGIN_AIRPORT_ID 
group by a.state,a.id
having COUNT(f.id)>%s
order by a.STATE asc """

        cursor.execute(query, (num_voli,num_voli))

        for row in cursor:
            result = {row["airport_id"]: (row["out_voli"], row['in_voli']) for row in cursor}

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_states(airports):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.state as id, a.id as airport_id
                    from airports a
                 where a.id = %s"""
        cursor.execute(query, (airports,))
        result = next((row["id"],row["airport_id"]) for row in cursor)

        cursor.close()
        conn.close()
        return result