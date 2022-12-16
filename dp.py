#  File: naximum_profit.py

#  Description: Recursive function that will generate all the possible combinations of houses and returns the maximum profit within budget

#  Student Name: Suren Bhakta

#  Student UT EID: ssb2943

#  Partner Name: Karim Ladak

#  Partner UT EID: kal3635

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 11/22/2022

#  Date Last Modified: 11/28/2022



import sys

# Add Your functions here
# this function will find the subset with the most houses that will stay under or equal to budget
def max(money, num_houses, prices, increase):
    tup = [(price, exp) for price, exp in zip(prices, increase)]
    res = arrange(tup)
    max = -100000000000000
    for item in res:
        if sum(x for x , y in item) <= money:
            tot=sum(x*y*0.01 for x,y in item)
            if tot>max:
                max=tot
    return round(max,2)
def arrange(final):
    if not final:
        return [[]]
    profit = arrange(final[:-1])
    res=[]
    for c in profit:
        res+=[c+[final[-1]]]
    return profit + res

# You are allowed to change the main function. 

# Do not change the template file name. 


def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
   

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])



# Add your implementation here .... 
    result =  max(money, num_houses, prices, increase) 

# Add your functions and call them to generate the result. 

    print(result)

    
main()
