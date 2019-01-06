'''
Practice/Algorithms/Strings/TwoStrings
Task:
  Given two strings, return true if share common substring. A substring may be as small as one character. 
'''
word1 = 'python'

word2 ='wython'

letter = set()
for i in word1:

    for k in word2:

        if i == k:
            letter.add(str(i))

print(letter)

print('Both words have a common substring of length: ' + str(len(letter)))


'''

use a set - recall sets are NON-DUPLICATE

'''
