import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: alias + entire row contents
    # Create an alias value to utilize in the Reducer
    # This will allow the reducer to remain unchanged
    # even if the input tables change.
    aliases = {}
    aliases[u"order"] = "a"
    aliases[u"line_item"] = "b"

    # Assign key the value of the order_id field
    key = record[1]
    value = (aliases[record[0]], record)

    # emit each record keyed by order_id
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: N/A
    # value: list of a and b records with matching order_id values
    # split list of values into aliases a and b
    # This creates an implicit join condition
    for row_a in [a[1] for a in list_of_values if a[0]=='a']:
        for row_b in [b[1] for b in list_of_values if b[0]=='b']:
           mr.emit(row_a + row_b)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
