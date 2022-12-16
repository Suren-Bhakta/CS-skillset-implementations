#  File: Cypher.py

#  Description: decrypts a string of words

#  Student Name: Suren Bhakta

#  Student UT EID: ssb2943

#  Partner Name: Karim Ladak

#  Partner UT EID: kal3635

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 09/08/2022

#  Date Last Modified: 09/12/2022

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
import sys
import math


def encrypt(strng):
    L = len(strng)
    print(L)
    if 0 < L <= 100:
        z = (square(L))
        z = round(math.sqrt(z))
        a = "*"
        d = (z ** 2) - L
        while d > 0:
            strng += a
            d -= 1
        lstrng = []
        for l in strng:
            lstrng.append(l)
        w = [[0 for n in range(z)] for y in range(z)]
        row = 0
        count = 0

        # appends each character into list
        for x in range(len(lstrng)):
            i = 0
            for i in range(0, z):
                if count >= len(lstrng):
                    break
                while row <= z:
                    if i < z:
                        if w[row][i] == 0:
                            w[row][i] = lstrng[count]
                            count += 1
                            if count >= (L - 1):
                                break
                    if i >= z - 1:
                        row += 1
                    break
        # rotates list
        rw = [["" for n in range(z)] for y in range(z)]
        for x in range(z):
            for y in range(z):
                rw[y][z - x - 1] = w[x][y]
        # removes asterisks
        nm = ''
        for x in range(z):
            for y in range(z):
                nm += rw[x][y]
        nm = nm.replace("*", "")
        return nm


# Finds the closest square number
def square(length):
    for i in range(0, 101):
        if length > (i ** 2):
            pass
        if length <= (i ** 2):
            x = (i ** 2)
            break
    return x


# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string 
def decrypt(strng):
    L = len(strng)
    if 0 < L <= 100:
        z = (square(L))
        z = round(math.sqrt(z))
        a = "*"
        d = (z ** 2) - L
        lstrng = []
        for l in strng:
            lstrng.append(l)

        w = [[0 for n in range(z)] for y in range(z)]
        for y in range(z):
            if d == 0:
                break
            for x in range(z - 1, -1, -1):
                if d == 0:
                    break
                w[x][y] = a
                d -= 1
        for x in range(z):
            for y in range(z):
                if w[x][y] != "*":
                    w[x][y] = lstrng.pop(0)
        row = 0
        count = 0
        # appends each character into list
        for x in range(len(lstrng)):
            i = 0
            for i in range(0, z):
                if count >= (len(lstrng)):
                    break
                while row <= z:
                    if i < z:
                        if w[row][i] == 0:
                            w[row][i] = lstrng[count]
                            count += 1
                            if count >= (L - 1):
                                break
                    if i >= z - 1:
                        row += 1
                    break

        # rotates list
        rw = [["" for n in range(z)] for y in range(z)]
        for x in range(int(z)):
            for y in range(int(z)):
                rw[y][x] = w[x][y]
        rw = (rw[::-1])
        for x in range(z):
            for y in range(z):
                temp = rw[y][x]
                rw[y][x] = rw[x][y]
                rw[x][y] = temp
        nw = ""
        for x in range(z):
            for y in range(z):
                nw += rw[x][y]
        nw = nw.replace("*", "")
        return nw


def main():
    # read the strings P and Q from standard input
    data = sys.stdin.read()
    data_list = data.split("\n")
    data_list.remove('')
    P = data_list[0]
    # encrypt the string P
    x = encrypt(P)
    print(x)
    # print the encrypted string of P
    Q = data_list[1]
    print(decrypt(Q))


if __name__ == "__main__":
    main()
