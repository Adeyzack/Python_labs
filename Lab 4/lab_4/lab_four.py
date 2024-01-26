"""
This program allows a user to enter and validate their phone number and zipcode+4.
 Then the user will enter values of two, 3x3 matrices and then select from options
  including, addition, subtraction, matrix multiplication, and element by element
  multiplication. The program use numpy.matmul() for matrix multiplication
   (e.g. np.matmul(a, b) ). The program also compute the appropriate results
and return the results, the transpose of the results, the mean of the rows
for the results, and the mean of the columns for the results.
When entering data, the application uses regular expressions and/or Pandas
functionality to check the format of the phone number and zipcode.
the program checks each value is numeric for the matrices. The user
interface should continue to run until the user indicates they are ready to exit.
"""
import re
import numpy as np


def input_menu():
    """
    This function displays operation menu
    :return: (str) user choice
    """
    user_input = input("Select a Matrix Operation from the list below:\n"
                       "a. Addition\n"
                       "b. Subtraction\n"
                       "c. Matrix Multiplication\n"
                       "d. Element by element multiplication\n")

    valid_choices = ['a', 'b', 'c', 'd']
    # validates user input
    while not user_input.isalpha() or user_input not in valid_choices:
        user_input = input("Invalid Input!!!\n"
                           "Select a Matrix Operation from the list below:\n"
                           "a. Addition\n"
                           "b. Subtraction\n"
                           "c. Matrix Multiplication\n"
                           "d. Element by element multiplication\n")
    return user_input


def welcome():
    """
    function to get users permission to continue or abort thr game
    :return: (bool) True if user typed 'y' or False otherwise
    """
    yes_no_choice = input("\n\n***************** Welcome to the"
                          " Python Matrix Application***********\n"
                          "Do you want to play the Matrix Game?\n"
                          "Enter Y for Yes or N for No:\n")
    yes_no = ['y', 'n']
    # input validation
    while not yes_no_choice.isalpha() or yes_no_choice not in yes_no:
        yes_no_choice = input("Input must be 'Y' or 'N' \n"
                              "Do you want to play the Matrix Game?")

    return yes_no_choice.lower() == 'y'


def phone_zip():
    """
    function to get phone number and zip-code in a specified format.
    :return: none
    """

    phone_number = input("Enter your phone number (XXX-XXX-XXXX): \n")

    phone_pattern = r"\d{3}-\d{3}-\d{4}$"
    # check if the phone number matches the pattern
    flag = re.match(phone_pattern, phone_number)
    # Prompt user to re-enter the phone number if not in a correct format
    while not flag:
        phone_number = input("Your phone number is not in correct format. Please renter:\n")
        flag = re.match(phone_pattern, phone_number)

    zip_code = input("Enter your zip code+4 (XXXXX-XXXX):\n")

    zip_pattern = r"\d{5}-\d{4}$"
    # check if the zip-code matches the pattern
    zip_flag = re.match(zip_pattern, zip_code)
    # Prompt user to re-enter zip code if not in a correct format
    while not zip_flag:
        zip_code = input("Your zip-code is not in correct format. Please renter:\n")
        zip_flag = re.match(zip_pattern, zip_code)


def list_input():
    """
    function to get the 3x3 matrix
    :return: (list or bool)
    """
    input_numbers = input()
    numbers = input_numbers.split()

    # Check if exactly three numbers were entered
    if len(numbers) == 3:
        try:
            matrix = []
            num1 = float(numbers[0])
            num2 = float(numbers[1])
            num3 = float(numbers[2])
            matrix.append(num1)
            matrix.append(num2)
            matrix.append(num3)

            return matrix

        except ValueError:
            print("Invalid input. Please enter three float numbers separated by a space.")
            return False

    else:
        print("Invalid input. Please enter exactly three float numbers separated by a space.")
        return False


def matrix_input():
    """
    function to validate if the elements of the matrix are numeric only
    :return: (list) 3X3 matrix
    """
    matrix = []
    # validate if user input is only numeric
    list_one = list_input()
    while list_one is False:
        list_one = list_input()
    list_two = list_input()
    while list_two is False:
        list_two = list_input()
    list_three = list_input()
    while list_three is False:
        list_three = list_input()

    matrix.append(list_one)
    matrix.append(list_two)
    matrix.append(list_three)
    return matrix


