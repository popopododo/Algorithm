class Node:
    def __init__(self,data,pre=None, post=None):
        self.data=data
        self.pre=pre
        self.post=post

class NodeFunction:
    def __init__(self,data):
        self.head=Node(data)
        self.tail = self.head

    def addNode(self,data):
        if self.head== None:
            self.head=Node(data)
            self.tail=self.head
        else:
            tempNode=self.tail
            newNode=Node(data)
            tempNode.post=newNode
            newNode.pre=tempNode
            self.tail=newNode

    def printNode(self):
        tempNode=self.head
        while tempNode:
            print(tempNode.data , end=" ")
            tempNode=tempNode.post
        print("\n=======================")
        
    def sort(self):
        count=0
        tempNode=self.head
        while(tempNode):
            tempNode=tempNode.post
            count+=1
        for x in range(count):
            for y in range(count-x):
                
        
    def addBetween(self,index,data):
        if(self.head== None):
            self.head=Node(data)
            self.tail=self.head
        else:
            if(index==self.head.data):
                newNode= Node(data)
                newNode.post=self.head
                self.head.pre=newNode
                self.head= newNode
            elif(index==self.tail.data):
                tempNode=self.tail
                newNode=Node(data)
                tempNode.post=newNode
                newNode.pre=tempNode
                self.tail=newNode
            else:
                tempNode=self.head
                for _ in range(index):
                    tempNode=tempNode.post
                preNode=tempNode.pre
                newNode=Node(data)
                newNode.pre=preNode
                preNode.post=newNode
                tempNode.pre=newNode
                newNode.post=tempNode
    def addNext(self,data):
        if(self.head.data<data and self.head.post.data >data):
            tempNode=self.head
            newNode= Node(data)
            newNode.post=tempNode
            tempNode.pre=newNode
            head=newNode

        elif(self.tail.data>data and self.tail.pre.data < data):
            addNode(data)
           
        # while(tempNode.post):
        #    tempNode=tempNode.post
            
    def deleteNode(self,data):
        if(self.head==data or self.tail==data):
            if(self.head.data==data):
                tempNode= self.head
                nextNode=self.head
                nextNode=nextNode.post
                tempNode.post=None
                nextNode.pre=None
                head=nextNode
            elif(self.tail.data==data):
                tempNode=self.tail
                preNode=self.tail
                preNode=preNode.pre
                tempNode.pre=None
                preNode.post=None
                tail=preNode
        tempNode=self.tail
        postNode=self.tail
        while(tempNode.pre):
            tempNode=tempNode.pre
            if(tempNode.data==data):
                preNode=tempNode.pre
                preNode.post=postNode
                postNode.pre=preNode
                tempNode.pre=None
                tempNode.post=None
                
            postNode=tempNode
        
            
                
        

# Main

# Create Doubly linked list
print(" Create Double LinkedList")
doublyLinkedList = NodeFunction(0)

# Add data in Doubly Linked list

for x in range(1,11):
    doublyLinkedList.addNode(x)
doublyLinkedList.printNode()

# Add data in indexed position
print(" Add 8080, 8181, 8282 in random index")
doublyLinkedList.addBetween(1,8080)
doublyLinkedList.printNode()
doublyLinkedList.addBetween(10,8181)    
doublyLinkedList.printNode()
doublyLinkedList.addBetween(5,8282)    
doublyLinkedList.printNode()

# Add data in right places after comparing data
print("Add data in right places")
doublyLinkedList.addNext(0)
doublyLinkedList.printNode()
# Deleted Node (중복된 데이터도 삭제)
print(" Overlap data")
doublyLinkedList.addBetween(5,3)
doublyLinkedList.printNode()

print(" Delete overlapped data")
doublyLinkedList.deleteNode(3)
doublyLinkedList.printNode()
doublyLinkedList.swapData()


