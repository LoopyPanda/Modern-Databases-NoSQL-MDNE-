from fastapi import APIRouter, HTTPException, Depends
from backend.db.connection import get_db_connection
from psycopg2.extras import DictCursor

router = APIRouter()

# Fetch all appliances for a specific user (Read Operation)
@router.get("/users/{user_id}/appliances")
def get_appliances(user_id: int):
    """
    Fetch all appliances for a specific user in their houses.
    """
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)

    # Query to fetch appliances for the given user
    cursor.execute("""
        SELECT * FROM Appliance a 
        JOIN House h ON a.houseid = h.HouseID 
        JOIN HouseUser hu ON hu.HouseID = h.HouseID 
        WHERE hu.UserID = %s;
    """, (user_id,))
    appliances = cursor.fetchall()
    conn.close()

    if not appliances:
        raise HTTPException(status_code=404, detail="No appliances found for the user")

    return [dict(appliance) for appliance in appliances]

# Create a new appliance (Create Operation)
@router.post("/appliances")
def create_appliance(name: str, house_id: int):
    """
    Create a new appliance in a specified house.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO Appliance (name, houseid)
            VALUES (%s, %s) RETURNING applianceid, name, houseid;
            """, (name, house_id)
        )
        appliance = cursor.fetchone()
        conn.commit()
        conn.close()
        return dict(appliance)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Update an appliance (Update Operation)
@router.put("/appliances/{appliance_id}")
def update_appliance(appliance_id: int, name: str = None, house_id: int = None):
    """
    Update an existing appliance by its appliance_id.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Prepare dynamic update query
        update_query = "UPDATE Appliance SET"
        values = []

        if name:
            update_query += " name = %s,"
            values.append(name)
        if house_id:
            update_query += " houseid = %s,"
            values.append(house_id)

        # Remove trailing comma and complete WHERE clause
        update_query = update_query.rstrip(",") + " WHERE applianceid = %s RETURNING applianceid, name, houseid;"
        values.append(appliance_id)

        cursor.execute(update_query, tuple(values))
        appliance = cursor.fetchone()

        if not appliance:
            raise HTTPException(status_code=404, detail="Appliance not found")

        conn.commit()
        conn.close()
        return dict(appliance)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Delete an appliance (Delete Operation)
@router.delete("/appliances/{appliance_id}")
def delete_appliance(appliance_id: int):
    """
    Delete an appliance by its appliance_id.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Appliance WHERE applianceid = %s RETURNING applianceid, name, houseid;",
            (appliance_id,)
        )
        appliance = cursor.fetchone()

        if not appliance:
            raise HTTPException(status_code=404, detail="Appliance not found")

        conn.commit()
        conn.close()
        return dict(appliance)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
