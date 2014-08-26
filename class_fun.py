#!/usr/bin/env python

# Fun with overloading class operators


class My_Class():
    """ Class with overloaded operators. """

    def __init__(self):
        """ Init method in'it!"""
        self.my_list = [1, 2, 3, 4, 5]
        print("I'm initialized.""")

    def __call__(self):
        """ Overload the call operator () to do sth else. """
        print("What are you calling me?")

    def __str__(self):
        """ Overload the print operator to do sth else. """
        return "Printing a class."

    def __add__(self, val):
        """ Overload the add """
        print("You can add {0} to this class.".format(val))

    def __setitem__(self, index, val):
        """ Overload the setitem operator. """
        print("You can set index {0} to '{1}' with this class."
              .format(index, val))
        self.my_list[index] = val

    def __getitem__(self, index):
        """ Overload the print operator to do sth else. """
        print("You can get index {0} with this class."
              .format(index))
        return self.my_list[index]


if __name__ == "__main__":

    # Create an instance which will be initialized
    my_instance = My_Class()

    # Call the instance. Not usually done with classes.
    my_instance()

    # Print the instance.
    print my_instance

    # Add to the class
    my_instance + 1

    # Set an item in the class
    my_instance[2] = "Sth"

    # Get an item in the class
    print my_instance[2]
