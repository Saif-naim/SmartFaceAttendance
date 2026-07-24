from database.db import get_connection

def main():
    try:
        conn = get_connection()
        print("✅ Database Connected Successfully!")
        conn.close()
    except Exception as e:
        print("❌ Database Connection Failed")
        print(e)

if __name__ == "__main__":
    main()