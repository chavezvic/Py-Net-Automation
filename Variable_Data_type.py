#type(variableName)

# String type
string_example = "Go Jets Go"
print("The variable 'string_example' with value:", string_example, "is of type:", type(string_example)) 
#WinnipegJets
print(string_example)
print("Winnipeg Jets:", string_example)
print()


# Integer type
int_example = 1873
print("The variable 'int_example' with value:", int_example, "is of type:", type(int_example))
#WinnipegIncorporated
print(int_example)
print("The year when Winnipeg was incorporated as a city:", int_example)
print()


# Float type
float_example = 6.28318530717958647692
print("The variable 'float_example' with value:", float_example, "is of type:", type(float_example))
#TauConstant
print(float_example)
print("Tau (τ) is aproximately", float_example, ", and is a constant twice the value of pi(π)")
print()


# Complex number type
complex_example = 120000 + 30000j
print("The variable 'complex_example' with value:", complex_example, "is of type:", type(complex_example))
#AverageFlowNiagaraFalls
print(complex_example)
print("The flow rate at Niagara Falls is represented as", complex_example)
print()


# List type
list_example = ["str", "int", "float", "complex", "list", "tuple", "range", "dict", "set", "frozenset", "boot", "bytes", "bytearray", "memoryview", "NoneType"]
print("The variable 'list_example' with value:", list_example, "is of type:", type(list_example))
#DataType
print(list_example)
print("This list includes various Python data types such as:", ', '.join(list_example))
print()


# Tuple type
tuple_example = ("Winnipeg", "Manitoba", 705244, "The Forks", "MITT")
print("The variable 'tuple_example' with value:", tuple_example, "is of type:", type(tuple_example))
# PrintTheTuple
print("City: {}, Province: {}, Population: {}, Notable Place: {}, Best School Ever: {}".format(*tuple_example))
print(tuple_example)
print("This tuple contains information about Winnipeg, including the city {}, province {}, population {}, a cool location {}, and a mention of {} as an amazing institution.".format(*tuple_example))
print()
