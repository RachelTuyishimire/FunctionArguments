# A function named concatenate_args that takes any number of string arguments 
# in positional arguments format and concatenates them into a single string
def concatenate_args(*words):
    sentence = " "
    for word in words:
        sentence += word
    return sentence

# A function named concatenate_kwargs that takes any number of string arguments 
# in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    attributes = " "
    for key,value in kwargs.items():
        attributes += value
    return attributes
