# You are given a function . You are also given  lists. The  list consists of  elements.

# You have to pick one element from each list so that the value from the equation below is maximized:

# %

#  denotes the element picked from the  list . Find the maximized value  obtained.

#  denotes the modulo operator.

# Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

# Input Format

# The first line contains  space separated integers  and .
# The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

# Sample input
# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 

def maximizeIt(modulo, rows):
    newRows = []
    sMax = 0
    rowsAmount = len(rows)
    for row in rows:
        newRows.append(list(map(int, row.split(' '))))
    
    rowsLength= []
    currentIndicies = []
    combinations = 1
    
    for row in newRows:
        combinations *= row[0]
    
    for idx in range(0, rowsAmount):
        rowsLength.append(len(newRows[idx]) - 1)
        currentIndicies.append(1)
        
    allCombinations = []
    for combination in range(1, combinations + 1):
        combo = []
        for rowIdx in range(0, len(newRows)):
            number = newRows[rowIdx][currentIndicies[rowIdx]]
            combo.append(number)
            M = 1
            for k in range(rowIdx, len(newRows) - 1):
                M = M * rowsLength[k + 1]
            if combination % M == 0:
                if currentIndicies[rowIdx] < rowsLength[rowIdx]:
                    currentIndicies[rowIdx] += 1
                else:
                    currentIndicies[rowIdx] = 1
        allCombinations.append(combo)
        
    result = 0
    for array in allCombinations:
        tempResult = 0
        for el in array:
            tempResult += el**2  
        tempResult = tempResult % modulo
        if result  < tempResult:
            result = tempResult
    print(result)        
        
    
            
if __name__ == '__main__':
    k_m = input()
    k_m = list(map(int, k_m.split(' ')))
    k, m = k_m[0], k_m[1]
    rows = [];
    for i in range(0, k):
        rows.append(input())

    maximizeIt(m, rows)
