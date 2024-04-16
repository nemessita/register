# Python SQL vasitəsilə Register app qurun

# Proqram soruşur:
   
#     Daxil edin :
#         username,first_name,last_name,email,password
#         Daxil edilmiş məlumatlar databazaya otursun

# Qeyd:

# Password daxil edildikdə əlavə təsdiq passwordu soruşsun əgər 2 password bir-birinə uymursa error mesajı qaytarsın
# Təkrar emailin databazaya oturmasının qarşısını alın
# Bazada mövcud olan email təkrar daxil edildikdə error mesajı qaytarsın
# Password və Email düzgün daxil edilmədikdə proqram sonlanmadan yenidən soruşsun
# Password databazaya təhlükəsizliyə görə şifrələnmiş şəkildə düşsün
# Hər şey qaydasındadırsa success mesajı qaytarsın və məlumatlar databazaya otursun

import sqlite3
import getpass

db = sqlite3.connect("register.db")
sql = db.cursor()

# sql.execute('''CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT NOT NULL, 
#                 password TEXT NOT NULL,
#                 re_password TEXT NOT NULL,
#                 email TEXT NOT NULL UNIQUE,
#                 first_name TEXT,
#                 last_name TEXT
#             )''')
# db.commit()

def check_email(email):
    try:
        sql.execute("SELECT * FROM users WHERE email = ?", (email,))
        result = sql.fetchone()
        if result:
            print("Error_email artiq qeydiyyat olub")
            return True
        else:
            return False
    except sqlite3.Error as e:
        print(f"Error_unkialiq yoxlana bilmedi: {e}")
        return True

def register_user():
    username = input("username: ").strip()
    password = getpass.getpass("password: ").strip()
    re_password = getpass.getpass("password again: ").strip()
    email = input("email: ").strip()
    first_name = input("first name: ").strip()
    last_name = input("last name: ").strip()

    if password != re_password:
        print("Error_Sifreler uygun deyil.")
        return

    if check_email(email):
        return

    sql.execute("INSERT INTO users (username, password, re_password, email, first_name, last_name) VALUES (?, ?, ?, ?, ?, ?)",
                (username, password, re_password, email, first_name, last_name))
    db.commit()
    print("Registration successful!")

def main():
    # create_table()
    while True:
        choice = input("Secim: 1) Qeydiyyatdan kecin (2) Cixish:: ").strip()
        
        if choice == "1":
            register_user()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("yalnis 1 ve ya 2 secin.")

if __name__ == "__main__":
    main()

db.close()
