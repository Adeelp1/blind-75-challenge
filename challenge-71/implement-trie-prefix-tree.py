from collections import defaultdict

class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.is_end = False

class Trie:

    def __init__(self):
        self.trie = TreeNode()

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.find_word(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.find_word(prefix) is not None
    
    def find_word(self, word: str):
        node = self.trie

        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# TC : O(N)
# SC : O(K * N)