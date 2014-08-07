Algorithms in MapReduce:
========================

In this assignment, you will be designing and implementing MapReduce algorithms for a variety of common data processing tasks.  


The MapReduce programming model (and a corresponding system) was proposed in a 2004 paper from a team at Google as a simpler abstraction for processing very large datasets in parallel.  The goal of this assignment is to give you experience “thinking in MapReduce.”  We will be using small datasets that you can inspect directly to determine the correctness of your results and to internalize how MapReduce works.  In the next assignment, you will have the opportunity to use a MapReduce-based system to process the very large datasets for which it was designed.


Python MapReduce Framework

You will be provided with a python library called MapReduce.py that implements the MapReduce programming model. The framework faithfully implements the MapReduce programming model, but it executes entirely on a single machine -- it does not involve parallel computation.

Problem 1: Create an Inverted index
-----------------------------------
Given a set of documents, an inverted index is a dictionary where each word is associated with a list of the document identifiers in which that word appears.

Mapper Input
The input is a 2 element list: [document_id, text], where document_id is a string representing a document identifier and text is a string representing the text of the document. The document text may have words in upper or lower case and may contain punctuation. You should treat each token as if it was a valid word; that is, you can just use value.split() to tokenize the string.

Reducer Output
The output should be a (word, document ID list) tuple where word is a String and document ID list is a list of Strings.

Problem 2: Implement a relational join as a MapReduce query
-----------------------------------------------------------

Consider the following query:

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id
Your MapReduce query should produce the same result as this SQL query executed against an appropriate database.

You can consider the two input tables, Order and LineItem, as one big concatenated bag of records that will be processed by the map function record by record.

Map Input
Each input record is a list of strings representing a tuple in the database. Each list element corresponds to a different attribute of the table

The first item (index 0) in each record is a string that identifies the table the record originates from. This field has two possible values:

"line_item" indicates that the record is a line item.
"order" indicates that the record is an order.
The second element (index 1) in each record is the order_id.

LineItem records have 17 attributes including the identifier string.

Order records have 10 elements including the identifier string.

Reduce Output
The output should be a joined record: a single list of length 27 that contains the attributes from the order record followed by the fields from the line item record. Each list element should be a string.

Problem 3: Social Network Friends
---------------------------------

Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person.

Map Input
Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB.

Reduce Output
The output should be a pair (person, friend_count) where person is a string and friend_count is an integer indicating the number of friends associated with person.

Problem 4: Non-symmetric Friend Relationships in Social Network
---------------------------------------------------------------

The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships.

Map Input
Each input record is a 2 element list [personA, personB] where personA is a string representing the name of a person and personB is a string representing the name of one of personA's friends. Note that it may or may not be the case that the personA is a friend of personB.

Reduce Output
The output should be the full symmetric relation. For every pair (person, friend), you will emit BOTH (person, friend) AND (friend, person). However, be aware that (friend, person) may already appear in the dataset, so you may produce duplicates if you are not careful.

Problem 5: Sequence ID and Nucleotides Parsing
----------------------------------------------

Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.

Map Input
Each input record is a 2 element list [sequence id, nucleotides] where sequence id is a string representing a unique identifier for the sequence and nucleotides is a string representing a sequence of nucleotides

Reduce Output
The output from the reduce function should be the unique trimmed nucleotide strings.

Problem 6 - Matrix Multiplicatoin in MapReduce
----------------------------------------------

Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute the matrix multiplication A x B

Map Input
The input to the map function will be a row of a matrix represented as a list. Each list will be of the form [matrix, i, j, value] where matrix is a string and i, j, and value are integers.

The first item, matrix, is a string that identifies which matrix the record originates from. This field has two possible values: "a" indicates that the record is from matrix A and "b" indicates that the record is from matrix B

Reduce Output
The output from the reduce function will also be a row of the result matrix represented as a tuple. Each tuple will be of the form (i, j, value) where each element is an integer.
