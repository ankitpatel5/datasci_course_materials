import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, 
where each record is of the form i, j, value. Design a MapReduce 
algorithm to compute the matrix multiplication A x B
"""

mr = MapReduce.MapReduce()

resultingMatrix_rows = [0,1,2,3,4]
resultingMatrix_cols = [0,1,2,3,4]


# =============================
# Do not modify above this line

def mapper(record):
    # record[0] : matrix label ("a" or "b")
    # record[1] : row
    # record[2] : col
    # record[3] : val
    
    table = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    
    if table == 'a':
        for c in resultingMatrix_cols:
            mr.emit_intermediate((row, c), record)
    elif table == 'b':
        for r in resultingMatrix_rows:
            mr.emit_intermediate((r,col), record )


def reducer(key, list_of_values):
    # key: index of the resultant
    # value: list of records needed to compute the value
    #do the matrix multiplication

    resultVal = 0
    for aCol in range(5):
        A_val = 0
        B_val = 0
        #find record of interest in A
        for v in list_of_values:
            if (v[0] == 'a' and v[2] == aCol):
                A_val = v[3]
                
        #find matching record of interest in B
        for v in list_of_values:
            if (v[0] == 'b' and v[1] == aCol):
                B_val = v[3]

        resultVal = resultVal + (A_val * B_val)
    mr.emit(key + (resultVal,))
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
