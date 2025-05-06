"""
가사에 특정 키워드가 몇 개 포함되었는지 찾아달라
? : 패턴, 글자수는 동일해야 함
가사 단어: 오직 알파벳 소문자로 이루어짐, 특수문자/숫자 X
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # 현재 노드까지 지나간 단어 수 (접두사의 개수)
        
    def insert(self, word):
        node = self
        node.count += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
            
    def search(self, query):
        node = self
        for ch in query:
            if ch == "?":
                return node.count  # 지금까지 누적된 접두사 수 반환
            if ch not in node.children:
                return 0  # 일치하는 단어 없음
            node = node.children[ch]
        return node.count
    

def solution(words, queries):
    answer = []
    trie_by_len = {}
    reversed_trie_by_len = {}
    
    for word in words:
        l = len(word)
        if l not in trie_by_len:
            trie_by_len[l] = TrieNode()
            reversed_trie_by_len[l] = TrieNode()
        trie_by_len[l].insert(word)
        reversed_trie_by_len[l].insert(word[::-1])
            
    for query in queries:
        l = len(query)
        if l not in trie_by_len:
            answer.append(0)
            continue
        if query[0] != '?':
            res = trie_by_len[l].search(query)
        else:
            res = reversed_trie_by_len[l].search(query[::-1])
            
        answer.append(res)
    return answer