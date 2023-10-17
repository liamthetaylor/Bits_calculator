# puts series of symbols at start and end of text
def statement_generator(text, decoration):
    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    print()
    print(statement)
    print()
    return ""


# checks user choice is integer, image or text.
def user_choice():
    text_ok = ["text", "t", "txt"]
    image_ok = ["im", "image", "pic", "picture", "photo"]
    int_ok = ["int", "in", "integer", "#", "num", "number"]
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


# heading
statement_generator("Bit calculator for text, integers and images", "~")


# loop to allow multiple calculations
keep_going = ""
while keep_going == "":
    print("hi")
    