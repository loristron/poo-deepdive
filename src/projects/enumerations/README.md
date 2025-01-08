# Application Exceptions

In many cases, especially in longer projects, we want to have an easy way to generate exceptions.

So we want:

- Raise consistent exceptions types
- Associated exception code
- Associated default exception message
- Ability for our user to easily list out all the possible exceptiosn in our app

This is very useful using API's, for example.

There is a bunch of ways to do that, but in this specifically case we want to use `Enumerations`.

## Functionality

Create a single enumeration AppException

Exceptions must have a name (key) and three associated value:

- - name (e.g `NotAnInteger`)
- - code (e.g `100`)
- - default message (e.g `Value is not an integer`)
- - Associated exception type (e.g `ValueError`)

We have to be able to:

- lookup by exception name (key) or code (value)
- - `AppException['NotAnInteger']` and `AppException(100)`
- Method to raise an exception
- - `AppException.Timeout.throw()`
- Ability to override default message when throwing exception
- `AppException.Timeout.throw('Custom message')`

## Tips

Enumeration members will be defined using a `tuple` containing three values

`NotAnInteger = 100, ValueError, 'Value is not an integer`

User the `__new__` approace

Make the `value` the error code and provide an additional property for message
