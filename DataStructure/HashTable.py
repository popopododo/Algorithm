hash_table = [0 for i in range(100)]

def key_function(key):
    key%=8
    return key


def store_data(data,value):
    hashed=hash(data)
    key= key_function(hashed)
    if(hash_table[key]!=0):
        key+=1
        hash_table[key]=value
    else:
        hash_table[key]=value

def get_data(data):
    data=hash(data)
    key=key_function(data)
    if hash_table[key]==0:
        print("저장된 값이 없습니다.")
        return 0
    else:
        return hash_table[key]



# Main

# Put data in HashTable

store_data('Eraser',1000)
store_data('Pen',1500)
store_data('gum',500)

# Get data from HashTable    
print(get_data("Eraser"))
print(get_data("Pen"))
print(get_data("gum"))
