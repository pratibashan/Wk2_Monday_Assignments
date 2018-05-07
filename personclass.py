

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends =[] 
        self.greeting_count = 0
        self.num_unique_greeted =0

    def __repr__(self):
        return f"{self.name},{self.email},{self.phone}"
    

    def greet(self, other_person):
        
        self.greeting_count += 1
        print (f" Hello {other_person}, I am {self.name}!") 

        if  other_person == "Jordan" or other_person == "Sonny":
            self.num_unique_greeted = 0
        else:
            self.num_unique_greeted += 1    
           
        


    def print_contact_info(self): 
        print(f"Sonny's email: {self.email}, Sonny's phone number: {self.phone}")   

    def add_friend(self,friend):   
        print(f"{self.name}'s friend is {friend}")

    def num_friends(self):
        print(f"{self.name}'s no.of friend(s) {len(self.friends)}")

    
    def num_unique_people_greeted(self):
        
        return f"{self.num_unique_greeted}" 



sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')

print(jordan)

sonny.greet("Jordan")

count_unique = sonny.num_unique_people_greeted()
print(count_unique) 

sonny.greet("Mike")

count_unique = sonny.num_unique_people_greeted()
print(count_unique) 

jordan.greet("Sonny")

count_unique = sonny.num_unique_people_greeted()
print(count_unique) 


print(f"Sonny greeted his friend {sonny.greeting_count} time(s)")
print(f"Jordan greeted his friend {jordan.greeting_count} time(s)")

print(f"The contact info of Sonny is\n phone no.: {sonny.phone},email : {sonny.email}")
print(f"The contact info of Jordan is\n phone no.: {jordan.phone},email : {jordan.email}")

sonny.print_contact_info()

jordan.friends.append(sonny)
sonny.friends.append(jordan)

print(len(jordan.friends))

jordan.add_friend("Sonny")
jordan.num_friends()




