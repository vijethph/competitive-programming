class TrieNode:
    def __init__(self) -> None:
        self.nodes: dict[str, TrieNode] = {}
        self.is_leaf = False

    def insert_many(self, words: list[str]) -> None:
        for word in words:
            self.insert(word)

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def find(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def delete(self, word: str) -> None:
        def _delete(curr: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0
            char = word[index]
            char_node = curr.nodes.get(char)
            if not char_node:
                return False
            delete_char_node = _delete(char_node, word, index + 1)
            if delete_char_node:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_char_node

        _delete(self, word, 0)

    def print_words(node: TrieNode, word: str) -> None:
        if node.is_leaf:
            print(word, end=" ")
        for char, char_node in node.nodes.items():
            TrieNode.print_words(char_node, word + char)


if __name__ == "__main__":
    trie = TrieNode()
    trie.insert_many(["apple", "app", "ape", "ball", "bat"])
    print(trie.find("apple"))
    print(trie.find("app"))
    print(trie.find("ap"))
    print(trie.find("ape"))
    print(trie.find("ball"))
    print(trie.find("bat"))
    print(trie.find("b"))
    print(trie.find("ba"))
