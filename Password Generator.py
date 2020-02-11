import random
import string
import winsound

def generate():
    """ Generates a random string of uppercase and lowercase letters, digits and punctuation to the given length """
    print("\u0332".join("Password Generator "))
    generate = True
    while generate == True:
        try:
            length = int(input("\n- How long should the password be: "))
            if length > 0:
                password = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation) for _ in range(length))
                print("Password: " + password)
                winsound.PlaySound("correct", winsound.SND_ASYNC)
            else:
                print("Invalid Length! Length must be above 0")
                continue

            while True: 
                #asks the user if they want to save their password
                save = str(input("\n- Would you like to save this password?\nPlease type 'yes' or 'no': ").casefold())
                
                #if the user answers 'yes' then the program appends the password into passwords.txt or creates the file if it doesn't exist.
                if save == 'yes':
                    with open("Passwords.txt", "a") as f:
                        f.write(f"{password}\n")
                        print("\nPassword saved to Passwords.txt")
                        break 
                        #breaks this loop and goes to the next loop which asks the user if they want to generate another

                elif save == 'no':
                    break
                    #breaks this loop and goes to the next loop without saving the password

                else:
                    print("Invalid Input. Please type 'yes' or 'no'.")
                    continue
                    #if the input is not yes or no, the user is told their input is invalid and the loop starts over so they can re-enter

            while True:
                retry = str(input("\n- Would you like to generate another password?\nPlease type 'yes' or 'no': ").casefold())
                #breaks this loop and returns to the generate loop if answer is yes
                if retry == 'yes':
                    break

                #closes the program if the user says no
                elif retry == 'no':
                    print("Closing Program.")
                    generate = False
                    break

                else:
                    print("Invalid Input. Please type 'yes' or 'no'.")
                    continue
                    #if the input is not yes or no, the user is told their input is invalid and the loop starts over so they can re-enter

        #Checks that password length is a valid number and if it is not, it returns to the start of the loop to ask again            
        except ValueError:
            print("Invalid Number")
            continue

generate()