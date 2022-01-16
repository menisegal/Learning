import exceptions

def check_input(username, password):

    if not str(username).isascii() or len(username) > 16 or len(username) < 3:
        raise exceptions.UsernameContainsIllegalCharacter(username)


    print ("OK")












if __name__ == "__main__":
    check_input("a", "dsadas")