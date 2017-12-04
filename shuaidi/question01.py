def print_index_value_pair_for_list(in_list):
    if not isinstance(in_list, list):
        raise TypeError(f"print_index_value_pair_for_list() takes a list ({type(in_list)} given)")

    length = len(in_list)

    if length == 0:
        print("()")
        return None

    list_for_print = [] # prepare elements to print
    for i in range(0, length-1):
        list_for_print.append(f"({i}, {in_list[i]}), ")

    # handle the last element
    list_for_print.append(f"({length-1}, {in_list[length-1]})")

    print("".join(list_for_print))

# invoke to test print_index_value_pair_for_list()
in_param = ["a", "b", "c"]
print_index_value_pair_for_list(in_param)
