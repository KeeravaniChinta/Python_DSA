# print("Keeravani\n"*3)
# print(r"C:\new\test")
# print("C:\\new\\test") 
# print(int(float("1.2"))) 


# n=int(input("Enter a number:"))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd number")


# dict={
#     "name":"Keeravani",
#     "gender":"female",
#     "age":20,
#     "courses":["python","java","datascience"]
# }
# #dict["name"]="Sri"
# dict.update(name="Kokila")
# print(dict)
# print(dict.keys())
# print(dict.items())
# print(dict.values())
# print(dict["age"])
# print(dict.get("name"))


# l=[1,2,3,4,5]
# l.remove(3)
# l.pop()
# print(l)


# l=[1,2]
# l.append(3)
# print(l)
# x=[]
# print(len(x))
# x.append(l)
# print(x)
# print(len(x),"len(x)")
# print(len(x[0]),"len(x[0])")
# m=[4,5,6]
# x.append(m)
# print(x)
# t=[]
# t.append(x)
# t.append([100,200,300])
# print(t)
# print(t[0])

# #Armstrong number
# number = int(input("Enter a number: "))
# temp = number
# digits = len(str(number))
# total = 0
# while temp > 0:
#     digit = temp % 10
#     total += digit ** digits
#     temp //= 10
# if total == number:
#     print("The number is an Armstrong number.")
# else:
#     print("The number is not an Armstrong number.")


# #perfect number
# number = int(input("Enter a number: "))
# total = 0
# for i in range(1, number):
#     if number % i == 0:
#         total += i
# if total == number:
#     print("The number is a Perfect Number.")
# else:
#     print("The number is not a Perfect Number.")


# # strong number 145=1!+4!+5!
# number = int(input("Enter a number: "))
# temp = number
# total = 0
# while temp > 0:
#     digit = temp % 10
#     fact = 1
#     for i in range(1, digit + 1):
#         fact *= i
#     total += fact
#     temp //= 10
# if total == number:
#     print("The number is a Strong Number.")
# else:
#     print("The number is not a Strong Number.")


# #factorial using recursion
# def factorial(n):
#     if n == 0 or n == 1:   # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print("Factorial =", factorial(num))


# #fibonacci series using recursion
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# # User input
# terms = int(input("Enter the number of terms: "))
# if terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     print("Fibonacci Series:")
#     for i in range(terms):
#         print(fibonacci(i), end=" ")


# #sum of array elements
# arr=[2,5,4,6,7,9]
# sum=0
# for i in range(len(arr)):
#     sum+=arr[i]
# print(sum)

# arr=[2,5,4,6,7,9]
# sum=0
# for i in range(len(arr)):
#     if i in range(2,6):
#        sum+=arr[i]
# print(sum)


# #prefix sum
# def build_prefix(arr):
#     prefix=[]
#     sum=0
#     for i in arr:
#         sum+=i
#         prefix.append(sum)
#     return prefix
# arr=[2,5,4,6,7,9]
# print(build_prefix(arr))


# #range sum
# def build_prefix(arr):
#     prefix=[]
#     sum=0
#     for i in arr:
#         sum+=i
#         prefix.append(sum)
#     return prefix
# def range_sum(prefix,start,end):
#     if start==0:
#         return prefix[end]
#     return prefix[end]-prefix[start-1]
# arr=[2,5,4,6,7,9,7,6]
# prefix=build_prefix(arr)
# print(prefix)
# print(range_sum(prefix,2,6))


# #equilibrium index
# arr=[-7,1,5,2,-4,3,0]
# def euilibrium_index(arr):
#     total=sum(arr)
#     left_sum=0
#     for i in range(len(arr)):
#         right_sum=total-arr[i]-left_sum
#         if right_sum==left_sum:
#             return i
#         left_sum+=arr[i]
#     return -1
# print(eqilibrium_index(arr))


# arr=[1,2,3,4]
# k=7
# def sub_array_sum(arr,k):
#     current_sum=0
#     start=0
#     for end in range(len(arr)):
#         current_sum+=arr[end]
#         while start<end and current_sum>k:
#             current_sum-=arr[start]
#             start+=1
#         if current_sum==k:
#             return [arr[start],arr[end]]
#     return []
# print(sub_array_sum(arr,k))


# #frequency count
# arr=[2,4,2,5,7,8,3,7,2,1,6]
# freq={}
# for num in arr:
#     freq[num]=freq.get(num,0)+1
# print(freq)


# lst = [1, 2, 3, 2, 4, 5, 1, 6, 2]

# d = {}

# # Count frequency
# for i in lst:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# # Print duplicate elements
# for key in d:
#     if d[key] > 1:
#         print(key)

# n=int(input("Enter the digit:"))
# count=0
# temp=n
# for i in str(n):
#     digit=n%10
#     temp=temp//10
#     count+=1
# print(count)


# name = input("Enter the name: ")
# words = name.split()
# initials = ""
# for word in words:
#     initials+=word[0].upper()
# print(initials)

# #or
# x=input("Enter your name:").split()
# print(x[0][0].upper()+x[1][0].upper())


# s = input("Enter a string: ")
# max_streak = 0
# current_streak = 1
# for i in range(len(s)):
#     if i == 0:
#         max_streak = 1
#     elif s[i] == s[i - 1]:
#         current_streak += 1
#     else:
#         current_streak = 1
#     if current_streak > max_streak:
#         max_streak = current_streak
# print(max_streak)


# arr = [3, 4, 5, 6]
# target = 9
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]==target:
#             print(i,j)
#             break
# else:
#     print([])


# arr=[3,4,5,6,7]
# target=9
# left=0
# right=len(arr)-1
# while left<right:
#     if arr[left]+arr[right]==target:
#         print(left,right)
#         break
#     elif arr[left]+arr[right]<target:
#         left+=1
#     else:
#         right-=1



# s = input("Enter a string: ")
# left = 0
# right = len(s) - 1
# while left < right:
#     if s[left] != s[right]:
#         print("False")
#         break
#     left += 1
#     right -= 1
# else:
#     print("True")

