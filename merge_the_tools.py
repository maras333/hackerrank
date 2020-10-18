# Consider the following:

# A string, s, of length n where s = c0c1....cn-1.
# An integer, k, where k is a factor of n.
# We can split s into n/k subsegments where each subsegment, t_i, consists of a contiguous block of k characters in s. Then, use each t_i to create string  such that:

# The characters in u_i are a subsequence of the characters in t_i.
# Any repeat occurrence of a character is removed from the string such that each character in u_i occurs exactly once. In other words, if the character at some index j in t_i occurs at a previous index < j in t_i, then do not include the character in string u_i.
# Given s and k, print n/k lines where each line i denotes string u_i.

# Input Format

# The first line contains a single string denoting s.
# The second line contains an integer, k, denoting the length of each subsegment.

# Constraints

# 1 <= n <= 10^4, where n is the length of s
# 1 <= k <= n
# It is guaranteed that n is a multiple of k.
# Output Format

# Print n/k lines where each line i contains string u_i.

def merge_the_tools(string, k):
    stringLength = len(string)
    numberOfParts = int(stringLength / k)
    for idx in range(0, numberOfParts):
        subsegment = string[k*idx : k+k*idx]
        subsegment = list(dict.fromkeys(subsegment))
        print(''.join(subsegment))
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)