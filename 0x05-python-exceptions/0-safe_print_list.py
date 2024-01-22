#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    print_count = 0
    iterator = iter(my_list)

    while print_count < x:
        try:
            element = next(iterator)
            print(element, end=" ")
            print_count += 1
        except StopIteration:
            break

    print()

    return print_count