def print_matrix_elements(matrx):
    """
    function to display the 3x3 matrix
    :param matrx:
    :return: none
    """
    for row in matrx:
        for element in row:
            print(element, end=" ")

        print()


def display_matrix():
    """
    function to display the matrix's
    :return: (list)
    """
    print("Enter your first 3x3 matrix:")
    mat_one = matrix_input()
    print("Your first 3x3 matrix is:\n")
    print_matrix_elements(mat_one)

    print("Enter your second 3x3 matrix:")
    mat_two = matrix_input()
    print("Your second 3x3 matrix is:\n")
    print_matrix_elements(mat_two)

    return mat_one, mat_two


def matrix_add(matrix_1, matrix_2):
    """
    function to add two matrices
    :param matrix_1: (list)
    :param matrix_2: (list)
    :return: none
    """
    # convert list to aray
    matrix_one = np.array(matrix_1)
    matrix_two = np.array(matrix_2)
    mat_add = matrix_one + matrix_two
    print("You selected Addition. The results are:")
    # add the matrices
    print_matrix_elements(mat_add)
    # transpose a matrix
    transposed_matrix = mat_add.transpose()
    print("\nThe Transpose is:")
    print_matrix_elements(transposed_matrix)
    mean_colum_row(mat_add)


def matrix_substra(matrix_1, matrix_2):
    """
    function to subtract two matrices
    :param matrix_1: (list)
    :param matrix_2: (list)
    :return: none
    """
    # convert list to aray
    matrix_one = np.array(matrix_1)
    matrix_two = np.array(matrix_2)
    mat_sub = matrix_one - matrix_two
    print("You selected Subtraction. The results are:")
    print_matrix_elements(mat_sub)
    # transpose a matrix
    transposed_matrix = mat_sub.transpose()
    print("\nThe Transpose is:")
    print_matrix_elements(transposed_matrix)
    mean_colum_row(mat_sub)


def matrix_multiplication(first_matrix, second_matrix):
    """
    function to multiply two matrices
    :param first_matrix:(list)
    :param second_matrix:(list)
    :return: none
    """
    # convert list to aray
    matrix_one = np.array(first_matrix)
    matrix_two = np.array(second_matrix)
    mat_mul = np.matmul(matrix_one, matrix_two)
    print("You selected Multiplication. The results are:")
    print_matrix_elements(mat_mul)
    # transpose a matrix
    transposed_matrix = mat_mul.transpose()
    print("\nThe Transpose is:")
    print_matrix_elements(transposed_matrix)
    mean_colum_row(mat_mul)


def elem_mult(mat_one, mat_two):
    """
    function to multiply two matrices element by element
    :param mat_one: (list)
    :param mat_two: (list)
    :return: none
    """
    matrix_one = np.array(mat_one)
    matrix_two = np.array(mat_two)
    # initialize output matrix
    mult_output = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                mult_output[i][j] += matrix_one[i][k] * matrix_two[k][j]
    print("You selected Element by element Multiplication. The results are:")
    print_matrix_elements(mult_output)
    mult_output = np.array(mult_output)
    transposed_matrix = mult_output.transpose()
    print("\nThe Transpose is:")
    print_matrix_elements(transposed_matrix)
    mean_colum_row(mult_output)


def mean_colum_row(matrix):
    """
    function to calculate the mean of each row and columns of a matrix
    :param matrix:
    :return:
    """
    matrix = np.array(matrix)
    # get the mean at axis 1 and 0
    row_mean = np.mean(matrix, axis=1)
    col_mean = np.mean(matrix, axis=0)
    print("The row and column mean values of the results are:")
    print("Row: ", end=" ")
    for mean in row_mean:
        print(mean, end=" ,")
    print("\nColumn: ", end=" ")
    for elem in col_mean:
        print(elem, end=" ,")


# prompt the user to do matrix operations on 'y'
while welcome():
    phone_zip()
    mat_1, mat_2 = display_matrix()
    user_choice = input_menu()
    if user_choice == 'a':
        matrix_add(mat_1, mat_2)
    if user_choice == 'b':
        matrix_substra(mat_1, mat_2)
    if user_choice == 'c':
        matrix_multiplication(mat_1, mat_2)
    if user_choice == 'd':
        elem_mult(mat_1, mat_2)

print("*********** Thanks for playing Python Numpy ***************")
