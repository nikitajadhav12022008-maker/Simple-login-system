username = "admin"
password = "1234"

for i in range(3):
    u = input("username:")
    p = input("password:")
    if(u == username and p == password):
        print("Login successful!!!")
        break
else:
    print("Account locked...")