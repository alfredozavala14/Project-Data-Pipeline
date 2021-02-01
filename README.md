![hamkmock](https://cache.desktopnexus.com/thumbseg/1930/1930911-bigthumbnail.jpg)

# Project-Data-Pipeline

## Introduction

This is the second weekly project in the Ironhack Data Analytics bootcamp. The objective is to practice the class learnings so far. This includes, cleaning a dataset, enriching it with data from an API and/or web scraping, and creating a report with statistics and plots.

To do this, we can use a dataset of our choice. I have decided to use a dataset with information on the happiness across 156 countries. This dataset can be found on [kaggle](https://www.kaggle.com/ayushggarg/all-trumps-twitter-insults-20152021)

## Hypotheses

Starting from a dataset than includes a ranking of the countries with the happiest people, I want to test the hypothesis that happiness is much less correlated to monetary data like GDP per capita or social support and more dependant on non-monetary factors like generosity, healthy life expectancy, or freedom. Additionally, I will look for new data in the API and try to find additional correlations with the happiness index.

## Libraries used

During the project, I have used the following libraries:
- Pandas
- Requests
- Os
- Json
- Datetime
- Wbdata
- Matplotlib
- Seaborn

You can find links to the official documentation of each library at the end, under Links & Resources

## Work done

To clean the data, I have used various techniques, including:

- Deleting columns full of null values
- Deleting duplicated data
- Changing column names to make them more 'python firendly' (e.g. removing spaces, special characters, etc.)
- Defining a new index

To enrich the data, I have downloaded information on several indicators and have merged them with the original dataframe. Not all rows had values for every new indicator, but being able to merge all the data in one single dataframe, even if it meant having incomplete data, allowed for easier visualization.

For the visualization process, I have used both Seaborn and Matplotlib to produce different kinds of plots and subplots that allowed ti visualize relationships between the different columns.

## Deliverables

Deliverables include the cleaned dataset enriched with data from the World Bank API, two jupyter notebooks, one where I carried out the cleaning and enriching process and one including the visualization part of the project, and a .py document with formulas defined for this project.

## Links & Resources


- [Kaggle dataset](https://www.kaggle.com/unsdsn/world-happiness?select=2019.csv)
- [World Bank API documentation](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information)
- [Pandas documentation](https://pandas.pydata.org/)
- [Requests documentation](https://requests.readthedocs.io/en/master/)
- [Os documentation](https://docs.python.org/3/library/os.html)
- [Json documentation](https://docs.python.org/3/library/json.html)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [Wbdata documentation](https://wbdata.readthedocs.io/en/stable/)
- [Matplotlib documentation](https://matplotlib.org/)
- [Seaborn documentation](https://seaborn.pydata.org/)
