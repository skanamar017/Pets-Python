class Animal:
    def speak(self) -> str:
        """
        Make the animal speak.

        Returns:
            str: The sound the animal makes.
        """
        raise NotImplementedError("Subclasses must implement this method")
        return ""
