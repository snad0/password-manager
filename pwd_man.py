from cryptography.fernet import Fernet
# generating an encryption key 
# def write_key():
    # key= Fernet.generate_key()
    # with open("key.key","wb") as key_file:
        # key_file.write(key)
# write_key()

# taking key from key.key 
def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key

key= load_key()
fer= Fernet(key)

#  view function 
def view():
    with open("password.txt","r") as f:
        for lines in f.readlines():
            data=lines.rstrip()
            #used rstrip here to strip off the new line
            user,passw=data.split(":")
            print(f"username: {user} | password: {fer.decrypt(passw.encode()).decode()}")

# add function          
def add():
    name=input("Username: ")
    pwd=input("Enter Password: ")
    with open("password.txt",'a') as f:
        f.write(name +":" + fer.encrypt(pwd.encode()).decode() + "\n")



#  main program       

master_pwd= input("What is the master password : ")
def main():
    while True:
        mode=input("Would you like to add a new password or view existing ones(view,add)?, or press q to quit  ").lower()
        if mode =="q":
            break
        elif mode== "view":
            view()
        elif mode=="add":
            add()
        else:
            print("invalid input")
            continue

if master_pwd=="Nad@123":
    main()
else:
    print("wrong password")


