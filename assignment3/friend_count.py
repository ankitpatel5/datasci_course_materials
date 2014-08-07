import MapReduce
import sys

"""
@author: Ankit Patel

Describes a MapReduce algorithm to count the number of friends 
for each person in a simple social network dataset consisting 
of a set of key-value pairs (person, friend) representing a friend 
relationship between two people.

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    key = record[0]
    #one friend connections found, emit data
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: person
    # value: list of 1s
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
