#Star Pattern

i = 1
while(i< 5):
    print(i * "*")
    i +=1
print()
#Reverse Star Pattern

while(i > 0):
    print(i * "*")
    i -= 1


for i in range(5):
    print(i)

marks = [70,80,90,"English"]
print(marks [-1])   #For reverse Iteration use (-1,-2,-3)

for score in marks:
    print(score)


# append function in List
marks.append(99)
print(marks)
# insert in particular idx
marks.insert(1,"Farsi")
print(marks)
# to Check Particular element exist in list or not
print("Farsi" in marks)
# to get length of List
print(len(marks))
# to clear List
marks.clear()
print(marks)


# use break
student = ["Ali", "insha","bittu","chacha", "chachi"]
for stu in student:
    if(stu == "chachi"):
        break
    print(stu)

print()
# use continue
student = ["Ali", "insha","bittu","chacha", "chachi"]
for stu in student:
    if(stu == "insha"):
        continue
    print(stu)

# Tuple :
    # In tuple () is not important used just for understanding purpose
    # Eg: person = "ram","shyam","abhi"
    # It is Immutable
marks = (97,98,99,99,99,78)

print(marks.index(99))      # to get index of element

print(marks.count(99))  # to count element how much tym it come


# set :
    # It store Unique value
    # Also there is no idexing in set so we cannot get like: marks[1]
    # So to get element from set we can iterate in it
    # it is unordered
marks = {97,98,99,99,99,78}
print(marks)

for score in marks:
    print(score)


# Dictionary :

marks= {"English": 95, "Chemistry": 97}
print(marks["English"])
marks["physics"] = 99
print(marks)

marks["physics"] = 78
print(marks)

# Function

def printSum(a,b=5):
    print(a + b)

printSum(1)