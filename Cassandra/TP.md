# TP Cassandra


## Data

Link : https://www.kaggle.com/sveneschlbeck/new-york-city-airport-activity

1. Read the data using Python, analyse it using pandas manipulations we practiced

2. Perform a data clearning for missing values, nulls and NANs for a better data

3. Based on what you analysed from the data file, create a table in Cassandra with a PRIMARY KEY that you think is the best combination between partitionning and uniqueness

4. Save your data to your new created table in Cassandra

## TablePlus - CQL

1. Have a look at your data using CQL : look at the data for some partitions

2. Calculate the sum of departure and arrival delays for each carrier by each year

## Back to Python

1. Perform what you see as required data analysis in order to produce a report and talk about the data and your findings

  - For example, the carriers having the largest delays
  - The days where all the carriers experience big delays
  - Are there any Origin or Destination airports that produce large delays
  - ...