import bcrypt
import psycopg2


def hash_password(plain_text_password):
    # Generate a secure, random cryptographic salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt using intensive computing cycles
    hashed = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
    return hashed.decode('utf-8'), salt.decode('utf-8')


def register_user(username, password):
    hashed_pw, salt = hash_password(password)
    
    try:
        # Connect using internal system variables (bypasses network restrictions)
        conn = psycopg2.connect(
            dbname="secure_app",
            user="postgres",
            host="localhost"
        )
        cursor = conn.cursor()
        
        # PARAMETERIZED QUERY: This completely prevents SQL Injection attacks
        insert_query = """
        INSERT INTO user_credentials (username, password_hash, salt) 
        VALUES (%s, %s, %s);
        """
        cursor.execute(insert_query, (username, hashed_pw, salt))
        
        conn.commit()
        print(f" Success: User '{username}' registered securely!")
        
        cursor.close()
        conn.close()
        
    except Exception as error:
        print(f" Database Error: {error}")

#  Step 3: Test Run the Script
if __name__ == "__main__":
    print("--- Security Database Registration Test ---")
    test_user = input("Enter a test username: ")
    test_pass = input("Enter a test password: ")
    register_user(test_user, test_pass)
