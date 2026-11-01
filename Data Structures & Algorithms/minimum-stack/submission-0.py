class MinStack:

    def __init__(self):
        self.min_elems=[float('inf')]
        self.stk=[]
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if val<=self.getMin():
            self.min_elems.append(val)


    def pop(self) -> None:
        val=self.stk.pop()
        if val==self.getMin():
            self.min_elems.pop()
        return val


    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_elems[-1]
