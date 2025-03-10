<<<<<<< HEAD
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

# Getting database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# PostgreSQL connection
def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

# store user responses
def save_user_response(user_input, ai_recommendation):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_responses (user_input, ai_recommendation) VALUES (%s, %s)",
        (user_input, ai_recommendation)
    )
    conn.commit()
    cursor.close()
    conn.close()
=======
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

# Getting database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# PostgreSQL connection
def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

# store user responses
def save_user_response(user_input, ai_recommendation):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_responses (user_input, ai_recommendation) VALUES (%s, %s)",
        (user_input, ai_recommendation)
    )
    conn.commit()
    cursor.close()
    conn.close()
>>>>>>> master
