# Unit testing
Using unittest module from Python to test a single part of the code, such as a function.

``` python
class Test_Rearrange(unittest.TestCase): #check example_testing.py
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected) #assertequal method will return "ok" with the test case and expected answers are the same

unittest.main() #will run the test 
```

# Types of Tests
- Black Box: When the person testing doenst know exactly how the software works, just what it is supposed to do
- White Box: When the person testing knows exactly how the software works and what it is supposed to do
- Smoke: Software testing process that determines whether the deployed software build is stable or not. Smoke testing is a confirmation for QA team to proceed with further software testing. It consists of a minimal set of tests run on each build to test software functionalities. Smoke testing is also known as “Build Verification Testing” or “Confidence Testing.” In simple terms, we are verifying whether the important features are working and there are no showstoppers in the build that is under testing.
- Integration: Also known as integration and testing (I&T) is a type of software testing in which the different units, modules or components of a software application are tested as a combined entity. However, these modules may be coded by different programmers. The aim of integration testing is to test the interfaces between the modules and expose any defects that may arise when these components are integrated and need to interact with each other. 
- Regression: Regression testing (rarely, non-regression testing) is re-running functional and non-functional tests to ensure that previously developed and tested software still performs after a change. If not, that would be called a regression. 
- Load: Type of software testing used to verify the software’s ability to behave well under significantly stressed testing conditions

# Raising Errors

``` python
def validade_user(usename, minlen):
    assert type(username) == str, "username must be a string" #will raise an error it the user inserts an invalid argument
    if minlen <1:
        raise ValueError("minlen must be at least 1") #will raise an error if the if condition is not met
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
```
# Handling Errors Cheat Sheet

Raise allows you to throw an exception at any time.

    https://docs.python.org/3/tutorial/errors.html#raising-exceptions

Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

    https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

    https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.

In the try clause, all statements are executed until an exception is encountered.

    https://docs.python.org/3/tutorial/errors.html#handling-exceptions

Except is used to catch and handle the exception(s) that are encountered in the try clause.

    https://docs.python.org/3/library/exceptions.html#bltin-exceptions

Other interesting Exception handling readings:

    https://doughellmann.com/posts/python-exception-handling-techniques/


