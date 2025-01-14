from fastapi import APIRouter, HTTPException, Query
from backend.db.connection import get_db_connection
from psycopg2.extras import DictCursor

router = APIRouter()

# Fetch houses associated with a specific user (Read Operation)
@router.get("/")
def get_houses_for_user(user_id: int = Query(..., description="User ID to filter houses")):
    """
    Fetch houses associated with a specific user.
    Args:
        user_id (int): The user ID to filter houses.
    Returns:
        list: List of houses with address and city for the specified user.
    Raises:
        HTTPException: If no houses are found or if a database error occurs.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=DictCursor)
        cursor.execute("""
            SELECT
                h.HouseID,
                h.AddressLine1,
                h.City
            FROM
                House h
            JOIN
                HouseUser hu ON h.HouseID = hu.HouseID
            WHERE
                hu.UserID = %s;
        """, (user_id,))
        houses = cursor.fetchall()
        if not houses:
            raise HTTPException(status_code=404, detail="No houses found for the specified user")
        return [dict(house) for house in houses]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        conn.close()

# Create a new HouseUser association (Create Operation)
@router.post("/")
def create_house_user(user_id: int, house_id: int):
    """
    Associate a user with a house (create relationship in HouseUser).
    Args:
        user_id (int): User ID to associate with the house.
        house_id (int): House ID to associate with the user.
    Returns:
        dict: Created HouseUser relationship.
    Raises:
        HTTPException: If there is a database error or the relationship already exists.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO HouseUser (UserID, HouseID)
            VALUES (%s, %s) RETURNING UserID, HouseID;
        """, (user_id, house_id))
        house_user = cursor.fetchone()
        conn.commit()
        conn.close()
        return dict(house_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Update an existing HouseUser association (Update Operation)
@router.put("/")
def update_house_user(user_id: int, house_id: int):
    """
    Update the association of a user with a house (if needed).
    Args:
        user_id (int): User ID to modify.
        house_id (int): House ID to modify.
    Returns:
        dict: Updated HouseUser relationship.
    Raises:
        HTTPException: If the relationship is not found or a database error occurs.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE HouseUser
            SET HouseID = %s
            WHERE UserID = %s RETURNING UserID, HouseID;
        """, (house_id, user_id))
        house_user = cursor.fetchone()
        if not house_user:
            raise HTTPException(status_code=404, detail="HouseUser association not found")
        conn.commit()
        conn.close()
        return dict(house_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Delete a HouseUser association (Delete Operation)
@router.delete("/")
def delete_house_user(user_id: int, house_id: int):
    """
    Remove a user from a house (delete HouseUser relationship).
    Args:
        user_id (int): User ID to dissociate from the house.
        house_id (int): House ID to dissociate from the user.
    Returns:
        dict: Deleted HouseUser relationship.
    Raises:
        HTTPException: If the relationship is not found or a database error occurs.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM HouseUser
            WHERE UserID = %s AND HouseID = %s RETURNING UserID, HouseID;
        """, (user_id, house_id))
        house_user = cursor.fetchone()
        if not house_user:
            raise HTTPException(status_code=404, detail="HouseUser association not found")
        conn.commit()
        conn.close()
        return dict(house_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
