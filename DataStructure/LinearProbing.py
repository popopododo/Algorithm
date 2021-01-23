hash_table=[0 for i in range(30)]

def key_function(data):
    key=data%11
    return key

def store_data(data,value):
    key=key_function(data)
    if(hash_table[key]==0):
        hash_table[key]=[data,value]
    else:
        while(hash_table[key]!=0):
            key+=1
            if(key>len(hash_table)-1):
                key=0
        hash_table[key]=[data,value]

def get_data(data):
    key=key_function(data)
    if(hash_table[key][0]==data):
        return hash_table[key][1]
    else:
        while(hash_table[key][0]!=data):
            key+=1
            if(key>len(hash_table)-1):
                key=0
        return hash_table[key][1]

# Main

# Store data in Hash Table
store_data(11,"Tommy")
store_data(12,"Buzzer")
store_data(22,"Hurly") # Hash Collision

# Get data from Hash Table
print(hash_table)
print(get_data(11))
print(get_data(22))