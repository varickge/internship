
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def add_to_start(self,value):
        if not isinstance(value,Node):
            value=Node(value)
        if self.head is None:
            self.head=value
            self.tail=value
        else:
            value.next=self.head
            self.head=value

    def add_to_end(self,value):
        if not isinstance(value,Node):
            value=Node(value)
        if self.head is None:
            self.head=value
            self.tail=value
        else:
            self.tail.next=value
            self.tail=value

    def pop(self):
        if self.head is None:
            return None
        current_element=self.head
        self.head=self.head.next
        return current_element.value

    def search(self,name):
        current_element=self.head
        while current_element:
            if current_element.value["name"] == name:
                return current_element.value
            current_element=current_element.next
        return "Element not found"

    def delete(self,name):
        current_element=self.head
        if current_element.value["name"]==name:
            self.head=self.head.next
        else:
            while current_element:
                if current_element.next is not None:
                    if current_element.next.value["name"]==name:
                        current_element.next=current_element.next.next
                        return
                current_element=current_element.next
            return print("Element not found")

    def reverse(self,current,previous):
        if self.head is None:
            return
        elif current.next is None:
            self.tali=self.head
            current.next=previous
            self.head=current
        else:
            next=current.next
            current.next=previous
            self.reverse(next,current)

    def __str__(self):
        current_element=self.head
        output=""
        while current_element:
            output+=(str(current_element.value)+"->")
            current_element=current_element.next

        return output


my_list=LinkedList()
my_list.add_to_start({
    "name": "Varuzhan",
    "age":"19",
    "country":"Armenia"
})
my_list.add_to_start({
    "name":"Aza",
    "age":"21",
    "country":"Armenia"
})
my_list.add_to_start({
    "name":"John",
    "age":"25",
    "country":"USA"
})
my_list.add_to_end({
    "name":"Simon",
    "age":"40",
    "country":"England",
})

print(my_list)




