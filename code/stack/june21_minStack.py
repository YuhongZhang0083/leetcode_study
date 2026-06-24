'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minstack:  # minstack 为空栈
            self.minstack.append(val)
        else:
            curr_min = min(val, self.minstack[-1]) # 当前的值与上一个最小值比较
            self.minstack.append(curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop() # 两个栈要一起弹


    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        top_min = self.minstack[-1] # 栈顶就是当前最小值，O(1)
        return top_min
    

minStack =  MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.getMin()) # return 0
minStack.pop()
print(minStack.top())    # return 2
print(minStack.getMin()) # return 1