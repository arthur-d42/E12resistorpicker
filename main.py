from pyperclip import copy
E12 = [10,12,15,18,22,27,33,39,47,56,68,82]

print("This program calculates the resistors needed for a specified gain on an OP-amp\nOr just a desired fraction")
print("Resistors in the E12 series")
print(E12)
magnitude = float(input("Factor of resistors to add?\ndefault = 10-82\ninput only powers of 10 to stay in E12 series:  "))#append magnitude to append of E12
for i in range(len(E12)):
    E12.append(E12[i]*magnitude)
print("Your resistors:")
print(E12)
amount = len(E12)#amount of resistors

gain = []
Rval = []

print("For a fraction value of R1/R2 (useful in dividers) input 1\nFor a fraction value of -R2/R1 (inverting opamp) input 2\nFor a fraction value of 1+R2/R1 (noninverting opamp) input 3 ")

fraction = int(input())

desiredval = float(input("Desired gain/fraction:  "))
margin = float(input("Margin input in float aka 0.05 for 5%:  "))

mapleinput = []
closegains = {} #TODO multiple values for one key
listoflists = []

for i in range(amount):
    R2 = E12[i]#def R2
    for k in range(amount):#will now iterate amount^2 times big O = n^2 watch out!!
        R1 = E12[k]#def R1
        if fraction == 1:
            gain.append(R1/R2)
        elif fraction == 2:
            gain.append(-R2/R1)
        elif fraction == 3:
            gain.append(1+(R2/R1))


        Rval.append([R1,R2])

dick = {}#creates a dictionary with gains as keys to resistances in list. Note:only last iteration of value and gain will appear if more than 1 combination is possible. This means that for a gain of 2 the value will be R1=820 and R2=820. This is not a problem seeing as you can always divide with magnitude
for i in range(len(gain)):
    dick.update({gain[i]:Rval[i]})


i = 0

while (i < len(Rval)):#same as amount^2
    if gain[i] < desiredval*(1+margin) and gain[i] > desiredval*(1-margin):#If between margins
        k= len(mapleinput)+1 #Indexnumber for maplecopy
        print("__________________________" + str(k) + "__________________________")
        print("for gain of:  " + str(gain[i]))
        print("R1=" + str(Rval[i][0]) + "  R2=" + str(Rval[i][1]))
        print("Varying from desired value with  " + str((1-gain[i]/desiredval)*100) + "%")
        print("____________________________________________________\n\n")
        mapleinput.append("R[1],R[2]:=" + str(Rval[i][0]) + "," + str(Rval[i][1]) + ":")
    if i == len(Rval)-1:
        print("No more values found.... if none were found you should try again")
        print("try again with different margin? y/n")
        ask = input()
        if ask == "y":
            margin = float(input("Input new margin  "))
            i = -1
    i += 1
    #print(i)
def maplecopy(x):#copies maple input
    copy(mapleinput[x-1])
print("For maplecopy input index")
maplecopy(int(input()))

input("press enter to exit program")
