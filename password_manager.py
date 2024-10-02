# from tkinter import *

# window = Tk()
# window.title('Password manager')
# window.config(padx=50, pady=50)

# canvas = Canvas(width=200, height=200)
# logo_img = PhotoImage(file=r"C:\Users\2309824\OneDrive - Cognizant\Documents\Python\Python_Projects\password_manager\images.png")
# canvas.create_image(100, 100, image=logo_img) 
# canvas.pack()

# window.mainloop()

import string
import random

    
def generate_pass():
                all_letters = string.ascii_letters
                nums = string.digits

                letters = list(all_letters)
                numbers = list(nums)
                sp_chars = ['!', '@', '#', '$', '%', '&', '*']
                chars = []
                
                for i in range(random.randrange(8, 11)):
                    alp = random.choice(letters)
                    chars.append(alp)
                
                for i in range(random.randrange(2, 4)):
                    sym = random.choice(sp_chars)
                    chars.append(sym)

                for i in range(random.randrange(2,4)):
                    nm = random.choice(nums)
                    chars.append(nm)

                random.shuffle(chars)

                password = "".join(chars)

                flag = False
                for i in password:
                    if i.isupper():
                        flag = True
                        break
                
                if flag:
                    return password
                else:
                    return generate_pass()


def add():
    site_name = input()
    with open('password_manager\manage_passwords.txt', "at") as f:
        if site_name:
             password = generate_pass()
             print(password)
             f.write(f"{site_name} ----> {password} \n")

add()
        
            

