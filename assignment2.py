import crypt
import sys


def get_info():
    while True:
        print ("****____Welcome to the Password Cracker____****")
        print("/n")
        path = raw_input("Please Enter the file path of the shadow file. Primarily( /etc/shadow ) ")
        user = raw_input("Please Enter the user-name of user whose password you would like to crack. ")

        return path, user


if __name__ == '__main__':
    user_dataline = None
    path, user = get_info()
    path = open(path, 'r')
    path = path.readlines()

    # searches the lines within the file of the specific file path to look for the username

    for options in path:
         if user in options:
            user_dataline = options
            break

    # returned when the user is not inside the shadow file
    if user_dataline == None:
        print("The user was not found")
        print("Program Terminated")
        sys.exit()

    user_dataline.split(":")
    split_1 = user_dataline.split(":")[1]
    key = split_1.split("$")[3]
    salt = split_1.split("$")[2]
    """
    the shadow file line string is taken and split at each ":" and string inside index 1
    the "hash" and "salt" are then taken by spliting the first split by "$"
    and stored into the variable key and salt

    """

    dictionary = "dictionary.txt"
    dictionary = open(dictionary, 'r')
    dictionary = dictionary.readlines()
    indicator = "$6$"
    # the imported password dictionary is accessed and the data is then read line by line

    c = False
    for psswd in dictionary:
        if indicator + salt + '$' + key == (crypt.crypt(psswd.strip(), indicator + salt + "$")):
            print("Password was found : " + psswd)
            c = True

    if not c:
        print("Password not Found")
