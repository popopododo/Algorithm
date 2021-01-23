'''
class Node:
    def __init__(self,key,data,next=None):
        self.key=key
        self.data=data
        self.next=next
class NodeFunction:
    def __init__(self,key,data):
       self.head=Node(key,data)

    def addNode(self,key,data):
        if(self.head==''):
            newNode=Node(key,data)
            self.head=newNode
        else:
            tempNode=self.head
            while(tempNode.next):
                tempNode=tempNode.next
            newNode=Node(key,data)
            tempNode.next=newNode
    def printNode(self):
        tempNode=self.head
        while(tempNode):
            print(tempNode.data,end=" ")
            tempNode=tempNode.next
        print("\n===================")
    
    def searchNode(self,key):
        tempNode=self.head
        while(tempNode.next):
            if(tempNode.key==key):
                return tempNode.data
            tempNode=tempNode.next
'''
        

hash_table = [0 for i in range(20)]

def key_function(key):
    key%=8
    return key


def store_data(data,value):
    hashed=hash(data) # data를 해싱함 고유값
    key= key_function(hashed) # 해쉬값을 키함수에 넣어 키를 구함
    # newNode=Node(hashed,data)
    if(hash_table[key]==0): # 데이터가 비어있을때 
        hash_table[key]= [] # 해쉬값과 값을 가진 링크드 리스트 생성
    for _ in range(1):
        for _ in range(2):
            hash_table[key].append(hashed)
            hash_table[key].append(value)
        

def get_data(data):
    hashed=hash(data)
    key=key_function(hashed)
    if(hash_table[key]==0):
        print("찾는 데이터는 없습니다.")
        return 0
    else:
        for _ in range(len(hash_table[key])):
            if(hash_table[key][0]==hashed):
                return hash_table[key][1]



# Main

# Put data in HashTable

store_data('Eraser',1000)
store_data('Pen',1500)
store_data('gum',500)


# Get data from HashTable    
print(get_data("Eraser"))
print(get_data("Pen"))
print(get_data("gum")) 


# Hash Collision
# Open Hashing


