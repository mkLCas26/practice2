def login_authentication():
    # Setting the Credentials
    username = input("Set your username: ")
    password = input("Set your password: ")

    print("Credentials have been set! You may now Log in.")

    # For Max Log in Attempts
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        entered_username = input("Enter Username: ")
        entered_password = input("Enter Password: ")

    # Checking the Credentials
        if entered_username == username and entered_password == password:
            print ("Login successful!")
            break
        else:
            attempts += 1
        if attempts < max_attempts:
            print ("Incorrect username or password. Try again.")
        else:
            print ("Too many failed attempts. Access denied.")
    
# Output
login_authentication ()