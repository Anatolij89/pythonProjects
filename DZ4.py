# a = 1
# for i in range(1, 10):
#     a *= i

# print(a)
# arr = []
# for i in range(1, 50):
#     if i % 5 == 0:
#         arr.append(i)
# print(arr)

# for i in range(1, 497):
#     if i % 2 == 0:
#         print(i)

arr = [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 7, 7, 7, 8, 8, 8, 8]
narr = []
for i in arr:
    if arr.count(i) > 2:
        narr.append(i)
for n in narr:
    if narr.count(n) > 1:
        narr.remove(n)
print(narr)
