import sys


class Switcher(object):
    def input_argument(self, argument):
        method_name = "method_" + str(argument).replace("-", "")
        print("Method name is: ", method_name)
        method = getattr(self, method_name, lambda : "Invalid argument!")
        return method()

    def method_default(self):
        print("No argument available!")
        return None

    def method_a(self):
        print("Method 1")
        return ""

    def method_b(self):
        print("Method 2")
        return ""

    def method_c(self):
        print("Method 3")
        return ""


if __name__ == "__main__":
    test_object = Switcher()
    try:
        test_object.input_argument(sys.argv[1])
    except IndexError:
        test_object.input_argument("default")
