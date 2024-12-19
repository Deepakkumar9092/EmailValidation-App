email = input("Enter Your Email Address: ")
k, j, d = 0, 0, 0

if len(email) >= 6:  # Rule 1: Length should be at least 6
    if email[0].isalpha():  # Rule 2: First character must be a letter
        if ("@" in email) and (email.count("@") == 1):  # Rule 3: Only one "@" allowed
            if email[-4:] == ".com" or email[-3:] == ".in":  # Rule 4: Ends with valid domain
                for i in email:
                    if i.isspace():  # Check for spaces
                        k = 1
                    elif i.isalpha():
                        if i.isupper():  # Check for uppercase letters
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in "_@.":
                        continue
                    else:  # Invalid character
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email Address 5")
                else:
                    print("Valid Email Address")
            else:
                print("Wrong Email Address 4: Invalid domain")
        else:
            print("Wrong Email Address 3: Invalid '@'")
    else:
        print("Wrong Email Address 2")
else:
    print("Wrong Email Address 1")
