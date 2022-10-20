# assignment1
# example to demonstrate dictionary is a mutable data type in python
# our current dictionary
my_dict = {"state":"UP", "Capital":"Lucknow"}
# adding new key-value pair to our dictionary
my_dict['Country'] = "India"
# printing our dictionary after the operation
print("Dictionary after adding a new key-value pair = ",my_dict)
# updating key-value pair in our dictionary
my_dict['state'] = "uttar pradesh"
# printing our dictionary after the operation
print("Dictionary after updating an existing key value pair = ",my_dict)
# removing key-value pair in our dictionary
my_dict.pop('Capital')
# printing our dictionary after the operation
print("Dictionary after popping out a key value pair = ",my_dict)
# removing key-value pair in our dictionary
my_dict.clear()
print("After clearing the whole dictionary = ",my_dict)
