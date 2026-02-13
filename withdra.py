path = input("Enter CSV path: ")

try:
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
except FileNotFoundError:
    print("File not found! Check the path.")
    exit()


headers = lines[0].strip().split(',')
print("CSV Headers:", headers)


print("\nMenu:")
print("1. Withdraw")
print("2. Enquiry")

ch = int(input("Enter your choice: "))


user_pin = input("Enter your PIN: ")

found = False


rows = [line.strip().split(',') for line in lines]


for i in range(1, len(rows)):
    name = rows[i][0]
    account = rows[i][1]
    pin = rows[i][2]
    balance = int(rows[i][3])

    if pin == user_pin:
        found = True
        print(f"\nWelcome {name}!")

        if ch == 1:
            # Withdraw
            print("Your current balance is:", balance)
            withdraw = int(input("Enter amount to withdraw: "))

            if withdraw > balance:
                print("Insufficient balance!")
            else:
                balance = balance - withdraw
                rows[i][3] = str(balance)  

                print("Amount withdrawn successfully!")
                print("Remaining balance:", balance)

                
                file = open(path, 'w')
                for row in rows:
                    file.write(",".join(row) + "\n")
                file.close()

                

        elif ch == 2:
            
            print("Your account balance is:", balance)

        else:
            print("Invalid choice!")

        break

if not found:
    print("Invalid PIN! No account found.")

