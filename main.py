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
    
if __name__ == "__main__":
    main()
