# lambdata
A useful library of DS helper functions

This library is for anyone who, for some reason, would like to use pandas through an arbitrary class written by a coding novice.

## Availible Functions

This library takes a dataframe as an argument to create a DataCleaner object.

This object has the following methods:

## clean_column_names(self)
Removes non-standard characters from column names

## squared_feature(self, list)
For a cleaned feature column, creates a n^2 dependent features

## desc(self)
Describes DataFrame

## ret_df(self)
Returns a Pandas DataFrame
