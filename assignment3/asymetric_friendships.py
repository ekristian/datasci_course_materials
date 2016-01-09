import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key0: Person, Friend Relationship
    # key1: Friend, Person Relationship 
    # value: Original Record
    
    key0 = ",".join(record)
    key1 = ",".join(reversed(record))

    mr.emit_intermediate(key1, 1)
    mr.emit_intermediate(key0, 1)

def reducer(key, list_of_values):
    # key: Person + Friend, or Friend + Person
    # value: Original Friend Record
    # if the length of the list_of_values is 1,
    # there musn't be a reciprical relationship
    if len(list_of_values) == 1:
        person, friend = key.split(",")
        mr.emit((person, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
