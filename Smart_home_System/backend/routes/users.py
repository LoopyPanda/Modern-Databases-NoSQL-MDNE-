from fastapi import APIRouter, HTTPException
from backend.db.connection import get_db_connection

router = APIRouter()

# Fetch all users (Already present)
@router.get("/")
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users;")
        users = cursor.fetchall()
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return [dict(user) for user in users]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

# Fetch a single user by ID (Already present)
@router.get("/{user_id}")
def get_user(user_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT UserID, FirstName, LastName, Email FROM Users WHERE UserID = %s", (user_id,)
        )
        user = cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return dict(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

# Create a new user
@router.post("/")
def create_user(first_name: str, last_name: str, email: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (FirstName, LastName, Email) VALUES (%s, %s, %s) RETURNING UserID, FirstName, LastName, Email;",
            (first_name, last_name, email)
        )
        user = cursor.fetchone()
        conn.commit()
        return dict(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

# Update an existing user
@router.put("/{user_id}")
def update_user(user_id: int, first_name: str = None, last_name: str = None, email: str = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Prepare dynamic update query
        update_query = "UPDATE Users SET"
        values = []
        
        if first_name:
            update_query += " FirstName = %s,"
            values.append(first_name)
        if last_name:
            update_query += " LastName = %s,"
            values.append(last_name)
        if email:
            update_query += " Email = %s,"
            values.append(email)
        
        # Remove trailing comma and complete WHERE clause
        update_query = update_query.rstrip(",") + " WHERE UserID = %s RETURNING UserID, FirstName, LastName, Email;"
        values.append(user_id)
        
        cursor.execute(update_query, tuple(values))
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        conn.commit()
        return dict(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

# Delete an existing user
@router.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Users WHERE UserID = %s RETURNING UserID, FirstName, LastName, Email;",
            (user_id,)
        )
        user = cursor.fetchone()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        conn.commit()
        return dict(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()
