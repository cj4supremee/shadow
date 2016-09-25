import crypt



def get_info():
    while True:
        
        path = raw_input("Please Enter the file path of the shadow file.")
        user =raw_input("Please Enter the name of user you would like to crack ")

        return path, user




if __name__ == '__main__':
    user_dataline= None
    path, user= get_info()
    path=open(path,'r')
    path=path.readlines()

# searches the lines within the file of the specific file path to look for the username
   
    for options in path:
 
        if user in options:
            user_dataline=options
            break
# returned when the user is not inside the shadow file
    if user_dataline==None:
        print("The user was not found")


    user_dataline.split(":")
    split_1= user_dataline.split(":")[1]
    key=split_1.split("$")[3]
    salt=split_1.split("$")[2]


    dictionary= "dictionary.txt"
    dictionary=open(dictionary, 'r')
    dictionary=dictionary.readlines()
    indicator="$6$"
    c=False
    for psswd in dictionary:
        """  
        if psswd=="apple":
            print indicator+salt+'$'+key
            print(crypt.crypt(psswd, indicator+salt+"$")) 
        """
        if indicator+salt+'$'+key == (crypt.crypt(psswd.strip(), indicator+salt+"$")):
            print("Password was found"+psswd)
            c=True

    if not c:
        print("Password not Found")










