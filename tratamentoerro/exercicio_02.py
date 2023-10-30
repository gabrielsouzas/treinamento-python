# Creating a utility to convert strings to boolean values

true_values = ["yes", "y"]
false_values = ["no", "n"]


def str_to_bool(value):
    if value.lower() in true_values:
        return True
    elif value.lower() in false_values:
        return False
    else:
        raise ValueError("Invalid entry")


print(str_to_bool("no"))
