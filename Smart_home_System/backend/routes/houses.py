from fastapi import APIRouter, HTTPException
from backend.db.connection import get_db_connection
from psycopg2.extras import DictCursor

router = APIRouter()

# Fetch all houses (Read Operation)
@router.get("/")
def get_houses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT * FROM House;")
        houses = cursor.fetchall()
        if not houses:
            raise HTTPException(status_code=404, detail="No houses found")
        return [dict(house) for house in houses]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Fetch a single house by its ID (Read Operation)
@router.get("/{house_id}")
def get_house(house_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT * FROM House WHERE HouseID = %s;", (house_id,))
        house = cursor.fetchone()
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        return dict(house)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Create a new house (Create Operation)
@router.post("/")
def create_house(address_line1: str, address_line2: str = None, city: str = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO House (AddressLine1, AddressLine2, City)
            VALUES (%s, %s, %s) RETURNING HouseID, AddressLine1, AddressLine2, City;
            """,
            (address_line1, address_line2, city)
        )
        house = cursor.fetchone()
        conn.commit()
        return dict(house)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Update an existing house (Update Operation)
@router.put("/{house_id}")
def update_house(house_id: int, address_line1: str = None, address_line2: str = None, city: str = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Prepare dynamic update query
        update_query = "UPDATE House SET"
        values = []
        
        if address_line1:
            update_query += " AddressLine1 = %s,"
            values.append(address_line1)
        if address_line2:
            update_query += " AddressLine2 = %s,"
            values.append(address_line2)
        if city:
            update_query += " City = %s,"
            values.append(city)
        
        # Remove trailing comma and complete WHERE clause
        update_query = update_query.rstrip(",") + " WHERE HouseID = %s RETURNING HouseID, AddressLine1, AddressLine2, City;"
        values.append(house_id)
        
        cursor.execute(update_query, tuple(values))
        house = cursor.fetchone()
        
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        
        conn.commit()
        return dict(house)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Delete a house (Delete Operation)
@router.delete("/{house_id}")
def delete_house(house_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM House WHERE HouseID = %s RETURNING HouseID, AddressLine1, AddressLine2, City;",
            (house_id,)
        )
        house = cursor.fetchone()
        
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        
        conn.commit()
        return dict(house)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()
