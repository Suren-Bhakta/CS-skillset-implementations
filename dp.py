import sys


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




    result =  max(money, num_houses, prices, increase) 



    print(result)

    
main()
