class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
          
class SwapNodes:  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
          
    def addNode(self, data):  
        newNode = Node(data);  
          
        if(self.head == None):  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            self.tail.next = newNode;  
            self.tail = newNode;  
              
    def swap(self, n1, n2):  
        prevNode1 = None;  
        prevNode2 = None;  
        node1 = self.head;  
        node2 = self.head;  
          
        if(self.head == None):  
            return;  
              
        if(n1 == n2):  
            return;  3
              
        while(node1 != None and node1.data != n1):  
            prevNode1 = node1;  
            node1 = node1.next;  
              
        while(node2 != None and node2.data != n2):  
            prevNode2 = node2;  
            node2 = node2.next;  
              
        if(node1 != None and node2 != None):  
              
            if(prevNode1 != None):  
                prevNode1.next = node2;  
            else:  
                self.head  = node2;  
                  
            if(prevNode2 != None):  
                prevNode2.next = node1;  
            else:  
                self.head  = node1;  
                  
            temp = node1.next;   
            node1.next = node2.next;   
            node2.next = temp;  
        else:  
            print("Swapping is not possible");  
              
    def display(self):  
        current = self.head;  
          
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):  
            print(current.data),  
            current = current.next;  
         
   
sList = SwapNodes();  
   
sList.addNode(1);  
sList.addNode(2);  
sList.addNode(3);  
sList.addNode(4);  
sList.addNode(5);  
   
print("Original list: ");  
sList.display();  
   
   
sList.swap(2,5);  
   
print("List after swapping nodes: ");  
sList.display();  

