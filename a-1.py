# assignment1
#list
'''union_terotories = ["ladakh","delhi","daman & diu","Chandigarh","podichery","Dadar&Nagar havelli"]
print(union_terotories)'''
#update
'''union_terotories[4] = "Jammu&Kashmir"
print(union_terotories)'''
#append the list
'''union_terotories.append("Lakshdeep")
print(union_terotories)'''
#inserting the value
'''union_terotories.insert(0,"Andaman&Nicobar Island")
print(union_terotories)'''
#remove 
'''Indian_Cricket_Team = ["Rohit Sharma","KL Rahul","Virat Kholi","Suryakumar Yadav","Arshdeep Singh","Axar Patel"]
print(Indian_Cricket_Team)
Indian_Cricket_Team.remove("Axar Patel")
print(Indian_Cricket_Team)'''
#pop
'''marks_obtained = [98,99,90.9,55,65,87,33,78]
print(marks_obtained)
marks_obtained.pop(2)
print(marks_obtained)'''
#delete
'''random_things = [True,"my name is paul",0.8,4566,False]
print(random_things)
del random_things[0]
print(random_things)'''
#cocatenation
'''Stream = " Data Science"
print(" The future will be dpending on" +Stream)'''
#tuple
'''Stream_Btech = ("Computer Science","Mechanical","Civil","Electronics","Electricals")
print(Stream_Btech)
print(len(Stream_Btech))'''
#update ,delete ,append cannot be used in tuple because it is  cannot changed its item because it is immmutable
#dicitionary
'''banking = {
         "customer id" : 98765321,
         "Balance" : 9999999,
         "adress of customer" : "New Delhi",
         "Customer Name" : "walker",
         " Bank name" : "State  Bank Of India",
         " IFSC code" : "SBI09787"
}
print(banking)
#update
banking["Bank name"] =["State Bank Of India","himachal State bank"]
print(banking)'''
#set
'''computer_languages = {"phython","java","C","C++","HTML",1001,2^5}
print(computer_languages)'''
#union operations
a = {"true","flase",True,False,0.12,23}
b ={23,43, 54,6356}
'''c = a|b
print(c)'''
#intersection
'''print(a.intersection(b))'''
#update
'''a.add("i am a superstar")
print(a)'''
#delete
'''del b
print(a)'''
#function
# Q 1
def my_func():
 '''x = 10
print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)'''
# Q 2
'''def greet(name):

    print("Hello, " + name + " Good morning!")

greet('Paul')'''
