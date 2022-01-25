from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_get_list():
    response = client.get("/project/list/")
    assert response.status_code == 200

def test_create():
    #response = client.post("/project/create/",data={"_name": "kento","_images": "APD"},headers={"Content-Type": "application/x-www-form-urlencoded"})
    response = client.post("/project/create/",data=dict(_name="kento",_images=["APD","AUBIST"]))
    #print(response.json())
    assert response.status_code == 200
    assert response.json() == {"id":"1","name":"kento","create_user":"User1","images":["APD","AUBIST"],"create_timestamp":int(time.time())}