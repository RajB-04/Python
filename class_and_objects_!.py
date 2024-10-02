class Gym:

    fees = {}
    gym_members = {}
    count = 0

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner 
        Gym.count += 1

    def set_fees(self):
        for i in range(4):
            inp = input("Enter months and fees: ").split()
            if inp[0].strip().isdigit() and inp[1].strip().isdigit():
                Gym.fees[inp[0].strip()] = inp[1].strip()
            else:
                print("Enter a valid input.")

    def get_fees(self):
        print(self.fees)



    def add_members(self):
        while True:
            member = input("Enter a name of member with gym package: ").split()
            if member[0].strip().isalpha() and member[1].strip().isdigit():
                self.gym_members[member[0]] = member[1]
            elif member[0].strip().casefold() == 'quit':
                break
            else:
                print("Enter a valid name and months")
        
    def remove_member(self):
        member = input("Enter a member name: ")
        mem = member.strip()
        if member.strip().isalpha():
            if member.strip().lower() in self.gym_members.keys():
                del self.gym_members[member.strip()]
                print(f"The {mem} removed from gym successfully")

            else:
                print(f"The {mem} name dosen't exist in gym.")
        else:
            print("Enter a valid name")

    def get_members(self):
        return self.gym_members


# g = Gym("Realsteel", "Gattya")

# print(g.owner, g.name)
# g.set_fees()
# g.add_members()

class Member(Gym):

    def __init__(self, name, owner, mem_name, month, fee):
        super().__init__(name, owner)
        self.mem_name = mem_name
        self.month = month
        self.fee = fee

        
    def val_fees(self):
        if str(self.month) in Gym.fees.keys():
            if Gym.fees[str(self.month)] == str(self.fee):
                return True
            else:
                return False
        else:
            return False
     
    def pay_fees(self):
        if self.val_fees():
            return True
        else:
            return False
        
    def join_gym(self):
        if self.pay_fees():
            self.gym_members[self.mem_name] = f"{self.month}"
            return True
        else:
            return False
        
y = Member("Realsteel", "Gattya", "Yuvraj", 3, 2800)
z = Member("Realsteel", "Gattya", "Mohak", 6, 3000)

y.set_fees()
y.get_fees()
print(y.name, y.owner, y.mem_name)
print(y.get_members())

print(y.val_fees())
print(y.pay_fees())
print(y.join_gym())
print(z.join_gym())
print(y.get_members())
print(Gym.count)
