############################
#    E X C E P T I O N S
############################


# When raising exceptions, use one of the built-in exceptions in Python:
"""
Exception - Cause of Error
AssertionError - Raised when an assert statement fails.
AttributeError - Raised when attribute assignment or reference fails.
EOFError - Raised when the input() function hits end-of-file condition.
FloatingPointError - Raised when a floating point operation fails.
GeneratorExit - Raise when a generator's close() method is called.
ImportError - Raised when the imported module is not found.
IndexError - Raised when the index of a sequence is out of range.
KeyError - Raised when a key is not found in a dictionary.
KeyboardInterrupt - Raised when the user hits the interrupt key (Ctrl+C or Delete).
MemoryError - Raised when an operation runs out of memory.
NameError - Raised when a variable is not found in local or global scope.
NotImplementedError - Raised by abstract methods.
OSError - Raised when system operation causes system related error.
OverflowError - Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError - Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError - Raised when an error does not fall under any other category.
StopIteration - Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError - Raised by parser when syntax error is encountered.
IndentationError - Raised when there is incorrect indentation.
TabError - Raised when indentation consists of inconsistent tabs and spaces.
SystemError - Raised when interpreter detects internal error.
SystemExit - Raised by sys.exit() function.
TypeError - Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError - Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError - Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError - Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError - Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError - Raised when a Unicode-related error occurs during translating.
ValueError - Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError - Raised when the second operand of division or modulo operation is zero.
"""

# or implement a user-defined exception:
class Error(Exception):
    """Base class for other exceptions"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
class InvalidArgumentTypeError(Error):
    """Raised when the function argument type is invalid"""
    pass
class InvalidArgumentValueError(Error):
    """Raised when the function argument value is invalid"""
    pass
class DataConversionError(Error):
    """Raised when the conversion of data from one format to another fails"""
    pass
class NormalizationError(Error):
    """Raised when normalization of a DataFrame fails"""
    pass
class DeltaLakeReadError(Error):
    """Raised when reading data from the Azure Delta Lake fails"""
    pass
class DeltaLakeWriteError(Error):
    """Raised when writing data to the Azure Delta Lake fails"""
    pass
class UnassignedPropertyError(Error):
    """Raised when an operation is dependent a property value, but there has not been assigned a alue to this property"""
    pass
class MissingDictionaryKeyError(Error):
    """Raised when the dictionary does not contain a required key"""
    pass
class InvalidDictionaryTypeError(Error):
    """Raised when the dictionary type is invalid"""
    pass
class InvalidDictionaryValueError(Error):
    """Raised when the dictionary value is invalid"""
    pass

