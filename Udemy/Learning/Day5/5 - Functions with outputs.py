def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print(formatted_f_name + ' ' + formatted_l_name)


format_name(f_name=input("Please enter your first name:\n"),
            l_name=input("Please enter your last name:\n"))
