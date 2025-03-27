import threading
from collections import deque

class Methane:
    def __init__(self):
        self.h_queue = deque()
        self.c_queue = deque()
        self.output = []

    def process(self, sequence: str) -> str:
        for atom in sequence:
            if atom == 'H':
                self.h_queue.append('H')
            elif atom == 'C':
                self.c_queue.append('C')
            
            while len(self.h_queue) >= 4 and len(self.c_queue) >= 1:
                self.output.append(self.c_queue.popleft())
                self.output.extend([self.h_queue.popleft() for _ in range(4)])
        
        return "".join(self.output)

# 示例使用
methane = Methane()
a=input("请输入原子序列：")
print(methane.process(a))

