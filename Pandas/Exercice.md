## Exercises: Pandas

Data Description : https://github.com/owid/covid-19-data/tree/master/public/data

0. Read the owid-covid-data.csv file from data directory
Link : https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv

1. Get the first 22 rows
2. Get the last 1 row
3. Count the number of rows and columns
4. Get the column names from your dataframe as a list
5. create a new dataframe from a reduced list of columns from the original dataframe
6. Get the continent column as pandas series and extract the list of unique continents from it
7. Using Filters on continents, calculate the sum of total cases per continent

# Question 8 with me, we will show how to deal with dates
8. Filter the data based on two dates
# Question 9 is to be discussed before we agree on the analysis to be done
9. Explore the data and make sense of it


## COVID Exercise: Pandas

# Cleaning the Dataframe - Exemples de cleaning avec des fonctions a utiliser
    ## Missing values handling - Examples
    ## Null, NaN, NA
    ## UDF - from Null or NAN or NA to 0 if it's a number
    ### Outliers, 
# Data Analysis - Utilisation de plusieurs GroupBy pour generer des insights
    ## Largest new_cases in a month / location
    ## Largest new_deaths in a month / location
    ## Largest Ratio in new cases and deaths (population_density)
    ## Largest number of cases within the whole period
    ## Largest number of deaths within the whole period

# Adding columns - detecting causality - if there any
    ## What causes new cases per location (people from a location are smokers)
    ## icu_patients analysis
    ## tests analysis
    ## vaccination - comparing vacc rate in a period / location
    ## age analysis
