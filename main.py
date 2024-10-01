# import libraries as alias
import numpy as pd
import pandas as pd

def main():
# series are 1D arrays of indexed data

    # create a series from a list/array
    data = pd.Series([0.25, 0.5, 0.75, 1.0])
    print(data.values) # looks like a list
    print(data.index) # range computed for indices

    # access series by index
    print(data[1]) # getting one value from series
    print(data[1:3]) # prints index and values (not inclusive of last index)

    # series are like arrays but with explicit indexing
    data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a","b","c","d"])
    print(data)
    
    grades = pd.Series([9, 10, 11, 12], index=["Freshman","Sophmore","Junior","Senior"])
    print(grades)
    
    # access series data by index
    print("Seniors are in Grade:", grades["Senior"])
    
    # can also create a series from a dictionary
    cookies_Dict = {"Chocolate Chip": 6, "Oatmeal Raisin": 9, "Snickerdoodle": 5, "Ginger Snap": 8, "Cookie Butter": 10, "Brookie": 7}
    cookies = pd.Series(cookies_Dict)
    print(cookies) # the dictionary keys become indices
    
    # access item by index
    print("Rating of Cookie Butter:", cookies["Cookie Butter"])
    
    # DataFrame is like a 2D array or special dictionary
    cookies_DF = pd.DataFrame(cookies, columns=["Rating"])
    print(cookies_DF)
    
    # add a column to the DataFrame
    cookies_DF["Allergens"] = [True, True, True, True, True, True]
    print(cookies_DF)
    
    # could also do it the long way and make another dict
    cookies_DF["Sweetness"] = {"Chocolate Chip": 8, "Oatmeal Raisin": 6, "Snickerdoodle": 5, "Ginger Snap": 5, "Cookie Butter": 8}
    print(cookies_DF)
    
    # DATA SELECTION
    # index using explicit index
    data2 = pd.Series(["G", "r", "a", "c", "i", "e"], index=[7, 18, 1, 3, 9, 5])
    print(data2[7])
    
    # NOTE: all are inclusive of final parameter
    print(data2[1:5]) # prints out the actual index of 1:5 not explicit
    print(data2[2:7]) # use actual index to call correct indices
    
    # slicing des not give expected output with explicit index b/c uses implict index always 
    
    # instead need to use the LOC attribute to slice w/ explicit
    print(data2.loc[1:5])
    
if __name__ == "__main__":
    main()
