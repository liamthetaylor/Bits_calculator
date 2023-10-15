text_ok = ["text", "t", "txt"]
image_ok = ["im", "image", "pic", "picture", "photo"]
int_ok = ["int", "in", "integer", "#", "num", "number"]


def user_choice():
    valid = False
    while not valid:
        response = input("File type (integer / text / image): ").lower()
        if response in text_ok:
            return "text"
        elif response in image_ok:
            return "image"
        elif response in int_ok:
            return "integer"
        elif response == "i":
            want_int = input("press <enter> to get integer, any other key to get image.")
            if want_int == "":
                return "integer"
            else:
                return "image"
        else:
            print()
            print("Please choose valid file type.")
            print()


keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print()
    print("You chose", data_type)
    print()
