import MapReduce
import sys

"""
@author: Ankit Patel

Creates an Inverted index in the Simple Python MapReduce Framework

Given a set of documents, an inverted index is a dictionary where each word 
is associated with a list of the document identifiers in which that word appears.

"""

mr = MapReduce.MapReduce()

# =============================

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    
    #remove duplicates
    wordsNoDuplicates = []
    for word in words:
        if word not in wordsNoDuplicates:
            wordsNoDuplicates.append(word)

    for w in wordsNoDuplicates:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents that contains the word
    mr.emit((key, list_of_values))

# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
