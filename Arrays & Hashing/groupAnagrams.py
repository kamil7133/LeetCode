class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {} #empty hashmap for exclusive keys and values

        for word in strs: #iterate every word in input
            sorted_word = "".join(sorted(word)) #sorting every word and making it string

            if sorted_word not in anagrams:
                anagrams[sorted_word] = [] #create empty list for key

            anagrams[sorted_word].append(word) #add original word to anagram list

        return list(anagrams.values()) #returnig words from hashmap back to list of lists

#test
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) #expected result [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(solution.groupAnagrams([""])) #expected result [['']]
print(solution.groupAnagrams(["a"])) #expected result [['a']]
