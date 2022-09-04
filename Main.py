class node:
    def _init_(s,x):
        s.data = x
        s.prev = None
        s.next = None

        class DLL:
            def _init_(s):
                s.head = None
               
            def insertFront(s,x):
                new_node = node(x)
                if s.head != None:
                    new_node.next = s.head
                    s.head.prev = new_node
                s.head = new_node
           
            def display(s):
                if s.head == None:
                    print("Empty list")
                    return
                t = s.head
                while t != None:
                    print(t.data,end="-->")
                    t = t.next
                print("None")
