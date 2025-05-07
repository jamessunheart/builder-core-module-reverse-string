# reverse_string module

def reverse_string(s: str) -> str:
    """
    Reverse the input string with basic validation.

    Args:
        s (str): The string to reverse

    Returns:
        str: The reversed string
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

def run(input: str) -> str:
    return reverse_string(input)