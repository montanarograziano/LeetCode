class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.end = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end == True
    
    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    def findSP(self, word):
        cur = self.root
        shortest_prefix = ""
        for c in word:
            if cur.end:
                return shortest_prefix
            if c not in cur.children:
                return word
            shortest_prefix += c
            cur = cur.children[c]
        return word




class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split()
        res = []
        for word in words:
            prefix = trie.findSP(word)
            res.append(prefix)
        
        return ' '.join(res) if res else ""
