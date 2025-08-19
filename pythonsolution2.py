from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class inventory(BaseModel):
    id: int
    name: str
    description: str
    quantity: int
    price: float


inventory_db= {}

'''@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}'''

@app.get("/inventory")
def get_items():
    return list(inventory_db.values())


@app.get("/inventory/inventory_id")
def get_specific_item(inventory_id: int):
    if inventory_id in inventory_db:
        return inventory_db.get(inventory_id)
    return "ID does not exist"


@app.put("/inventory/inventory_id")
def update_items(inventory_id: int, Inventory: inventory):
    if inventory_id != Inventory.id:
        return "Error, ID mismatch"
    inventory_db[inventory_id] = Inventory
    return Inventory


@app.post("/inventory")
def post_items(Inventory: inventory):
    if Inventory.id in inventory_db:
        return 'Item already exists'
    inventory_db[Inventory.id]= Inventory
    return Inventory


@app.delete("/inventory/inventory_id")
def delete_item(inventory_id:int):
    if inventory_id in inventory_db:
        del inventory_db[inventory_id]
        return "Successfully deleted"
    return "ID does not exist"
    

