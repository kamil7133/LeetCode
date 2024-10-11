def validAnagram(s, t):


    if len(s) != len(t): #first of all, if the words don't have same amount of letters
        return False

    s_dic = {}
    t_dic = {} #two empty dictionaries

    for char in s:
        s_dic[char] = s_dic.get(char, 0) + 1 #iterate every character in s and check if it is already in dictionary, if not adding +1

    for char in t:
        t_dic[char] = t_dic.get(char, 0) + 1#doing the same for word t

    return s_dic == t_dic #compared dictionaries

#testing
print(validAnagram("grey", "regy")) #expected result true
print(validAnagram("blue", "red")) #expected result false
