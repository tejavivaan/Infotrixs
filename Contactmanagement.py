from joblib import load, dump

class Contacts:
    def __init__(self):
        self.dic = dict()

    def add_contact_details(self):
        try:
            self.dic = load(open("contacts.pkl", "rb"))
        except FileNotFoundError:
            self.dic=dump({},open("contacts.pkl","wb")) 
        except EOFError:
            pass       
        sample = dict()
        first_name = input("\nEnter Contact First Name: ")
        last_name = input("\nEnter Contact Last Name: ")
        key = first_name + "_" + last_name
        phno = input("\nEnter Phone Number: ")
        sample["First Name"] = first_name
        sample["Last Name"] = last_name
        sample["Phone Number"] = phno
        yn = input("\nDo you want to add EMAIL ID (yes/no):")
        if yn == "yes":
            email = input("\nEnter Email Id: ")
            sample["Email Id"] = email
        else:
            sample["Email Id"] = ""
        while 1:
            que=input("\nDo you want to add any other Field(yes/no): ")
            if que.lower()=="yes":
                flname=input("\nEnter the Field Name: ")
                value1=input("\nEnter the value: ")
                sample[flname]=value1
            if que.lower()=="no":
                break
        self.dic[key] = sample
        print("Contact",key,"created")
        dump(self.dic, "contacts.pkl")
        open("contacts.pkl", "rb").close()

    def view_all_contacts(self):
        try:
            x = load(open("contacts.pkl", "rb"))
            print("Contact Name\t Phone Number")
            for k in x:
                print(k,"\t",x[k]["Phone Number"])
            open("contacts.pkl", "rb").close()
        except EOFError:
            print("\nNo contacts in the list")
    
    def view_by_contactname(self):
        try:
            
            l=[]
            x = load(open("contacts.pkl", "rb"))
            contact_name=input("\nEnter Contact Name to be Searched: ")
            count=0
            print("\nThese are the Contact names For given name: ")
            print("\nSno\tContact Name\t Phone Number")
            for k in x:
                if contact_name.lower() in k.lower():
                    count+=1
                    print(count,"\t",k,"\t",x[k]["Phone Number"])
                    l.append(k)
            cno=int(input("\nIf you want to view the contact enter Serial no or else enter '0': "))
            if cno==0:
                print("\nRETURNING TO MAIN MENU")
            else:
                cdet=x[l[cno-1]]
                print("\nContact Name:\t",l[cno-1])
                for det in cdet:
                    print("\n",det,":\t",cdet[det])

            open("contacts.pkl", "rb").close()
        except EOFError:
            print("\nNo contacts in the list")
        
    def update_details(self):
        try:
            contact_name=input("\nEnter Contact Name to be Updated: ")
            l=[]
            x = load(open("contacts.pkl", "rb"))
            count=0
            print("\nThese are the Contact names For given name: ")
            print("\nSno\tContact Name\t Phone Number")
            for k in x:
                if contact_name.lower() in k.lower():
                    count+=1
                    print(count,"\t",k,"\t",x[k]["Phone Number"])
                    l.append(k)
            
            
            cno=int(input("\nIf you want to update the contact enter Serial no or else enter '0': "))
            if cno==0:
                print("\nRETURNING TO MAIN MENU")
            else:
                cdet=x[l[cno-1]]
                print("\nContact Name:\t",l[cno-1])
                for det in cdet:
                    print("\n",det,":\t",cdet[det])
                
                while(1):
                    uno=int(input("\nIf you want to update enter 1 or else enter 0: "))
                    if uno==0:
                        break
                    else:
                        fieldname=input("\nEnter the field to name to be updated: ")
                        value=input("\nEnter the value to be updated: ")
                        x[l[cno-1]][fieldname]=value
                        print("Contact",l[cno-1],"Updated")
            dump(x,"contacts.pkl")

            open("contacts.pkl", "rb").close()
        except EOFError:
            pass
    
    def delete_details(self):
        try:
            x = load(open("contacts.pkl", "rb"))
            print("\nSno\tContact Name\t Phone Number")
            count=0
            l=[]
            for k in x:
                count+=1
                print("\n",count,"\t",k,"\t",x[k]["Phone Number"])
                l.append(k)
            
            dno=int(input("\nEnter the Serial no of the contact to delete: "))
            del x[l[dno-1]]
            dump(x,"contacts.pkl")
            print("Contact",l[dno-1],"deleted")
        except EOFError:
            print("No contacts to delete")


print("\n\n\n------------------------------------Welcome To Contact Management------------------------------------")
c1=Contacts()
while 1:
    print("\n---------Select The Operation:----------\n")
    print("1: Add Contact Details")
    print("2: View All The Details")
    print("3: View By Contact name")
    print("4: Update The Details")
    print("5: Delete The Details")
    print("6: Exit The System")
    x=int(input("\nEnter Your Choice:"))
    if x==1:
        c1.add_contact_details()
    elif x==2:
        c1.view_all_contacts()
    elif x==3:
        c1.view_by_contactname()
    elif x==4:
        c1.update_details()
    elif x==5:
        c1.delete_details()
    elif x==6:
        print("Exting")
        break
    else:
        print("Enter valid option")
