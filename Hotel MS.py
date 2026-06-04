class hotelMS():
    def __init__(self):
        self.file="hotelmanage.txt"
    def add_guest(self):
        guest_id=input("Enter guest id:")
        guest_name=input("enter guest name:")
        room_number=input("enter room number:")
        num_of_days=input("enter number of days:")
        try:
            with open(self.file,"r") as f:
                hotels=f.readlines()
        except:
            hotels=[]
        for hotel in hotels:
            if hotel.strip()=="":
                continue
            i,n,r,d=hotel.strip().split(",")
            if i==guest_id:
                print("GUEST ID ALREADY EXIST")
                return
            if r==room_number:
                print("ROOM ALREADY BOOKED")
                return
        with open(self.file,"a") as f:
            f.write(guest_id+","+guest_name+","+room_number+","+num_of_days+"\n")
        print("GUEST ADDED")
    def view_guest(self):
        with open(self.file,"r") as f:
            hotels=f.readlines()
        if not hotels:
            print("GUEST LIST IS EMPTY")
            return
        print("GUEST LIST")
        for hotel in hotels:
            if hotel.strip()=="":
                continue
            i,n,r,d=hotel.strip().split(",")
            print("\nGuest id:",i,
                  "\nGuest name:",n,
                  "\nRoom number:",r,
                  "\nNumber of days:",d,"\n")
            found=True
    def search_guest(self):
        guest_id=input("Enter guest id:")
        with open(self.file,"r") as f:
            hotels=f.readlines()
        found=False
        for hotel in hotels:
            if hotel.strip()=="":
                continue
            i,n,r,d=hotel.strip().split(",")
            if i==guest_id:
                print("\nGuest id:",i,
                  "\nGuest name:",n,
                  "\nRoom number:",r,
                  "\nNumber of days:",d,"\n")
                found=True
        if not found:
            print("INVALID GUEST ID")
    def update_guest(self):
        guest_id=input("Enter guest id:")
        guests_name=input("enter guest name:")
        rooms_number=input("enter room number:")
        numb_of_days=input("enter number of days:")
        with open(self.file,"r") as f:
            hotels=f.readlines()
        update=[]
        found=False
        for hotel in hotels:
            if hotel.strip()=="":
                continue
            i,n,r,d=hotel.strip().split(",")
            if i==guest_id:
                update.append(str(guest_id)+","+guests_name+","+rooms_number+","+str(numb_of_days)+"\n")
                found=True
            else:
                update.append(hotel)
        with open(self.file,"w") as f:
            f.writelines(update)
        if found:
            print("GUEST DETAILS UPDATED")
        else:
            print("INVALID GUEST ID")
    def delete_guest(self):
        guest_id=input("Enter guest id:")
        with open(self.file,"r") as f:
            hotels=f.readlines()
        delete=[]
        found=False
        for hotel in hotels:
            if hotel.strip()=="":
                continue
            i,n,r,d=hotel.strip().split(",")
            if i==guest_id:
                found=True
            else:
                delete.append(hotel)
        with open (self.file,"w") as f:
            f.writelines(delete)
        if found:
            print("GUEST DETAILS DELETED")
        else:
            print("INVALID GUEST ID")
system=hotelMS()
while True:
    print("\n HOTEL MANAGEMENT SYSTEM")
    print("1.add guest")
    print("2.view guest")
    print("3.search guest")
    print("4.update guest")
    print("5.delete guest")
    print("6.EXIT")
    choice=input("enter your choice:")
    if choice=="1":
        system.add_guest()
    elif choice=="2":
        system.view_guest()
    elif choice=="3":
        system.search_guest()
    elif choice=="4":
        system.update_guest()
    elif choice=="5":
        system.delete_guest()
    
    elif choice=="6":
        print("------------EXITING HOTEL MANAGEMENT SYSTEM------------------")
        break
    else :
        print("invalid choice :(")
            
        
        
            
        
            
        
        
            
        
            
