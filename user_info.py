import vaccine_info

class virus_info:
    def ALPHA():
        LIFE=100
    def BETA():
        LIFE=100
    def GAMMA():
        LIFE=200
    def SIGMA():
        LIFE=250
    def random_durablity():
        print("write something..")

#user info class
class user_info(vaccine_info,virus_info):

    def __init__(self):
        print("Welcome to the Portal")
        self.select_option()

    def select_option(self):
        print("Please Select Your option")
        print(" 1.New User")
        print(" 2.Existing Patient")
        print(" 3.Exit")
        n=int(input())
        if(n==1):
            self.new_user()
        elif(n==2):
            self.existing_patient()
        else:
            print("Exit")

    def new_user(self):
        username=input("Enter Username:")
        Aadhar_Number=int(input("Enter Aadhar Number:"))
        print("Choose Your Vaccine")
        print(" 1. Covishield")
        print(" 2. Covaxin")
        print(" 3. Pfizer")
        print(" 4. Sputnik")
        vaccine_name=input()

        print("Patient has been registered")
        print("Username - ",username)
        print("Aadhar Number - ",Aadhar_Number)
        print("Vaccine Opted - ",vaccine_name)
        self.select_option()

    def existing_patient(self):
        username_check=input("Enter Username:")
        print("Verifying...")
        if(username_check==username):#variable from another function
            print("Welcome ", username_check)
            print("Patient Found !")
            print("You're being tested for the 1st Wave for the Alpha variant of the virus :") #can create a function here
            print( "Vaccine's BOOST : 10 | Vaccine's DURABLITY : ",virus_info.ALPHA,"| Virus's LIFE : |Virus Variant : ")
            self.vaccine_test()
        else:
            print("Patient not found!!! If you haven't registered yet then please register first.")
            self.select_option()

        
    def vaccine_test():
        print()

    
