import re
from collections import namedtuple

"""
Class to search for the Trie keys in the given text

"""
resulttuple=namedtuple("trieresult","text line word")
class TrieSearch():
    def __init__(self, trie=None, splitter=r'\s+'):
        self.splitter = splitter
        self.trie=trie
    def remove_punc(self,w):
        return re.sub(r'[^\w\s]', '', w) if w else w
    def search_text(self, text):
        """
        :param text:
        :return: a tuple( [word(s), line, word] ) for each match.

        The exact match is performed for the full word ( may include spaces)

        This class is not generic but based on the exercise requirements
        """
        line_idx = 0
        results=[]
        for line in re.split(r'[\n\r]', text):
            line_idx +=1
            if self.splitter:
                words = re.split(self.splitter, line)
            else:
                words = line
            word_idx = 0

            while len(words)>=1:
                #remove punctuation
                w=words.pop(0)
                word_idx += 1

                w = self.remove_punc( w)

                if not w:
                    continue
                wordnode=self.trie.get_node(w)
                if wordnode is   None:
                    continue
                fnd=[w]
                while wordnode is not None:
                    if wordnode.value_valid:
                        break #terminal
                    if not wordnode.value_valid and len(words):
                        nxt=self.remove_punc(words[0])
                        if nxt in wordnode.path:
                            words.pop(0)
                            word_idx += 1
                            fnd.append(nxt)
                            wordnode=wordnode.get_node(nxt)
                        else:
                            break
                    else:
                        break
                if fnd:
                    results.append(resulttuple((" ").join(fnd),line_idx,word_idx))
        return results
