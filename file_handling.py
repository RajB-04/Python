import os 

dir_name = input("Enter a name of dir: ")
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
f_name = input("Enter a name of the file: ")
file_path = os.path.join(dir_name, f_name)


def write_file():
    with open(f"{file_path}.txt", "wt") as f:
        sr_no = 1
        while True:
            inp = input("Enter name of member and fees_paid as Name - fees, \n and 'quit' to exit: ").split('-')
            if inp[0].strip().isalpha() and inp[1].strip().isdigit():
                name = inp[0].strip().capitalize()
                fees = int(inp[1].strip())
                if len(name) < 15:
                    name += " " * (15 - len(name))
                f.write(f"{sr_no}. {name} ---------> {fees} \n")
                sr_no += 1
            
            elif inp[0].strip().casefold() == 'quit':
                break
            
            else:
                print("Invalid Input")

write_file()
