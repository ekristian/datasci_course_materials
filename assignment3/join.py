import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: book identifier
    # value: book contents
    aliases = {}
    aliases[u"order"] = "a"
    aliases[u"line_item"] = "b"
    key = record[1]
    value = (aliases[record[0]], record)
    # emit each record keyed by order_id
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # split list of values into aliases a and b
    for row_a in [a[1] for a in list_of_values if a[0]=='a']:
        for row_b in [b[1] for b in list_of_values if b[0]=='b']:
           mr.emit(row_a + row_b)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
