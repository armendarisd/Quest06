def my_csv_parser(param_1, param_2):
    current_array = param_1.split('\n')
    array_num_elements = len(current_array)
    index = 0
    csv_array = []

    while(index < array_num_elements-1):
        csv_array.append(create_columns(current_array[index], param_2))
        index += 1
    return csv_array

def create_columns(param_1, param_2):
    current_array = param_1.split(param_2)
    return current_array

