class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def len(self):
        return len(self.items)

    def isEmpty(self) -> bool:
        return len(self.items) == 0
