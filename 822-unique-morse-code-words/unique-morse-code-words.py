class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse =[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapping = {chr(ord('a') + i): morse[i] for i in range(26)}
        s = set()
        for w in words:
            current = "".join((mapping[c] for c in w))
            if current  not in s:
                s.add(current)
            
        return len(s)