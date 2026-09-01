# bit 연싼자

a = 5 # 0000 0101
b = 3 # 0000 0011
print(a & b)
print(a | b)
print(a ^ b) # 0000 0110
print(a << b) # 5 -> 10 -> 20 -> 40
print(a >> b) # 5
print(40 >> b)
print(~a)

# Membershit 연산자
print("a" in "apple")
print(3 in [1, 2, 3])

# ternary operator
# int max = a > b ? a : b
a, b = 2, 3
max_num = a if a > b else b
print("짝수" if a % 2 == 0 else "홀수")
score = 85
# ABCD
print('A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D')