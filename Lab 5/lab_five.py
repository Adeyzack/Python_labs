"""
This software enables users to load either of two CSV files
and conduct histogram analysis and plotting for specific variables
within the datasets. The first dataset focuses on population
change for specific dates across different regions in the United States.
The second dataset encompasses housing data spanning a significant
timeframe, including information on home age, number of bedrooms,
and other relevant variables.
"""
import sys

import pandas as pd
import matplotlib.pyplot as plt


def main_menu():
    """
    this function displays the main menu and gets and validates user input
    :return:(str) user input
    """
    first_pick = input("***************** Welcome to the Python Data Analysis App********** \n"
                       "Select the file you want to analyze: \n"
                       "1. Population Data \n"
                       "2. Housing Data \n"
                       "3. Exit the Program\n")

    valid_choice = ['1', '2', '3']

    while not first_pick.isdigit() or first_pick not in valid_choice:
        first_pick = input("Invalid Input\n"
                           "***************** Welcome to the Python Data Analysis App********** \n"
                           "Select the file you want to analyze: \n"
                           "1. Population Data \n"
                           "2. Housing Data \n"
                           "3. Exit the Program\n")

    return first_pick


def pop_data():
    """
    This function displays a pop data menu for user to choose, gets and validate
    user input
    :return: (str) user input
    """
    print("You have entered Population Data. ")
    analysis_col = input("Select the Column you want to analyze: \n"
                         "a. Pop Apr 1 \n"
                         "b. Pop Jul 1\n"
                         "c. Change Pop \n"
                         "d. Exit Column\n")

    valid_choice = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']

    while not analysis_col.isalpha() or analysis_col not in valid_choice:
        analysis_col = input("Invalid Input!!\n"
                             "Select the Column you want to analyze: \n"
                             "a. Pop Apr 1 \n"
                             "b. Pop Jul 1\n"
                             "c. Change Pop \n"
                             "d. Exit Column\n")

    return analysis_col


def housing_data():
    """
    This function displays a housing data menu for user to choose, gets and validate
    user input
    :return: (str) user input
    """

    print("You have entered Housing  Data. ")
    housing_col = input("Select the Column you want to analyze: \n"
                        "a. AGE \n"
                        "b. BEDRMS \n"
                        "c. BUILT\n"
                        "d. ROOMS \n"
                        "e. UTILITY\n"
                        "f. Exit Column\n")

    valid_choice = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']

    while not housing_col.isalpha() or housing_col not in valid_choice:
        housing_col = input("Invalid Input!!\n"
                            "Select the Column you want to analyze: \n"
                            "a. AGE \n"
                            "b. BEDRMS \n"
                            "c. BUILT\n"
                            "d. ROOMS \n"
                            "e. UTILITY\n"
                            "f. Exit Column\n")

    return housing_col


def pop_analysis(column_name, file_name):
    """
    This function calculates the count, mean, std, min and max values from a particular column
    of .csv file.
    :param column_name: (str) the name of column from the csv file
    :param file_name: (str) name of the csv file.
    :return: none
    """

    data_file = pd.read_csv(file_name)

    count_value = data_file[column_name].count()
    mean_value = data_file[column_name].mean()
    stand_dev = data_file[column_name].std()
    min_value = data_file[column_name].min()
    max_value = data_file[column_name].max()

    # Create a histogram
    plt.hist(data_file[column_name])

    # Set labels
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    # set title of the histogram
    plt.title('Histogram of ' + column_name)

    # Print the count, mean, std, min and max values
    print(f"Count = {count_value}")
    print(f"Mean = {mean_value}")
    print(f"Standard Deviation = {stand_dev}")
    print(f"Min = {min_value}")
    print(f"Max = {max_value}")

    plt.show()
    plt.close()


while True:
    user_choice = main_menu()
    if user_choice == '1':

        while True:
            pop_choice = pop_data()
            if pop_choice == 'a':
                pop_analysis('Pop Apr 1', 'PopChange.csv')
            if pop_choice == 'b':
                pop_analysis('Pop Jul 1', 'PopChange.csv')
            if pop_choice == 'c':
                pop_analysis('Change Pop', 'PopChange.csv')
            if pop_choice == 'd':
                break

    if user_choice == '2':

        while True:
            housing_choice = housing_data()
            if housing_choice == 'a':
                pop_analysis('AGE', 'Housing.csv')
            if housing_choice == 'b':
                pop_analysis('BEDRMS', 'Housing.csv')
            if housing_choice == 'c':
                pop_analysis('BUILT', 'Housing.csv')
            if housing_choice == 'd':
                pop_analysis('ROOMS', 'Housing.csv')
            if housing_choice == 'e':
                pop_analysis('UTILITY', 'Housing.csv')
            if housing_choice == 'f':
                break
    if user_choice == '3':
        print("*************** Thanks for using the Data Analysis App********** ")
        sys.exit()
