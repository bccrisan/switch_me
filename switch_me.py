"""
Main docstring for the module
"""
import sys


class Switcher(object):
    """
    This needs docstring.
    """
    def input_argument(self, argument):
        """
        This handles the input argument
        """
        method_name = "method_" + str(argument).replace("-", "")
        print("Method name is: ", method_name)
        method = getattr(self, method_name, lambda: "Invalid argument!")
        return method()

    def method_default(self):
        """
        Default method.
        """
        print("No argument available!")

    def method_a(self):
        """
        Method a.
        """
        print("Method 1")
        return ""

    def method_b(self):
        """
        Method b.
        """
        print("Method 2")
        return ""

    def method_c(self):
        """
        Method c.
        """
        print("Method 3")
        return ""


def main():
    """
    Main function
    """
    test_object = Switcher()
    try:
        test_object.input_argument(sys.argv[1])
    except IndexError:
        test_object.input_argument("default")


if __name__ == "__main__":
    main()
