from .Pet import Pet

from typing import List

class PetOwner:
    def __init__(self, name: str, pets: List[Pet]) -> None:
        """
        Initialize a PetOwner with a name and a list of pets.

        Args:
            name (str): The name of the pet owner.
            pets (List[Pet]): A list of Pet objects owned by the pet owner.

        Returns:
            None
        """
        self.name=name
        self.pets=pets

    # Name property
    @property
    def name(self) -> str:
        """
        Get the name of the pet owner.

        Returns:
            str: The name of the pet owner.
        """
        return self.name

    # Pets property

    @property
    def pets(self) -> List[Pet]:
        """
        Get a list of all pets owned by the owner.

        Returns:
            List[Pet]: A list of all pets owned by the owner.
        """
        return self.pets

    def addPet(self, pet: Pet) -> None:
        """
        Add a pet to the owner's list of pets.

        Args:
            pet (Pet): The pet to be added.

        Returns:
            None
        """
        if pet.owner==self.name: self.pets.append(pet)

    def removePet(self, pet: Pet) -> None:
        """
        Remove a pet from the owner's list of pets.

        Args:
            pet (Pet): The pet to be removed.

        Returns:
            None
        """
        if pet.owner==self.name: self.pets.remove(pet)

    def isOwnerOf(self, pet: Pet) -> bool:
        """
        Check if the owner has a specific pet.

        Args:
            pet (Pet): The pet to check.

        Returns:
            bool: True if the owner has the pet, False otherwise.
        """
        return True if pet in self.pets else False

    def getYoungestPetAge(self) -> int:
        """
        Get the age of the youngest pet.

        Returns:
            int: The age of the youngest pet.
        """
        return min(x.age for x in self.pets)

    def getOldestPetAge(self) -> int:
        """
        Get the age of the oldest pet.

        Returns:
            int: The age of the oldest pet.
        """
        return max(x.age for x in self.pets)

    def getAveragePetAge(self) -> float:
        """
        Get the average age of all pets.

        Returns:
            float: The average age of all pets.
        """
        return sum(x.age for x in self.pets)/len(self.pets)

    def getNumberOfPets(self) -> int:
        """
        Get the total number of pets owned by the owner.

        Returns:
            int: The total number of pets.
        """
        return len(self.pets)

    def __str__(self) -> str:
        """
        String representation of the PetOwner.
        Returns:
            str: A string representation of the PetOwner.
        """
        return ""
# Compare this snippet from core/data/Pets-Python/src/main/AnimalMixin.py: