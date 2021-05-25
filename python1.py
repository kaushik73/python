# name=input("enter your first name " )
# name1=input("enter your last  name " )
# name2= name+" "+name1
# gender , classes = input("enter your gender and class with comma seperated ").split(",")
# print("Your Details Are:-")
# print("Your name: "+ (name2))
# print("Your Gender is:"+ gender )
# print("Your Class is:" +classes )
#-------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------#
dicti = {'name': 'Kaushik','college':'SKIT', 'Semester':'3'}
# print(dicti['name'])
dicti['section'] = 'C(g1)'
print(dicti)
# print(type(dicti))
if 'name' in dicti :
 print("present")
# print("not present")  
else :
    print("NOT present")
dicti_items= dicti.items
# print(f"Printing dictionary as tuple {dicti_items}")
# print(dicti.items)
dicti['batch']= ['this is new method']
print(dicti)

dicti.pop('batch')
print(dicti)


class laptop : 
    def __init__ (self,model_name,brand, price):
        self.model = model_name
        self.brand = brand
        self.price = price
        self.laptop_name = brand + ' ' + model_name


lap1 = laptop('rx00tx', 'HP','45000')         
 
print("Brand of laptop is : " +  lap1.brand)
print(lap1.model)
print(lap1.laptop_name)


