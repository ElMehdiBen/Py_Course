# Cassandra Exercices

### using session.execute("put your query here"):

1. Read the table called data from your Cassandra instance and transform the results to a Dataframe. (Done on Friday)

2. Create a table called COVID using some selected columns from COVID file

3. Insert row by row the data from your COVID file to your new COVID table in Cassandra

4. Read the table called data from your Cassandra, add 100 to each new_cases value and save it back to a new table called COVID_NEW. (You should already create COVID_NEW table). This question 4 simulates a whole ETL.