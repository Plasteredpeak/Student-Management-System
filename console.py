def Admin():
    login={"peep69":"pp"}
    u=input("enter userName: ")
    if u==login["peep69"]:
        p=input("enter password")
        if p in login:
            print("logged in")
        else:
            print("wrong password")
            while True:
                i=input("Try again? Y or N :").upper()
                if i=="Y":
                    Admin()
                    exit()
                elif i=="N":
                    main()
                else:
                    continue
    else:
        print("wrong Username")
        while True:
            i=input("Try again? Y or N :").upper()
            if i=="Y":
                Admin()
                exit()
            elif i=="N":
                main()
            else:
                continue
                
            
    
def main():
    print("***********WELCOME TO STUDENT MANAGMENT SYSTEM*************")
    while True:
        print("type A to access admin controls")
        print("type T to access teacher controls")
        print("type S to access student controls")
        In=input("enter: ").upper()
        if In=="A":
            Admin()
        elif In=="T":
            Teacher()
        elif In=="S":
            Student()
        else:
            print("invalid input")
        i=input("Access again? Y or N :").upper()
        if i =="N":
            exit()
        else:
            continue
main()

