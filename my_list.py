my_list= []

my_list.append("Deborah")
my_list.append("Dayo")
my_list.append("Eunice")
my_list.append("Kaffie")
print(my_list)
my_list[1]= "Apple"
print(my_list)
my_list + =["Ade","Segun","Love"]
print(my_list)
my_list.pop(6)
print(my_list)
last_item = my_list[:-1]
print(my_list)
my_list.sort ()
print(my_list)
for i in range (len (my_list)):
    if my_list[i] = "Ade":
        print(i)