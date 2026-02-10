path = input("Enter CSV path: ")

file = open(path, 'r')
lines = file.readlines()
file.close()


key = lines[0].strip().split(',')

users = {}


for l in lines[1:]:
    value = l.strip().split(',')
    rowd = {}
    for i in range(len(key)):
        rowd[key[i]] = value[i]

    users[rowd["username"]] = {
        "password": rowd["password"],
        "status": rowd["status"]
    }

print("1. Register, 2. Login")
ch = int(input("Enter your choice: "))


if ch == 1:
    new_username = input("Enter new username: ")

    if new_username in users:
        print(" Username already exists!")
    else:
        new_password = input("Enter new password: ")
        status = "active"

        
        users[new_username] = {
            "password": new_password,
            "status": status
        }

        # Append to CSV file
        file = open(path, "a")
        file.write(f"\n{new_username},{new_password},{status}")
        file.close()

        print(" Registration successful! You can now login.")


elif ch == 2:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        if users[username]["password"] == password:
            if users[username]["status"] == "active":
                print(" Login successful! User is active.")
            else:
                print(" Account exists, but it is inactive.")
        else:
            print(" Wrong password.")
    else:
        print(" Username not found.")

else:
    print(" Invalid choice")



    
    