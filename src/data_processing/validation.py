"""
Data validation functions.
"""


# Example function to implement:
def validate_isbn(isbn):
    """Validate ISBN-13 format."""


    isbn = str(isbn).strip()
    isbn = isbn.replace('-','')
    isbn = isbn.replace(' ','')

    if len(isbn) != 13:
        return False

    return True



 

