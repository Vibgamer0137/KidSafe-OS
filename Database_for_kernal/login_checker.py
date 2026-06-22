from hashmaker import hash_var
class PasswordChecker: 
    def password_initializer():
        password = None
        while True:
            password_type = int(input("What is your password type(1 for pin, 2 for password):"))
            if password_type == 1:
                print("Ok")
                password = input("Please Enter your pin:")
                password = hash_var.hashmaking(password)
                print("Done")
                return password
            elif password_type == 2:
                print("Ok")
                password = input("Please enter your password:")
                password = hash_var.hashmaking(password)
                print("Done")
                return password
            else:
                print("You entered wrong press 100 to escape or choose either 1 nor 2!!!")

    def password_checker(password_hashed):
        attempt = input("Enter whatever your pin or password:")
        while True:
            if attempt.isdigit():
                print("Your password type is pin")
                password_type = 1
                while True:
                    if hash_var.hashmaking(attempt) == password_hashed:
                        print("Attempt Succesfull")
                        return password_type
                    else:
                        print("Attempt Failed")

            else:
                print("Your password type is password")
                password_type = 2
                while True:
                    if hash_var.hashmaking(attempt) == password_hashed:
                        print("Attempt Succesfull")
                        return password_type
                    else:
                        print("Attempt Failed")

login = PasswordChecker()