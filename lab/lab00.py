def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """

    return 2020

def whatsmyname():
    """ Make the function return your name."""
    return "jason"

def main():
    print("My name is: " + whatsmyname())
    print("Making sure twenty_twenty returns 2020")
    assert(twenty_twenty() == 2020)
    print("Nice... it did")

if __name__ == "__main__":
    main()
