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
        error = "Please enter an integer that is more than (or equal to) {}".format(low)
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


def text_bits():
    print()
    var_text = input("Please enter some text: ")
    var_length = len(var_text)
    num_bits = 8 * var_length
    print()
    print("\'{}\' has {} characters...".format(var_text, var_length))
    print("Number of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent '{}'".format(num_bits, var_text))
    print()
    return ""


def image_bits():
    image_height = integer_checker("Image height: ", 1)
    image_width = integer_checker("Image width: ", 1)
    num_pix = image_height * image_width
    num_bits = num_pix * 24
    print()
    print("Number of pixels is {} x {} = {}".format(image_height, image_width, num_pix))
    print("Number of bits is {} x 24 = {}".format(num_pix, num_bits))
    print()
    return ""


def integer_bits():
    var_int = integer_checker("Please enter an integer: ", 0)
    var_bin = "{0:b}".format(var_int)
    num_bits = len(var_bin)
    print()
    print("{} in binary is {}".format(var_int, var_bin))
    print("The number of bits in {} is {}".format(var_int, num_bits))
    print()

    return ""

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
    if data_type == "integer":
        var_integer = integer_checker("Enter an integer: ", 0)
        print()

    # For images, ask user for width and height
    # (must be integer more / equal to 1)
    elif data_type == "image":
        image_width = integer_checker("image width: ", 1)
        print()
        image_height = integer_checker("image height: ", 1)
        print()

integer_bits()

text_bits()

image_bits()
