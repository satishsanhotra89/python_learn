"""s1= "python is fun"
s2= s1.strip()
print(s2)  # Output: "python"
print(s1.replace("fun","powerful"))  # Output: "python is fun"
s4= "we are learning python"
s5= "python"
print(s4.find(s5))  # Output: 18
print(s4.index(s5))  # Output: 18
print(s4.upper())  # Output: "WE ARE LEARNING PYTHON"
print(s4.lower())  # Output: "we are learning python"

Name="satish"
Age= 35

list1= ["satish", 35, "kumar"]
print(list1)  # Output: True

list2 = [1,2,3,6,4]
print(list2)  # Output: [1, 2, 3, 4, 6]
print(list2[1:5:1])
print(list2*2)
print(len(list2))
list4=print(list2.sort())
##list5=print(list2.append("satish"))
print(list2)
##list2.insert(3,"kumar")
print(list2)
##list2.extend(["a","b","c"])
print(list2)

list2.pop()
print(min(list2))
print(max(list2))
print(sum(list2))
print(list2.count(3))
print(list2.reverse())
tuple1= (1,2,3,4,5)
print(tuple1) 
print(tuple1.count(3))
print(tuple1.index(4))  

"""
#sets
Student1= {"Hindi", "english", "maths", "science"}
Student2= {"history", "geography", "maths", "science"}
#union of two sets
all= Student1.union(Student2)

print(all)
#intersection of two sets
#common_in_both= Student1.intersection(Student2)
common_in_both= Student1 & Student2
print(common_in_both)

