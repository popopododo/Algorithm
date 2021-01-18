class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class NodeFunction:
    def __init__(self,data):
        self.head=Node(data)
    
    def addNode(self,data):
        if(self.head==""):
            self.head=Node(data)
        else:
            tempNode=self.head
            while(tempNode.next):
                tempNode=tempNode.next
            tempNode.next=Node(data)
    def addBetween(self,index,data):
        pos=0
        tempNode=self.head
        preNode= self.head
        newNode=Node(data)
        if(index==0):
            newNode.next=self.head
            self.head=newNode
        else:
            while(tempNode.next):
                tempNode=tempNode.next
                pos+=1
                if(pos==index):
                    newNode.next=preNode.next
                    preNode.next=newNode
                preNode=tempNode
                
                
    def searchNode(self,target):
        tempNode=self.head
        while(tempNode.next):
            if(tempNode.data==target):
                print("{}을 찾았습니다.".format(target))
                break
            tempNode=tempNode.next
        if(tempNode.next==None):
            print("{}을 찾지 못했습니다.".format(target))
            
    def printNode(self):
        tempNode=self.head
        while(tempNode):
            print(tempNode.data, end=" ")
            tempNode=tempNode.next
        print("\n========================")
    
    def deleteNode(self,data):
        tempNode=self.head
        preNode=self.head
        if(self.head==''):
            return -1
        elif(self.head.data==data):
            self.head=tempNode.next
        else:
            while(tempNode.next):
                tempNode=tempNode.next
                if(tempNode.data==data):
                    if(tempNode.next==None):
                        preNode.next=None
                        break
                    else:
                        preNode.next=tempNode.next
                        tempNode.next=None
                preNode=tempNode

# Main

# Create First Node
linkedList= NodeFunction(1)


# Add 2 to 10 to linkedList
for x in range(2,11):
    linkedList.addNode(x)

linkedList.printNode()

# Add Element between the linkedList  
linkedList.addBetween(0,8181)
linkedList.printNode()
linkedList.addBetween(5,8282)
linkedList.printNode()

# Search Node

linkedList.searchNode(8282)
print()
linkedList.searchNode(8000)
print()
# Delete Element

linkedList.deleteNode(8181)
linkedList.printNode()
linkedList.deleteNode(8282)
linkedList.printNode()
linkedList.deleteNode(10)
linkedList.printNode()

