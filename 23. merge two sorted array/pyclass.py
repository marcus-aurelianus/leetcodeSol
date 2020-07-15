class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.cur_min = float('inf')
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, None))
            self.cur_min = x
        else:
            if x <= self.cur_min:
			# if the current one is the new minimum, record the previous minimum value along with it
                self.stack.append((x, self.cur_min))
                self.cur_min = x
            else:
                self.stack.append((x,None))

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp[0] == self.cur_min:
		# if we pop the current minimum value, recover the previous minimum value
            self.cur_min = temp[1]
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.cur_min



