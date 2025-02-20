import sqlite3
from fastapi import FastAPI

app = FastAPI()

DATABASE = "characters.db"

def query_db(query, params=()):
    """Helper function to query SQLite."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

@app.get("/seteth")
def get_seteth():
    """Retrieve Seteth's data from the special table."""
    result = query_db("SELECT * FROM seteth WHERE name = 'Seteth'")
    return {"Seteth": result} if result else {"error": "Seteth data not found"}

@app.get("/character/{name}")
def get_character(name: str):
    """Retrieve character details from the characters table."""
    result = query_db("SELECT * FROM characters WHERE name = ?", (name,))
    return {"Character": result} if result else {"error": "Character not found"}

@app.get("/world_lore/{name}")
def get_world_lore(name: str):
    """Retrieve world lore details from the database."""
    result = query_db("SELECT * FROM world_lore WHERE name = ?", (name,))
    return {"WorldLore": result} if result else {"error": "World lore not found"}

@app.get("/timeline/{year}")
def get_timeline(year: str):
    """Retrieve historical events for a given year."""
    result = query_db("SELECT event FROM timeline WHERE year = ?", (year,))
    return {"Events": [row[0] for row in result]} if result else {"error": "No events found"}

# Run API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
