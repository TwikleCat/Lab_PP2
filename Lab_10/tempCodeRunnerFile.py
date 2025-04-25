import psycopg2
import csv

conn = psycopg2.connect(
    host = 'localhost',
    dbname = 'Database',
    user = 'postgres',
    password = 'Pass@STU2015',
    port = 1671  
)
cur = conn.cursor()


def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            phone VARCHAR(15) NOT NULL
        )
    ''')
    conn.commit()


def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()


def insert_from_csv():
    file_path = "contacts.csv"
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data inserted from CSV.")

def update_user():
    old_username = input("Enter existing username to update: ")
    new_username = input("Enter new username (leave blank to keep unchanged): ")
    new_phone = input("Enter new phone (leave blank to keep unchanged): ")
    if new_username:
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_username, old_username))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, new_username or old_username))
    conn.commit()
    print("Update completed.")

def query_users():
    print("1. All users\n2. Filter by username\n3. Filter by phone")
    choice = input("Choose filter: ")
    if choice == "1":
        cur.execute("SELECT * FROM phonebook")
    elif choice == "2":
        value = input("Enter username: ")
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (value,))
    elif choice == "3":
        value = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (value,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_user():
    print("1. By username\n2. By phone")
    choice = input("Choose delete option: ")
    value = input("Enter value: ")
    if choice == "1":
        cur.execute("DELETE FROM phonebook WHERE username = %s", (value,))
    elif choice == "2":
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (value,))
    conn.commit()
    print("Delete completed.")


def main():
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update user")
        print("4. Query users")
        print("5. Delete user")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_users()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
