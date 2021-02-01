import pandas as pd
import os
import requests
import json
import wbdata
import datetime

def clean_df_titles(df):
    '''
    Function to remove extra spaces and uppercase characters from column names and replace spaces between words
    with undersocres
    
    Takes: dataframe
    Returns: dataframe with clean titles
    '''
    
    df.columns = df.columns.str.lower().str.replace(' ','_').str.strip()
    
def drop_nan_columns(df):
    '''
    Drops all columns that are full of NaNs
    
    Takes: dataframe
    Returns: dataframe without empty columns
    '''
    
    df.dropna(axis=1, how='all', inplace = True)

    
def change_column_name(df, old_col_name, new_col_name):
    '''
    Changes a column name
    
    Takes: dataframe, old column name and new colum name
    Returns: dataframe with new name
    '''
    
    df.rename(columns = {old_col_name: new_col_name}, inplace = True)

    
def change_df_index(df, new_index_col_name):
    '''
    Changes a dataframe's index to the chosen column
    
    Takes: dataframe and name of new index
    Returns: dataframe with new index
    '''
    
    df.set_index(new_index_col_name, inplace = True)

def clean_data_set(df, old_col_name = False, new_col_name = False, new_index_col_name = False):
    '''
    Function to clean dataset downloaded from Kaggle. Column names to be changed have to be in two separate
    lists (old vs. new). Accepts multiple changes at once.
    
    Takes: dataframe, old_col_name (must be a list), new_col_name (must be a list) and name of column that 
    will be the new index
    Returns: dataframe with cleaned titles, no empty columns, new column name(s) and a new index name
    '''
    
    # First step is to clean titles
    
    clean_df_titles(df)
    
    # Second step is to drop columns that are full of NaNs
    
    drop_nan_columns(df)
    
    # Third we will change any column names we want to change
    
    if (not type(old_col_name) == list) and (not type(new_col_name) == list):
        print('old_col_name and/or new_col_name not type list')
        pass
    else:
        if old_col_name and new_col_name:
            for i,j in zip(list(old_col_name), list(new_col_name)):
                change_column_name(df, i, j)
        else:
            pass
    
    # Fourth we will change the index name
    
    if new_index_col_name:
        change_df_index(df, new_index_col_name)
    else:
        pass

def print_WB_available_sources():
    '''
    prints a list of available databases in the World Bank API
    
    Takes: none
    Returns: list of WB available databases
    '''

    sources = requests.get("http://api.worldbank.org/v2/sources?per_page=100&format=json")
    sourcesJSON = sources.json()

    for i in sourcesJSON[1]:
        print(i['id'],i['name'])

def show_WB_indicators(source_id):
    '''
    Given source id of one of the WB databases, gives a list with available indicators
    
    Takes: database source_id (str format)
    Returns: list of available indicators in the database
    '''
    
    indicators = requests.get(f"http://api.worldbank.org/v2/indicator?format=json&source={source_id}&per_page=1500")
    indicatorsJSON = indicators.json()
    wdev_indicators = dict()

    # Add the Indicator IDs and Names to a dictionary
    for i in indicatorsJSON[1]:
        key = i['id']
        value = i['name']
        wdev_indicators[key] = value
    # return wdev_indicators        commented to limit very long output when revising

def print_available_countries_WB():
    '''
    Prints the country id and name of available countries in WB databases
    
    Takes: none
    Returns: list of ids and names for available countries
    '''

    country_ids = requests.get('http://api.worldbank.org/v2/country?format=json&per_page=250')
    country_idsJSON = country_ids.json()
    list_country_ids = []
    list_country_ids_name = []

    for i in country_idsJSON[1]:
        c_id = (i['id'])
        c_id_n = (i['id'], i['name'])
        list_country_ids.append(c_id)
        list_country_ids_name.append(c_id_n)
    print(list_country_ids_name[:20])
    # return list_country_ids         commented to limit very long output when revising

