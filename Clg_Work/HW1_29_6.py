"""Amazon Conveyor belt """

lst=['NULL']*8

# Update a slot
def update_product(index,product):
    lst[index]=product
    
# what's at a slot
def print_slot(index):
    print(lst[index])
    

#find product
def find_product(product):
    if product in lst :
        print(f"{product} found at slot {lst.index(product)}")
    else:
        print(f"{product} not found in the slot")
        
#slot full
def is_full():
    if 'NULL' in lst:
        print("Slots are not full")
    else:
        print("Slots is full")
        


update_product(0, "Laptop")
update_product(3, "Phone")
update_product(7, "Keyboard")

print_slot(3)

find_product("Phone")
find_product("Mouse")
is_full()

print(lst)