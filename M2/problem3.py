a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    """
    print("type() of input data:",end=" ")
    input_type = [ type(ele) for ele in arr]
    print(input_type)
    """
    print("\nPositive Output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value
    #nv335-9/22/2023
    for j in arr:
        if isinstance(j,str):
            positive_integer = str(abs(int(j)))
            print(positive_integer, end =" ")
        else:
            positive_integer = abs(j)
            print(positive_integer,end =" ")
    print("\n type() of output data:",end=" ")
    print(type(positive_integer))
            
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)