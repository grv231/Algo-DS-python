# Testing panagram
def testPanagram(str1,str2):
    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()

    # Checking edge cases
    if len(s1) != len(s2):
        return False

    if s1 =='' and s2 =='':
        return True

    # Using dictionary for keeping a count of unique items in strings
    count = {}

    # Check frequencey of each letters in both string 1 and string 2
    for letter in s1:
        if letter in count:
            count[letter] += 1

        else:
            count[letter] = 1

    # Looping in string 2 and checking against dictionary
    for letter in s2:
        if letter in count:
            count[letter] -= 1

        else:
            count[letter] = 1

    # Finally checking the dictionary items
    for k in count:
        if count[k] != 0:
            return False

        else:
            return True

# Driver Code for checking panagrams (paragraph anagrams)
if __name__=='__main__':
    print(testPanagram('My name is John','name IS my NOJH'))