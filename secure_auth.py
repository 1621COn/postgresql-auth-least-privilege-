import bcrypt
import psycopg2

def login_user(username, input_password):
    try:
        
        conn = psycopg2.connect(
            dbname="secure_app",
            user="low_priv_user",
            host="localhost"
        )
        cursor = conn.cursor()
        
       
        query = "SELECT password_hash FROM user_credentials WHERE username = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if result:
            # Fetch the stored hash from the database
            stored_hash = result[0].encode('utf-8')
            
            # Check if the input password matches the secure stored hash
            if bcrypt.checkpw(input_password.encode('utf-8'), stored_hash):
                print("[SUCCESS]: Authentication successful. Access Granted.")
                return True
            else:
                print(" [DENIED]: Invalid password. Access Blocked.")
                return False
        else:
            print("[DENIED]: Username not found.")
            return False
            
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    print("--- Secure Login Verification Interface ---")
    user = input("Username: ")
    password = input("Password: ")
    login_user(user, password)
