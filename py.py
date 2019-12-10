 
"""
n = int(input("Digite um número: "))

i = 0

while i < n:
    print (i**2)
    i+=1

n = int(input()) *range (1, n+1) = range is from 1 to n, exclusive of n. so if your input is 3 then it prints 1 2. So input to the range function is 1 to n+1

if you don't give sep='' in print statement then each value is seperated by a space

int(input("Digite um número: "))

n = int(input("Digite um número: "))

print(*range(1, n+1), sep='')

ListOfNumbers = [ x for x in range(10) ]
print (ListOfNumbers)

ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
ListOfThreeMultiples
print (ListOfThreeMultiples)


	Looks good, but to avoid those repetitive input calls you could do something like:

x, y, z, n = (int(input()) for _ in range(4))


x, y, z, n = (int(input()) +1 for inp in range (4))
print ([[i,j,k] for i in range(x) for j in range(y) for k in range(z) if i + j + k != n -1 ])

"""
'''
@HAMZA_SHAKEEL First two lists are created as marksheet and scorelist. marksheet is used to store the values of all the inputs more like a dictionary while the scorelist recores only the scores.
input is put into the range() to make sure there are enough inputs taken for all the inputs gievn and also because we camt be so sure about th amount of inputs.
Then the scores, marks are stored by marksheet+=[[name,score]] scorelist+=[score]
sorted() is a function used to sort the list items in the accending order. Check this link for more info. https://docs.python.org/3/howto/sorting.html
b=sorted(list(set(scorelist)))[1] The second lowest score is taken out to the element b by the index[1].
Then for a,c (a and c are used for the loop process. Nothing special with the functionality of the programme) in the range, all the names which bears the score b is printed.
And a special note must be made, this may look like its forgetting that the test cases might have more than one lowest score. That issue has been addressed by the use of set(). A set does not have duplicate items. Therefore the check is valid and accurate.

please help what is the meaning of sorted(marksheet)
it is used to sort the list....in this case it will arrange the names in marksheet alphabetically.
a,c represent name,score in marksheet
'''

'''
marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        b=sorted(list(set(scorelist)))[1] 

        for a,c in sorted(marksheet):
             if c==b:
                    print(a)



    marklist=[[input(""),float(input(""))] for i in range(int(input("")))]
print("\n".join(a for a,b in sorted(marklist) if b==sorted(list(set([b for a,b in marklist])))[1]))
'''
#python map() is an iterator.so that we can iterate over elements. can be converted to tuple ,lists
#map is also very usefull to use lambda functinons and it applies function to all items in the input list

'''
n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i=0
while(i<n):
    if zes ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))


    n = int(input())

    arr = list(map(int, input().split()))

    listnew=[]

    for i in arr:

         if i not in listnew:


                    listnew.append(i)

    listnew.sort(reverse=True)

    print(listnew[1])
'''
'''
def swap_case(s):   
    return s.swapcase()

s = "OI eu SOU mara"

result = swap_case(s)
print (result)
'''
'''
a = "mara"
b = "rosa" 

print("Hello ",a," ",b,"! You just delved into python.",sep="")

'''
#print("Hello " + a + " " + b +"! You just delved into python.")

#Explanation : Actually, here trinadhkoya is converting input string to list.....then replace list index value with new element and again convert list to string using joint syntex.

string = str(input());

list1 = list(string);

replace = list(input().split());

list1[int(replace[0])]=replace[1];

string = ''.join(list1);

print(string)