class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minmaxStack = []
        
    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minmaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)
        newMinMax = {"max": number, "min": number}
        if len(self.minmaxStack):
        	lastMinMax = self.minmaxStack[-1]
        	newMinMax["max"] = max(lastMinMax["max"], number)
        	newMinMax["min"] = min(lastMinMax["min"], number)
        self.minmaxStack.append(newMinMax)

    def getMin(self):
        return self.minmaxStack[-1]["min"]

    def getMax(self):
        return self.minmaxStack[-1]["max"]

