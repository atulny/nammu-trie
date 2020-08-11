#!/usr/bin/python3
from triesearch import TrieSearch
from trie import Trie
import pprint


test="""The operations of each Borrower, and the activities of the officers and directors and, to the knowledge of each Borrower, 
any Subsidiaries of the Borrowers, employees, agents and representatives of each Borrower, while acting on behalf of such 
Borrower, and to the knowledge of each Borrower the operations of each Material Project Party in relation to the Project, 
have been conducted at all times in compliance with all applicable Anti-Money Laundering Laws, Sanctions, and Anti-Corruption 
Laws. Neither Borrower, nor any Subsidiaries of the Borrowers, nor any officer or director or, to the knowledge of any Borrower, 
Affiliates, employee, agent or representative of either Borrower has engaged, directly or indirectly, in any activity or conduct 
which would violate any Anti-Corruption Laws or Anti-Money Laundering Laws. Neither Borrower nor any Subsidiaries of the Borrowers, 
nor any officer or director or, to the knowledge of any Borrower, Affiliates, employee, agent or representative of either Borrower 
has engaged, directly or indirectly, in any dealings or transactions with, involving or for the benefit of a Sanctioned Person,
or in or involving a Sanctioned Country, where such dealings or transactions would violate Sanctions, in the five (5) year period
immediately preceding the date hereof."""

Keys="""Borrower
Subsidiaries
Material Project Party
Project
Project Manager
Anti-Money Laundering Laws
Sanctions
Anti-Corruption Laws
Affiliates
Sanctioned Person
Sanctioned Country
Person
Officer
Director
Agents""".split("\n")

def dump(t):
    print ("trie keys:")
    for k in t.keys():
        if k:
            print ("  t[%s] => %s" % (k, t[k]))


"""  test """

t = Trie()
for k in Keys:
    t[k] = True

ts = TrieSearch(trie=t)
#dump all keys
#dump(t)

#returns a tuple for each match
results=ts.search_all_patterns(test)

pprint.pprint(results)


