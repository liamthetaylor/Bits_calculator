# functions go here

# puts series of symbols at start and end of text
def statement_generator(text, decoration):
    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    print()
    print(statement)
    print()
    return ""


# Checks user choice is text, integer or image
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


def integer_checker(question, low):
    valid = False
    while not valid:
        error = "Please enter an integer that is more than 0" "or (equal to) {}".format(low)
        try:
            response = int(input(question))
            if response >= low:
                return response
            else:
                print()
                print(error)
                print()
        except ValueError:
            print()
            print(error)
            print()

    print()
    print("The integer you have chosen is", response)
    print()
    loop = input("press <enter> to rerun, any other key to finish: ")
    print()

# main routine goes here

# heading
statement_generator("Bit calculator for text, integers and images", "~")

# display instructions if it is users first time

# loop to allow multiple calculations
keep_going = ""
while keep_going == "":

    # Ask user for file type
    data_type = user_choice()
    print()
    print("You chose", data_type)
    print()

    
    # For integers, ask user for integer
    # (must be integer more / equal to 0)

    # For images, ask user for width and height
    # (must be integer more / equal to 1)
