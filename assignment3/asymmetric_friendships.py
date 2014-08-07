import MapReduce
import sys

"""

The relationship "friend" is often symmetric, meaning 
that if I am your friend, you are my friend. Here we
implement a MapReduce algorithm to check whether this 
property holds and generate a list of all non-symmetric 
friend relationships.

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person = record[0]
    friend = record[1]
    #friend connections found, emit data
    mr.emit_intermediate((person, friend),1)
    mr.emit_intermediate((friend, person),0)
    

def reducer(key, list_of_values):
    # key: (person,friend) pair
    # value: list of # of references: 1 if one way friendship, 2 if symmetric friendship
    if len(list_of_values) < 2:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
