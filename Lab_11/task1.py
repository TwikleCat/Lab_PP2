import psycopg2


conn = psycopg2.connect(
    host='localhost',
    dbname='Database',
    user='postgres',
    password='Pass@STU2015',
    port=1671
)
cur = conn.cursor()

def search_contacts(pattern):
     
    results = []
    try:
        cur.callproc('search_phonebook', (pattern,))
        row = cur.fetchone()
        while row is not None:
            results.append(row)
            row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")
    return results



def insert_or_update_user():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    cur.execute("CALL proc(%s, %s)", (username, phone))
    conn.commit()
    print("User inserted/updated successfully.")


def insert_many_users():
    usernames = input("Enter usernames (comma-separated): ").split(",")
    phones = input("Enter phones (comma-separated, same order): ").split(",")
    if len(usernames) != len(phones):
        print("Mismatch in number of usernames and phones.")
        return
    cur.execute("CALL insert_many_users(%s, %s)", (usernames, phones))
    conn.commit()
    print("Bulk insert completed. Check server for invalid data notice.")


def get_users_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM get_users_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_by_value():
    value = input("Enter username or phone to delete: ")
    cur.execute("CALL delete_user_by_value(%s)", (value,))
    conn.commit()
    print("User deleted if found.")


def main():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Search by pattern")
        print("2. Insert or update single user")
        print("3. Bulk insert many users")
        print("4. Paginated user list")
        print("5. Delete user by username or phone")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            pattern = input("Enter search pattern: ")
            results = search_contacts(pattern)
        elif choice == "2":
            insert_or_update_user()
        elif choice == "3":
            insert_many_users()
        elif choice == "4":
            get_users_paginated()
        elif choice == "5":
            delete_by_value()
        elif choice == "6":
            break
        else:
            print("Invalid option.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
