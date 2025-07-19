from .Pet import Pet

class Dog(Pet):
    def __init__(self, name: str="", age: int=0) -> None:
        """
        Initialize a Dog with optional name and age.

        Args:
            name (str, optional): The name of the dog.
            age (int, optional): The age of the dog.

        Returns:
            None
        """
        pass

    def speak(self) -> str:
        """
        Make the dog speak.
        Returns:
            str: The sound the dog makes.
        """
        return ""

    def __str__(self) -> str:
        """
        Get a string representation of the dog.

        Returns:
            str: A string representing the dog.
        """
        return ""
