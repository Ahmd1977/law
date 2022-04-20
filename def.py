equations ={"static_energy", "mechanic_energy", "dynamic_energy", "dynamic_energy1", "density"}
while equations == equations:
    equations = input("Which equation? static_energy, mechanic_energy, dynamic_energy, dynamic_energy1 or density?").lower()
    if equations=="static_energy":
        weight=input("weight =")
        height=input("height =")
        

        def static_energy(weight,height):
            g=10
            weight = int(weight)
            height = int(height)
            return weight*g* height
        print("static_energy=",static_energy(weight,height))
        
    
    elif equations=="mechanic_energy":
        static_energy=input("static_energy =")
        dynamic_energy=input("dynamic_energy =")

        def mechanic_energy(static_energy,dynamic_energy):
            static_energy = int(static_energy)
            dynamic_energy = int(dynamic_energy)
            return static_energy + dynamic_energy
        print("mechanic_energy=",mechanic_energy(static_energy,dynamic_energy))
    
    elif equations=="dynamic_energy":
        mechanic_energy=input("mechanic_energy =")
        static_energy=input("static_energy =")
        def dynamic_energy(mechanic_energy,static_energy):
            mechanic_energy = int(mechanic_energy)
            static_energy = int(static_energy)
            return mechanic_energy-static_energy 
        print("dynamic_energy=", dynamic_energy(mechanic_energy,static_energy))
    
    elif equations=="dynamic_energy1":
        weight=input("weight =")
        velocity=input("velocity =")
        def dynamic_energy1(weight,velocity):
            weight = int(weight)
            velocity = int(velocity)
            return 0.5*weight* (velocity**2)
        print("dynamic_energy=", dynamic_energy1(weight,velocity))

    elif equations=="density":
        weight=input("weight =")
        volume=input("volume =")

        def density(weight,volume):
            weight = int(weight)
            volume = int(volume)
            return weight / volume
        print("density=",density(weight,volume))    
    else:
        print("Wrong enterance, please try again")
        
    
    
    




    
    
    
    
    