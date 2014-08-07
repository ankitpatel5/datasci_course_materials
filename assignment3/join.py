import MapReduce
import sys

"""
Implementation of a relational join as a MapReduce query 
in the Simple Python MapReduce Framework

Consider the following query:

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
"""

mr = MapReduce.MapReduce()

# =============================

def mapper(record):
    # record[1]: order id
    orderID = record[1]
    mr.emit_intermediate(orderID, record)

def reducer(key, list_of_collections):
    # key: order id
    # value: collection of records from orders catalog or line_item catalog
    
    #grab the order collection
    order_collection = []
    for c in list_of_collections:
        if c[0] == 'order':
            order_collection = c
            break
    
    #combine order collection with each line_item collection
    for c in list_of_collections:
        if c[0] == 'line_item':
            line_item_collection = c
            mr.emit(order_collection + line_item_collection)

# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
