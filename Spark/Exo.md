# Covid Exercice

Data Description if needed : https://github.com/owid/covid-19-data/tree/master/public/data
Data Source if needed : https://github.com/ElMehdiBen/Py_Course/blob/main/Pandas/data.csv

## Questions

1. Read the data and Handle missing values (null) as well as outliers
2. Create a new dataframe by selecting few columns : (continent, location, date, population, new_cases, new_deaths, icu_patients, hosp_patients, new_tests, people_vaccinated)
3. Keep a clean data which will be used for analysis
4. Make use of the date columns - Make sure its format can be used in your analysis
5. Using one month of data - display top 5 locations who counts the biggest sum of new cases [Tip : data.limit(5)]
6. Same as question 5 but for new deaths
7. Using another different month, display the same as question 5 and 6
8. Use display graphics to plot the top 10 biggest sum of new cases ordered ASC
9. Use display graphics to plot the top 10 biggest sum of new deaths ordered DESC [Tip : orderBy(column, ascending=False)]
10. Using 6 months of data - Display the average of new vaccinations per month per location 
11. Explore Display Graphics available on Databricks
