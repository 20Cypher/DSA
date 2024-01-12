# n = int(input("number of elements in list: "))
# list1 = list()
# for i in range(n):
#     a = int(input())
#     list1.append(a)
# print(list1)

# print("enter the list elements:")
# list2 = list(map(int, input().split()))

# print(list1)
# print(list2)

inp = input()
if ord(inp)>64 and ord(inp)<90:
    print("1")
elif ord(inp)>97 and ord(inp)<122:
    print("0")
else:
    print("-1")