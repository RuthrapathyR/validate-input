#to validate user input without error it makes program user friendly
def validate_input(prompt="enter the value:",error_msg="check your input!"):
    """
    author:ruthrapathy
    prompt:you can enter user input mssg
    eroor_msg:you can enter error message
    """
    while True:
        try:
            u=int(input(prompt))
            return u
        except:
            print(error_msg)
            
