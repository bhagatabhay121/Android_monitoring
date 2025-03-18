from firebase import firebase
firebase = firebase.FirebaseApplication("https://chat-app-d2935-default-rtdb.firebaseio.com/", None)

data = firebase.get(f"chat-app-d2935-default-rtdb/admin/users/account", "")
print(data)



for i in data.keys():
    ak = i
    pr = data[i]["name"]

for i in range(len(data)):
    print(i)


np = i+1

print(f"{np} : {pr}")
username = int(input("Enter the choice: "))

if username == np:
    print("1. Block User")  
    print("2. Unblock User")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = firebase.put(f"chat-app-d2935-default-rtdb/admin/users/account/{ak}", "status", "blocked")
        print("User blocked successfully")
    elif choice == 2:
        data = firebase.put(f"chat-app-d2935-default-rtdb/admin/users/account/{ak}", "status", "active")
        print("User unblocked successfully")

