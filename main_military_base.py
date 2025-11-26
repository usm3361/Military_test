from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from pydantic import BaseModel, Field
import sqlite3
import os
from datetime import datetime
import uvicorn
import csv
import io

app = FastAPI(title="soldierss - Residential Assignment on Base API", version="1.0.0")

class Soldiers(BaseModel):
    
    person_num : int 
    first_name : str
    last_name : str
    gender : str
    city : str
    distance_km : int | None = None
    status_places: str 
    
    
class Buildingsoldierss(BaseModel):
    id_building : int 
    max_num_rooms : int = 10
    number_tenats : int = 80
    list_of_rooms : list
    
    def add_rooms_of_Building(rooms:Rooms):
        
        room = Rooms()
        return room
    
class Rooms(BaseModel):
    building_id : int
    room_num : int
    tenat_id : int
    tenats_of_room : list
    is_full: bool = False
    
    def add_soldiers_to_rooms(soldiers:Soldiers):
        count = 0
        if count <= 7:
            Rooms.tenats_of_room.append(soldiers)
            count += 1
        else:
            Rooms.is_full = True
            
    
    def get_building_by_id(self, buildings):
        for building in buildings:
            if building.id_building == self.building_id:
                return building
    
class BaseMilitary(BaseModel):
    residences:int = 2
    soldierss: int = 80 * residences
    is_full: bool = False
     
    def add_Building_to_base(Building:Buildingsoldierss):
        Building = Buildingsoldierss()
        


list_of_soldierss = []
def import_csv_to_dict(csv_content: bytes)-> dict:
    # Read CSV content
    csv_text = csv_content.decode('utf-8')
    csv_reader = csv.DictReader(io.StringIO(csv_text))
    
    for row in csv_reader:
        list_of_soldierss.append({
            'person_num': row.get("person_num", ''),
            'first_name': row.get("first_name", '').strip(),
            'last_name': row.get("last_name", '').strip(),
            'gender' : row.get("gender", '').strip(),
            'city' : row.get("city", '').strip(),
            'distance_km': int(row.get(("distance_km")).strip()) if int(row.get(("distance_km")).strip()) else None,
    })
    
def sort_soldierss(soldierss):
    sort_soldierss_by_contrance = sorted(soldierss, key=lambda x: x['distance_km'])
    return sort_soldierss_by_contrance



    
    
        
# @app.post("/soldierss", response_model=soldiers, status_code=201)
# def create_soldiers(soldiers: soldiers):
    
#     return
    
@app.post("/soldierss/assignWithCsv")
async def upload_csv(file: UploadFile = File('hayal_300_no_status.csv')):
    # Validate file type
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    
    contents = await file.read()
    
    import_csv_to_dict(contents)
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
    
