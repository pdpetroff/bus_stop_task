##########################################################################
#
# Main FastAPI app
#
# project: Bus Stations Task
# updated: 30.04.2023
#
##########################################################################

from fastapi import FastAPI
from bus_db import BusDB


app = FastAPI()
busdb = BusDB()

# Retrieve Bus stop information by ID
@app.get("/bus_station/{id}")
async def get_bus_station(id:int):
    return {"bus_station": busdb.convert_to_dict(busdb.get_bus_stop(id))}

# Remove Bus stop information by ID
@app.delete("/bus_station/{id}")
async def delete_bus_station(id:int):
    return {"deleted_bus_stations_count":busdb.delete_bus_stop(id)}

# Upsert Bus stop information
@app.put("/bus_station/")
async def upsert_bus_station(name:str, lat:float, lng:float, id: int = -1):
    return {"upserted_bus_stations_count":busdb.set_bus_stop(id, name, lat, lng)}

# Retrieve Bus stop information by area
@app.get("/bus_stations_in_area/")
async def get_bus_stations_in_area(min_lat:float, min_lng:float, max_lat:float, max_lng:float):
    return {"bus_stations_in_area": busdb.convert_to_dict(
            busdb.get_bus_stops_in_area(min_lat=min_lat, min_lng=min_lng, max_lat=max_lat, max_lng=max_lng))
            }

