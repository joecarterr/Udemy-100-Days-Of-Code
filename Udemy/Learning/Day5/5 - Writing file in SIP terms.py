def account_creation(f_name, l_name):
    if f_name == "" or l_name == "" or f_name == " " or l_name == " ":
        # if the user has not yet set a first or last name it will skip and go onto their account creation
        return "You didn't enter a first or last name"  # this will completely skip the function and go onto what's
        # after it
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print(formatted_f_name + ' ' + formatted_l_name)


account_creation(f_name=input("Please enter your first name:\n"),
                 l_name=input("Please enter your last name:\n"))
