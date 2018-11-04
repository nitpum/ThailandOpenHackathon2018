# To check if o is an instance of str or any subclass of str, use isinstance (this would be the "canonical" way):
if isinstance(o, str):

# To check if the type of o is exactly str (exclude subclasses):

if type(o) is str:

# The following also works, and can be useful in some cases:

if issubclass(type(o), str):