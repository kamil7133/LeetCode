class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        dic = self.trie

        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]

        dic["."] = "."

    def search(self, word: str) -> bool:
        dic = self.trie
        for ch in word:
            if ch not in dic:
                return False
            dic = dic[ch]

        return "." in dic

    def startsWith(self, prefix: str) -> bool:
        dic = self.trie
        for ch in prefix:
            if ch not in dic:
                return False
            dic = dic[ch]

        return True

# Your Trie object will be instantiated and called as such::
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)