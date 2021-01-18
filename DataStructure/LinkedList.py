class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def addNode(self,data):
        tempNode=head
        while tempNode.next:
            tempNode=tempNode.next
        tempNode.next=Node(data)
        
    def addBetween(self,head,data,index):
        if(index==1):
            tempNode=Node(data,head)
            head=tempNode
            return head
            

    def printNode(self):
        tempNode=head
        while tempNode.next:
            print(tempNode.data, end=" ")
            tempNode=tempNode.next
        print(tempNode.data)
        print("=================================")
    def searchNode(self,head,x):
        count=1
        tempNode=head
        while tempNode.next:
            if(tempNode.data==x):
                print("찾으시는 노드의 위치는 {}번째에 위치해 있습니다.".format(count))
                return count
            tempNode.next=next
            count+=1
            
    def deleteNode(self,head,data):
        tempNode=head
        preNode=head
        if(head.data==self.data):
            head=tempNode.next
            tempNode=None
        else:
            while tempNode.next:
                if(tempNode.next.next==None):
                    tempNode.next=None
                    break
                tempNode.next=next
                if(tempNode.data==self.data):
                    preNode.next=tempNode.next
                    tempNode.next=None
                    break
                preNode.next=tempNode
        

# Main

# Create First Node
node= Node(1)
head=node

# Add 2 to 10 to linkedList
for x in range(2,10):
    node.addNode(x)

node.printNode()

# Add Element between the linkedList  
head=node.addBetween(head,10,1)
node.printNode()

# Delete Element

# node.deleteNode(head,10)
# node.printNode()

# Search Node

node.searchNode(head,3)
