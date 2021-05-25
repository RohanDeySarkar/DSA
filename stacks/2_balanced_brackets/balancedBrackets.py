def balancedBrackets(string):
    stack = []
    openBrackets = "({["
    closeBrackets = ")}]"
    matchBrackets = {")":"(", "}":"{", "]":"["}
    for bracket in string:
        if bracket in openBrackets:
            stack.append(bracket)
        elif bracket in closeBrackets:
            if not len(stack):
                return False
            if stack[-1] == matchBrackets[bracket]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

string = "([])(){}(())()()"
print(balancedBrackets(string))
