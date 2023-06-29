# # p=[1,2,3,4,5,6,7,8,9,10]
# #
# # ll=[x for x in p if x%2==0]
# # print(ll)
#
# names=['aishwarya','pratik','amit','sumeet','raj']
#
# # print(names[0],names[-1])
# # names.append('yash')
# # print(names)
#
# alphabte={'A':'apple','B':'ball','c':'cat','D':'dog','E':'elephant'}
#
# # for i in alphabte.keys():
# #     print(i)
#
# # for i,j in alphabte.items():
# #     print(i,j)
#
# # for i,j in alphabte.items():
# #     if j =='cat':
# #         print(i)
#
# # set={1,2,3,4}
# #
# numbers1=[1,2,3,4,5]
# numbers2=[6,7,8,9,10]
# #
# # print(numbers1+numbers2)
# # a=list(zip(numbers1,numbers2))
# # print(a)
#
# m = [[1,2,3,4],
#      [4,5,6,8],
#      [7,8,9,2],
#      [5,7,3,9]]
# #
# for i in range(len(m)):
#     print(m[i][len(m[i])-1-i])
# m = [["a","b","c"],
#      ["x","y","z"],
#      ["k","y","q"]]

# for x in m:
#     for j in x:
#         print((str(x)+str(j)))
#         if (str(x)+str(j)) == len(m- 1):
#             print(x, j)
#         # print(j)
# for i in m:
#     print(len(i))

# a=[[1,2,3],[3,4,5],[5,6,7]]
# #
# p=[a[i][i] for i in range(len(a))]
# print(p)

# print(numbers2.extend(numbers1))

# p=['a','b','c']
#
# print(' '.join(['aish','1']))


# nums=[3,5,5,8]
# target=10

# tsum = [[i, j+1] for i in range(len(nums) - 1) for j in range(len(nums)-1) if nums[i] + nums[j + 1] == target]
# print(tsum[0])

# alphabte={'A':'apple','B':'ball','c':'cat','D':'dog','E':'elephant'}
#
# print(alphabte.get('cat'))

# def twosum(l, target):
#     start, end, total = 0, len(l) - 1, 0
#     while (start < end):
#
#         total += l[start] + l[end]
#         if total> target:
#             end -= 1
#         elif total< target:
#             start += 1
#         elif total == target:
#             return [start, end]
#         total=0
#
# print(twosum(l, target))
#
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # list1.reverse()
# print(list1[::-1])
# list2=[]
# for i in range(len(list1)-1,0,-1):
#     list2.append(list1[i])
#
# print(list2)
# p=[list1[i]+list2[j] for i in range(len(list1)) for j in range(len(list2)) if i == j ]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i==j:
#             p.append(list1[i]+list2[j])
# print(p)


#
# numbers = [1, 2, 3, 4, 5, 6, 7]
#
# for i in range(len(numbers)):
#     numbers[i]=numbers[i]**2
# print(numbers)
#
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# p=[]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i==j:
#             p.append(' '.join([list1[i],list2[j]]))
# print(p)

# list1 = [1,3,5,7,9]
# list2 = [2,4,6,1]
# p=[]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i==j:
#             p.append(list1[i]+list2[j])
# print(p)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# for i,j in zip(list1,list2[::-1]):
#     print(i,j)

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for i in list1:
#     if i=="":
#         list1.remove(i)
# print(list1)

# remove_blank = list(filter(None, list1))
# print(remove_blank)

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#
# list1[2][2].append(7000)
# print(list1)

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#
# # sub list to add
# sub_list = ["h", "i", "j"]
#
# list1[2][1][2].extend(sub_list)
# print(list1)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# list2=[ ]
# for i in list1:
#     if i not in  list2:
#         list2.append(i)
# print(list2)

# list1 = [5, 10, 15, 20, 25, 50, 20]

# for i in range(len(list1)):
#     if list1[i]==20:
#         list1[i]=200
#         break
# print(list1)

# divide_by_seven=[i for i in range(2000,3201) if i%7==0 and i%5!=0]
# print(divide_by_seven)

# print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
#
# x = int(input())
# print (fact(x))


# number=int(input("Enter Number:"))
# square={i: i*i for i in range(1,number+1)}
# print(square)


# class Inputoutput:
#     def __init__(self):
#         self.name=''
#
#     def getString(self):
#         self.name=input('String: ')
#     def toupperstring(self):
#         print(self.name.upper())
#
# object=Inputoutput()
# object.getString()
# object.toupperstring()


# numbers=input("Enter the Number:")
# list_of_numbers=numbers.split(',')
# tuple1=tuple(list_of_numbers)
#
# print(list_of_numbers,tuple1)

# elements=5
# items=3
# list_array=[[i for i in range(elements)] for x in range(items)]
# print(list_array)

# words=input()
# words_list=[x for x in words.split(" ")]
# print(" ".join(sorted(list(set(words_list)))))


# values=[1010,1100,1001]
# v=[]
#
# for i in values:
#     if i%5==0:
#         v.append(i)
#
# print(v)


# Sample_List =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# Sample_List.sort(key=lambda x:x[1])
#
# print(Sample_List)


# for i in range(1000,3001):
#     snumber=str(i)
#
#     if int(snumber[0])%2==0 and int(snumber[1])%2==0 and int(snumber[2])%2==0 and int(snumber[3])%2==0:
#         print(i, end=',')

# sentence = "helLo wOrld"
# l=0
# digits=0
# for i in sentence:
#     if i.isalpha():
#         l+=1
#     elif i.isdigit():
#         digits+=1
# print(l,digits)

# upper,lower=0,0
# for i in sentence:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
# print(upper,lower)

# list_of_names = [("Tom", 19, 80),
#                  ("John", 20, 90),
#                  ("Jony", 17, 91),
#                  ("Jony", 17, 93),
#                  ("Json", 21, 85)]
#
#
# list_of_names.sort(key=lambda x:x[0][2])
# print(list_of_names)

# class Divide_by_seven:
#     def divide_seven(self,n):
#         for i in range(n):
#             if i%7==0:
#                 yield i
#
# g=Divide_by_seven()
# p=g.divide_seven(100)
# for i in p:
#     print(i)
# sentence="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
#
#
# sentence_list=sorted(sentence.split(' '))
#
# count_dic={x:sentence_list.count(x) for x in sentence_list}
# for key, value in count_dic.items():
#     print(key,value)
#
# tuple_ele=(1,2,3,4,5,6,7,8,9,10)
#
# print(tuple[:5])
# print(tuple[5:])

# square_list=tuple(map(lambda x:x**2,filter(lambda x:x%2==0 , tuple_ele) ))
# print(square_list)


# import  re
# sword="2 cats and 3 dogs."
#
# print (re.findall('\d+',sword))


# import re
# emailAddress = "aishwarya@code.com"
# pat2 = "(\w+)@(\w+)\.(com)"
# r2 = re.match(pat2,emailAddress)
# print (r2.group(2))

# n=5
# def f(n):
#     if n==0:
#         return 0
#
#     return f(n-1) + 100
#
# p=f(5)
# print(p)


#
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(li)):
#     for j in range(len(li)):
#         print(li[i][j])
#         if li[i][i] > 1:
#             for x in range(2, li[i][j]):
#                 if li[i][j] % x == 0:
#                     break
#                 else:
#                     li[i][j] = 'True'


for i in range(len(li)):
    for n in range(len(li[i])):

        if li[i][n] > 1:
            for x in range(2, li[i][n]):
                if li[i][n] % x == 0:
                    break
            else:
                li[i][n] = 'True'

print(li)
