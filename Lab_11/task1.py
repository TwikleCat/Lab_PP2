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
    cur.callproc('search_phonebook', [pattern])
    for row in cur.fetchall():
        print(row)




def insert_or_update_user():
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    cur.execute("CALL proc(%s, %s)", (username, phone))
    conn.commit()
    print("User inserted/updated successfully.")


def insert_users():
    n = int(input("How many users do you want to insert? "))
    usernames = []
    phones = []

    for i in range(n):
        username = input(f"Enter username #{i+1}: ")
        phone = input(f"Enter phone for {username}: ")
        usernames.append(username)
        phones.append(phone)

    cur.execute(
        "select*from insert_users(%s::VARCHAR[], %s::VARCHAR[])",
        (usernames, phones)
    )
    invalids = cur.fetchall()

    if invalids:
        print("\nInvalid entries:")
        for user in invalids:
            print(f"Username: {user[0]}, Phone: {user[1]}")
    else:
        print("All users inserted successfully.")

    conn.commit()




def get_users_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    cur.callproc('paginate_phonebook', (limit, offset))
    for row in cur.fetchall():
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
        print("3. Insert many users")
        print("4. Paginated user list")
        print("5. Delete user by username or phone")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            pattern = input("Enter search pattern: ")
            print(search_contacts(pattern))
        elif choice == "2":
            insert_or_update_user()
        elif choice == "3":
            insert_users()
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
