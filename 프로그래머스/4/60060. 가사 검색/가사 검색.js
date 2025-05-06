class TrieNode {
    constructor() {
        this.children = {};
        this.count = 0;
    }
    
    insert(word) {
        let node = this;
        node.count += 1;
        for (const ch of word) {
            if (!(ch in node.children)) {
                node.children[ch] = new TrieNode();
            }
            node = node.children[ch];
            node.count += 1;
        }
    }
    
    search(query) {
        let node = this;
        for (const ch of query) {
            if (ch === '?') {
                return node.count;
            }
            if (!(ch in node.children)) {
                return 0;
            }
            node = node.children[ch];
        }
        return node.count;
    }
}


function solution(words, queries) {
    const answer = [];
    const trieByLen = {};
    const reversedTrieByLen = {};
    
    for (const word of words) {
        const len = word.length;
        if (!trieByLen[len]) {
            trieByLen[len] = new TrieNode();
            reversedTrieByLen[len] = new TrieNode();
        }
        trieByLen[len].insert(word);
        reversedTrieByLen[len].insert([...word].reverse().join(""));   
    }
    
    for (const query of queries) {
        const len = query.length;
        if (!trieByLen[len]) {
            answer.push(0);
            continue;
        }

        if (query[0] !== '?') {
            answer.push(trieByLen[len].search(query));
        } else {
            const reversedQuery = [...query].reverse().join('');
            answer.push(reversedTrieByLen[len].search(reversedQuery))
        }
    }
    return answer;
}