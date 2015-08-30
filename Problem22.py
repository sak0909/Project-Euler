#!/usr/local/bin/python3

#Solution to Problem 22: Names scores
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?  
#


def value(word):
    count = 0
    for i in word:
        count += ( ord(i) - (ord('A') - 1) )
    return count
    
def solve():
    f = open('p022_names.txt')
    names = f.readline()
    f.close()

    list_names = names.split('","')
    #Remove extra '"' chars in the first and last words
    list_names[0] = list_names[0][1:]
    list_names[len(list_names) - 1] = list_names[len(list_names) - 1][:-1]

    sorted_list = sorted(list_names)

    pos = 1
    total = 0
    for word in sorted_list:
        total += ( pos *  value(word) )
        pos += 1

    print (total, pos)

solve()
    
