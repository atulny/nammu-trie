# 	A simple Trie implementation written in Python.
#  the Trie is built for word tokens .. not characters
#  emulates the behaviour of a dict
#  when assigning a value ..
#   the key is tokenized and corresponding nodes are added

import re
class Trie:
    def __init__(self):
        self.path = {}
        self.value = None
        self.value_valid = False # True indicates terminal token
    def get_tokens(self,key):
        return re.split(r'\s+',key)  if type(key) is str else key
    def set(self, words, value):
        key=self.get_tokens(words)
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            node.__setitem__(remains, value)
        else:
            node.value = value
            node.value_valid = True

    def get_node(self, words):
        key = self.get_tokens(words)
        head = key[0]
        node=None
        if head in self.path:
            node = self.path[head]
        else:
            return None
        if len(key) > 1:
            remains = key[1:]
            sub=node.get_node(remains)
            if sub is not None:
                node=sub
        return node

    def get_(self, words):
        key=self.get_tokens(words)
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            raise KeyError(key)
        if len(key) > 1:
            remains = key[1:]
            try:
                return node.__getitem__(remains)
            except KeyError:
                raise KeyError(key)
        elif node.value_valid:
            return node.value
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, words):
        key=self.get_tokens(words)
        head = key[0]
        if head in self.path:
            node = self.path[head]
            if len(key) > 1:
                remains = key[1:]
                node.__delitem__(remains)
            else:
                node.value_valid = False
                node.value = None
            if len(node) == 0:
                del self.path[head]

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
        except KeyError:
            return False
        return True

    def __len__(self):
        n = 1 if self.value_valid else 0
        for k in self.path.keys():
            n = n + len(self.path[k])
        return n

    def get(self, key, default=None):
        try:
            return self.get_(key)
        except KeyError:
            return default

    def nodeCount(self):
        n = 0
        for k in self.path.keys():
            n = n + 1 + self.path[k].nodeCount()
        return n

    def keys(self, prefix=()):
        return self.__keys__(prefix)

    def __keys__(self, prefix=(), seen=()):
        result = []
        if self.value_valid:
            isStr = True
            val = ""
            for k in seen:
                if type(k) != str :
                    isStr = False
                    break
                else:
                    val += " "+k
            if isStr:
                result.append(val)
            else:
                result.append(list(prefix))
        if len(prefix) > 0:
            head = prefix[0]
            prefix = prefix[1:]
            if head in self.path:
                nextpaths = [head]
            else:
                nextpaths = []
        else:
            nextpaths = self.path.keys()
        for k in nextpaths:
            nextseen = []
            nextseen.extend(list(seen))
            nextseen.append(k)
            result.extend(self.path[k].__keys__(prefix, nextseen))
        return result

    def __iter__(self):
        for k in self.keys():
            yield k
        raise StopIteration

    def __add__(self, other):
        result = Trie()
        result += self
        result += other
        return result

    def __sub__(self, other):
        result = Trie()
        result += self
        result -= other
        return result

    def __iadd__(self, other):
        for k in other:
            self[k] = other[k]
        return self

    def __isub__(self, other):
        for k in other:
            del self[k]
        return self
