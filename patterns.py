# n=5
# for i in range(n):
#     print("*",end=" ")

# m=2
# n=5
# for i in range(m):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# n=5
# for i in range(n): #rows
#     for j in range(n): #columns
#         print("*",end=" ")
#     print()

# #left angled trinagle
# n=5
# for i in range(1,n+1): #rows
#     for j in range(i): #columns
#         print("*",end=" ")
#     print()


# #triangle pattern
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# #diamond pattern
# n = 5
# # Upper half
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(2*i-1):
#         print("*", end=" ")
#     print()
# # Lower half
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end=" ")
#     for k in range(2*i-1):
#         print("*", end=" ")
#     print()

# #hollow sphere
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #hollow sphere with diagonal
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #hollow sphere with 2 diagonal
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==j or n-i-1==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()