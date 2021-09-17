import time


t1 = time.time()

x = "1+1=2"
x1 = "π + 2112 -2112 +2*x - 2*x = π"
x2 = "2*π + 3112 -1000 - 2*π = 2112"
x3 = "2*t + 8 - 8 -t = t"
x4 = "2112 +7 + 3,14 + 2 = 2124,14"
x5 = "2124, 14 - 2124 - 0,14 = 0"
x6 = "we did a full circle again it's a focusing and silence exercise"
x7 = "social media are more mathematical structures than we think"
x8 = "don't wonder for whom the bell tolls it's always for you that's another idea we don't really understand"
x9 = "9 + 9 -1 -1 -1 -1 -14 = 0"
x10 = "68 101 109 111 99 114 97 99 121 32 103 111 101 115 32 115 108 111 119 32 105 116 39 97 32 103 111 111 100 32 105 100 101 97 32 73 32 116 104 105 110 107 46 32"

print(bool(x))
print(bool(x1))
print(bool(x2))
print(bool(x3))
print(bool(x4))
print(bool(x5))
print(bool(x6))
print(bool(x7))
print(bool(x8))
print(bool(x9))
print(bool(x10))

t2 = time.time()
t = t2 - t1
print("Elapsed time is : ", t, " seconds")
