from .Animal import Animal

class Pet(Animal):
    def __init__(self, name:str="", age:int=0) -> None:
        """
        Initialize a Pet with optional name and age.

        Args:
            name (str, optional): The name of the pet.
            age (int, optional): The age of the pet.

        Returns:
            None
        """
        self.name=name
        self.age=age
        self.owner=None
        


    # Name property

    @property
    def name(self) -> str:
        """
        Get the name of the pet.

        Returns:
            str: The name of the pet.
        """
        return self.name
    

    @name.setter
    def name(self, value: str) -> None:
        """
        Set the name of the pet.

        Args:
            value (str): The name to be set.

        Returns:
            None
        """
        self.name=value

    # Age property

    @property
    def age(self) -> int:
        """
        Get the age of the pet.

        Returns:
            int: The age of the pet.
        """
        return self.age

    @age.setter
    def age(self, value: int) -> None:
        """
        Set the age of the pet.

        Args:
            value (int): The age to be set.

        Returns:
            None
        """
        self.age=value

    # Owner property

    @property
    def owner(self):
        """
        Get the owner of the pet.

        Returns:
            PetOwner: The owner of the pet.
        """
        return self.owner

    @owner.setter
    def owner(self, value) -> None:
        """
        Set the owner of the pet.

        Args:
            value (PetOwner): The owner to be set.

        Returns:
            None
        """
        from .PetOwner import PetOwner
        self.owner=PetOwner(value, [])
        
        self.owner.pets.append(self)

    def __str__(self) -> str:
        """
        Get a string representation of the pet.

        Returns:
            str: A string representing the pet.
        """
        return ""
