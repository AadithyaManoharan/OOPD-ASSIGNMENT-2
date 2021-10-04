import random

class wave:
    wave1_number=1
    wave1_durability=100
    wave1_name="ALPHA"
    wave2_number=2
    wave2_durability=150
    wave2_name="BETA"
    wave3_number=3
    wave3_durability=200
    wave3_name="GAMMA"
    wave4_number=4
    wave4_durability=250
    wave4_name="SIGMA" 

class vaccine_info:
    Covishield_Inject=10
    Covishield_Effect=10
    Covaxin_Inject=5
    Covaxin_Effect=5
    Pfizer_Inject=6
    Pfizer_Effect=4
    Sputnik_Inject=4
    Sputnik_Effect=8

class virus_info(wave):
    ALPHA_LIFE=100
    BETA_LIFE=100
    GAMMA_LIFE=200
    SIGMA_LIFE=250

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
        self.username=input("Enter Username:")
        Aadhar_Number=int(input("Enter Aadhar Number:"))
        print("Choose Your Vaccine")
        print(" 1. Covishield")
        print(" 2. Covaxin")
        print(" 3. Pfizer")
        print(" 4. Sputnik")
        vaccine_number=int(input())
        if(vaccine_number==1):
            self.vaccine_name="Covishield"
        elif(vaccine_number==2):
            self.vaccine_name="Covaxin"
        elif(vaccine_number==3):
            self.vaccine_name="Pfizer"
        elif(vaccine_number==4):
            self.vaccine_name="Sputnik"

        print("Patient has been registered")
        print("Username - ",self.username)
        print("Aadhar Number - ",Aadhar_Number)
        print("Vaccine Opted - ",self.vaccine_name)
        self.select_option()

    def existing_patient(self):
        username_check=input("Enter Username:")
        print("Verifying...")
        if(username_check== self.username):#variable from another function
            print("Welcome ", username_check,",")
            print("Patient Found !")
            print("You're being tested for the 1st Wave for the Alpha variant of the virus :") #can create a function here
            self.test(0,0,1,1)
        else:
            print("Patient not found!!! If you haven't registered yet then please register first.")
            self.select_option()
    
    temp=0
    def test(self,local_life,local_durability,local_wave_number,factor_attack):
        #add parameter to add wave
        
        if(self.vaccine_name=="Covishield"):
                inject=vaccine_info.Covishield_Inject
                effect=vaccine_info.Covishield_Effect
        elif(self.vaccine_name=="Covaxin"):
                inject=vaccine_info.Covaxin_Inject
                effect=vaccine_info.Covaxin_Effect
        elif(self.vaccine_name=="Pfizer"):
                inject=vaccine_info.Pfizer_Inject
                effect=vaccine_info.Pfizer_Effect
        elif(self.vaccine_name=="Sputnik"):
                inject=vaccine_info.Sputnik_Inject
                effect=vaccine_info.Sputnik_Effect

        if(self.temp==0):
            if(local_wave_number==1):
                local_name=wave.wave1_name
                local_life=virus_info.ALPHA_LIFE
                local_durability=wave.wave1_durability
                factor_attack=0.25*local_life
            if(local_wave_number==2):
                local_name=wave.wave2_name
                local_life=virus_info.BETA_LIFE
                local_durability=wave.wave2_durability
                factor_attack=0.25*local_life
            if(local_wave_number==3):
                local_name=wave.wave3_name
                local_life=virus_info.GAMMA_LIFE
                local_durability=wave.wave3_durability
                factor_attack=(1/3)*local_life
            if(local_wave_number==4):
                local_name=wave.wave4_name
                local_life=virus_info.SIGMA_LIFE
                local_durability=wave.wave4_durability
                factor_attack=0.5*local_life

            print( "Vaccine's BOOST : ",10*local_wave_number ,"| Vaccine's DURABLITY : ", local_durability,"| Virus's LIFE :",local_life, "|Virus Variant : ",local_name)
            self.temp=1
        
        print("Please select an option ")
        print(" 1.INJECT")
        print(" 2.EFFECT")
        print(" 3.EXIT")
        n=int(input())
        if(n==1):
            print("Your vaccine is boosted and it reduces the life of the virus by" ,inject)
            local_life=local_life-inject
            print("Vaccine DURABILITY : ",local_durability,"|Virus's LIFE: ",local_life)
            if(local_life>0):
                print("Virus's ACTION !")
            elif (local_life==0):
                print()
                print("Virus Defeated !")
                print("Vaccine proves to be effective during the wave",local_wave_number,"!!!")
                print("Moving on to the next wave.")
                self.temp=0
                local_wave_number+=1
                if(local_wave_number<5):
                    self.test(0,0,local_wave_number,1)
                else:
                    print("You have defeated all Known Virus Variants!! Stay Safe!! Stay Tuned for the next Variant!!!")

            #random_var= random.randint(1,factor_attack)
            random_var= random.randint(1,10)
            print("Virus reduces the vaccine DURABILITY by",random_var)
            local_durability=local_durability-random_var
            if(local_durability>0):
                print("Vaccine DURABILITY :" , local_durability,"|Virus's LIFE: ",local_life)
            else:
                 print("Vaccine DURABILITY : 0 |Virus's LIFE: ",local_life)

            if(local_durability<=0 and local_life!=0):
                print("Oops!Your vaccine fails to affect the ALPHA Variant.")
                print("However, The vaccine helps you fight against several attacks of the virus and proves to be useful. This shows how important the vaccine is in the fight against COVID-19.")
                print("Thanks for your participation. Now Let's get Vaccinated !!!")
            else:
                self.test(local_life,local_durability,local_wave_number,factor_attack)
            
    
        elif(n==2):
            print("Virus's action reduced by ",effect)
            print("Vaccine DURABILITY :" , local_durability,"|Virus's LIFE: ",local_life)
            print("Virus's ACTION !")
            print("Virus reduces the vaccine DURABILITY by 0")
            print("Vaccine DURABILITY :" , local_durability,"|Virus's LIFE: ",local_life)
            self.test(local_life,local_durability,local_wave_number,factor_attack)
        
        else:
            print("Exited at Wave",local_wave_number)
            print("Thanks for your participation. Let's get Vaccinated !!!")

 
if __name__ =="__main__":
    obj1=user_info()
            