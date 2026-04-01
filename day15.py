# 
# Password Check and Reset with Retry

saved_password = "Python123"

password = input("Enter your password: ")

if password == saved_password:
    print(" Password is correct. Access Granted!")

else:
    print("Incorrect Password.")

    choice = input("Do you want to reset password? (yes/no): ")

    if choice.lower() == "yes":

        while True:
            new_password = input("Enter new password: ")

            if len(new_password) >= 6:
                saved_password = new_password
                print(" Password reset successful!")

                # Login again
                password = input("Enter your new password again: ")

                if password == saved_password:
                    print(" Login Successful!")
                else:
                    print(" Password does not match.")

                break  # exit loop

            else:
                print("⚠️ Password too short! Use at least 6 characters.")

    else:
        print("Access Denied.")
