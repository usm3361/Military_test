from fastapi import FastAPI, HTTPException, Request, UploadFile, File 
from pydantic import BaseModel, Field
import sqlite3
import os
from datetime import datetime
import uvicorn
import csv
import io

app = FastAPI(title="Soldiers - Residential Assignment on Base API", version="1.0.0")


class Soldier(BaseModel):
    person_num : int = Field() #לעשות שיתחיל ב8
    first_name : str
    last_name : str
    Gender : str
    city : str
    distance_km : int
    status_places: str 

    

class HomePlaceSoldiers(BaseModel):
    id_home: int # A/B
    name : str | None = None
    age : int | None = None
    email : str | None = None
    
