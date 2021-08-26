class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Operation:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beg(self,ele):
        self.ele = ele
        if self.head == None:
            node = Node(self.ele,None)
            self.head = node
            self.tail = node
            return

        node = Node(self.ele,self.head)
        self.head = node

    def insert_pos(self,ele,pos):
        self.pos = pos
        self.ele = ele
        if self.head == None and self.pos > 1:
            print("Invalid Position")
            return
        
        if self.pos == 1:
            self.insert_beg(self.ele)
            return

        count = 1
        temp = self.head
        while count != self.pos-1:
            if temp.next:
                temp = temp.next
                count += 1
            else:
                print("Invalid Position")
                return

        if temp.next:
            node = Node(self.ele,temp.next)
            temp.next = node
        else:
            self.insert_end(self.ele)

    def insert_end(self,ele):
        self.ele = ele
        if self.head == None:
            self.insert_beg(self.ele)
            return

        node = Node(self.ele,None)
        self.tail.next = node
        self.tail = node

    def delete_beg(self):
        if self.head == None:
            print("Empty")
            return
        
        self.head = self.head.next

    def delete_pos(self,pos):
        self.pos = pos
        if self.head == None:
            print("Empty")
            return
        
        if self.pos == 1:
            self.delete_beg()
            return

        count = 1
        temp = self.head
        while count != self.pos-1:
            if temp.next:
                temp = temp.next
                count += 1
            else:
                print("Invalid Position")
                return

        if temp.next == None:
            print("Invalid Position")
            return

        if temp.next.next:
            temp.next = temp.next.next
        else:
            self.delete_end()

    def delete_end(self):
        if self.head == None:
            print("Empty")
            return

        temp = self.head
        if temp.next == None:
            self.head = None
            return
        
        while temp.next.next:
            temp = temp.next

        temp.next = None
        self.tail = temp

    def search(self,ele):
        self.ele = ele
        temp = self.head
        while temp:
            if temp.data == self.ele:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='-->')
            temp = temp.next
        print()
        


print('''1.Insert at beginning  2.Insert at position  3.Insert at end
4.Delete at beginning  5.Delete at position  6.Delete at end
7.Search               8.Display             9.Exit''')

LL = Operation()

while True:
    choice = int(input("\nChoice: "))

    if choice==1:
        ele = input("Element: ")
        LL.insert_beg(ele)

    elif choice==2:
        ele = input("Element: ")
        pos = int(input("Position: "))
        LL.insert_pos(ele,pos)

    elif choice==3:
        ele = input("Element: ")
        LL.insert_end(ele)

    elif choice==4:
        LL.delete_beg()

    elif choice==5:
        pos = int(input("Position: "))
        LL.delete_pos(pos)

    elif choice==6:
        LL.delete_end()

    elif choice==7:
        ele = input("Element: ")
        print(LL.search(ele))

    elif choice==8:
        LL.display()

    else:
        exit()
