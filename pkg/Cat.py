from .Pet import Pet

class Cat(Pet):
    def __init__(self, name: str="", age: int=0) -> None:
        """
        Initialize a Cat with optional name and age.

        Args:
            name (str, optional): The name of the cat.
            age (int, optional): The age of the cat.

        Returns:
            None
        """
        pass

    def speak(self) -> str:
        """
        Make the cat speak.

        Returns:
            str: The sound the cat makes.
        """
        return ""

    def __str__(self) -> str:
        """
        Get a string representation of the cat.

        Returns:
            str: A string representing the cat.
        """
        return ""
