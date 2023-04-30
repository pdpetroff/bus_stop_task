##########################################################################
#
# Database communication class
#
# project: Bus Stations Task
# updated: 30.04.2023
#
##########################################################################

import psycopg2
from psycopg2 import Error

import config as cfg

class BusDB:
 
    # init method for creating DB connection
    def __init__(self):

        try:
            self.connection = psycopg2.connect(
                host=cfg.db_host,
                database=cfg.db_database,
                user=cfg.db_user,
                password=cfg.db_pass)

            self.cursor = self.connection.cursor()

            print("Successfully connected to PostgreSQL DB: {}".format(cfg.db_database))

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    # Close DB Connection
    def __del__(self):   
        if (self.connection):
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")

    # Retrieve information for one Bus stop
    def get_bus_stop(self, id:int):
        sql = "SELECT * FROM bus_stops WHERE id={}".format(id)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    # Retrieve information for many Bus stops in area
    def get_bus_stops_in_area(self, min_lat:float, min_lng:float, max_lat:float, max_lng:float ):
        sql = "SELECT * FROM bus_stops WHERE ((location[1] BETWEEN {} AND {}) \
            AND (location[2] BETWEEN {} AND {}))".format(min_lat, max_lat, min_lng, max_lng)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        return result

    # Delete a Bus stop
    def delete_bus_stop(self, id:int):
        sql = "DELETE FROM bus_stops WHERE id={}".format(id)
        self.cursor.execute(sql)
        self.connection.commit()

        return self.cursor.rowcount

    # Upsert Bus stop information
    def set_bus_stop(self, id:int == -1 , name:str, lat:float, lng:float):
        if (id==-1):
            sql = "INSERT INTO bus_stops (name, location) VALUES ('{}', ARRAY[ {}, {} ])".format(name, lat, lng)
        else:
            sql = "UPDATE bus_stops SET name = '{}', location = ARRAY [ {}, {} ] WHERE id = {}".format(name, lat, lng, id)
        
        self.cursor.execute(sql)
        self.connection.commit()


        return self.cursor.rowcount

    #Convert recordset to dict
    def convert_to_dict(self, recordset):
        tmp_dict = [{'id': row[0], 'name': row[1], 'location': { "lat": row[2][0], "lng":row[2][1] }} for row in recordset]
        return (tmp_dict)
