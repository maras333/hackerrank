# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
# For each  integer in the array, if , you add 1 to your happiness. If , you add -1 to your happiness. 
# Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Constraints



# Input Format
# 3 2
# 1 5 3
# 3 1
# 5 7

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain  integers, A and B, respectively.

# Output Format
# 1

# Output a single integer, your total happiness.

def getHappiness(n_m, arrayN, aSet, bSet):
    n_m = list(map(int, n_m.split(' ')))
    arrayN = list(map(int, arrayN.split(' ')))
    aSet = set(map(int, aSet.split(' '))) #like
    bSet = set(map(int, bSet.split(' '))) #dislike
    
    n, m = n_m[0], n_m[1]
    
    print(sum([(i in aSet) - (i in bSet) for i in arrayN]))
            
if __name__ == '__main__':
    n_m = input()
    arrayN = input()
    aSet = input()
    bSet = input()
    getHappiness(n_m, arrayN, aSet, bSet)
