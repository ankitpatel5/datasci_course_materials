Database Assignment: Simple In-Database Text Analytics:
=======================================================

For most of these problems, you will use the reuters.db database consisting of a single table:
frequency(docid, term, count)

where docid is a document identifier corresponding to a particular file of text, term is an English word, and count is the number of the occurrences of the term within the document indicated by docid.

Problem 1: Inspecting the Reuters Dataset; Basic Relational Algebra
-------------------------------------------------------------------
(a) select: Write a query that is equivalent to the following relational algebra expression.

σ 10398_txt_earn(frequency)


(b) select project: Write a SQL statement that is equivalent to the following relational algebra expression.

π term ( σ docid=10398_txt_earn and count=1(frequency))

(c) union: Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL)

π term( σ docid=10398_txt_earn and count=1(frequency)) U π term( σ docid=925_txt_trade and count=1(frequency))

(d) count: Write a SQL statement to count the number of documents containing the word "parliament"

(e) big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)

(f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.

Problem 2: Matrix Multiplication in SQL
---------------------------------------
Sparse matrix has many positions with a value of zero.

Systems designed to efficiently support sparse matrices look a lot like databases: They represent each cell as a record (i,j,value).

The benefit is that you only need one record for every non-zero element of a matrix.

Within matrix.db, there are two matrices A and B represented as follows:

A(row_num, col_num, value)

B(row_num, col_num, value)

The matrix A and matrix B are both square matrices with 5 rows and 5 columns each.

(g) multiply: Express A X B as a SQL query

If you're wondering why this might be a good idea, consider that advanced databases execute queries in parallel automatically. So it can be quite efficient to process a very large sparse matrix --- millions of rows or columns --- in a database. But a word of warning: In a job interview, don't tell them you recommend implementing linear algebra in a database. You won't be wrong, but they won't understand databases as well as you now do, and therefore won't understand when and why this is a good idea. Just say you have done some experiments using databases for analytics, then mention the papers in the reading if they seem incredulous!

Problem 3: Working with a Term-Document Matrix
-----------------------------------------------

The reuters dataset can be considered a term-document matrix, which is an important representation for text analytics.

Each row of the matrix is a document vector, with one column for every term in the entire corpus. Naturally, some documents may not contain a given term, so this matrix is rather sparse. The value in each cell of the matrix is the term frequency. (You'd often want this this value to be a weighted term frequency, typically using "tf-idf": term frequency - inverse document frequency. But we'll stick with the raw frequency for now.)

What can you do with the term-document matrix D? One thing you can do is compute the similarity of documents. Just multiply the matrix with its own transpose S = DDT, and you have an (unnormalized) measure of similarity.

The result is a square document-document matrix, where each cell represents the similarity. Here, similarity is pretty simple: if two documents both contain a term, then the score goes up by the product of the two term frequencies. This score is equivalent to the dot product of the two document vectors.

To normalize this score to the range 0-1 and to account for relative term frequencies, the cosine similarity is perhaps more useful. The cosine similarity is a measure of the angle between the two document vectors, normalized by magnitude. You just divide the dot product by the magnitude of the two vectors. However, we would need a power function (x^2, x^(1/2)) to compute the magnitude, and sqlite has built-in support for only very basic mathematical functions. It is not hard to extend sqlite to add what you need, but we won't be doing that in this assignment.

(h) similarity matrix: Write a query to compute the similarity matrix DDT. (Hint: The transpose is trivial -- just join on columns to columns instead of columns to rows.) The query could take some time to run if you compute the entire result. But notice that you don't need to compute the similarity of both (doc1, doc2) and (doc2, doc1) -- they are the same, since similarity is symmetric. If you wish, you can avoid this wasted work by adding a condition of the form a.docid < b.docid to your query. (But the query still won't return immediately if you try to compute every result -- don't expect otherwise.)

You can also use this similarity metric to implement some primitive search capabilities. Consider a keyword query that you might type into Google: It's a bag of words, just like a document (typically a keyword query will have far fewer terms than a document, but that's ok).

So if we can compute the similarity of two documents, we can compute the similarity of a query with a document. You can imagine taking the union of the keywords represented as a small set of (docid, term, count) tuples with the set of all documents in the corpus, then recomputing the similarity matrix and returning the top 10 highest scoring documents.

(i) keyword search: Find the best matching document to the keyword query "washington taxes treasury". You can add this set of keywords to the document corpus with a union of scalar queries:

SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count

Then, compute the similarity matrix again, but filter for only similarities involving the "query document": docid = 'q'. Consider creating a view of this new corpus to simplify things.
