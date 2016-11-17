#The first line of input contains the original string. The next line contains the substring.
#Output the integer number indicating the total number of occurrences of the substring in the original string. 
#
S = raw_input() s = raw_input() total = 0   for i in range(0, len(S) - len(s) + 1):     if S[i:i+len(s)] == s:         total += 1  print total 
