import unittest

from pkg import Pet, PetOwner

class PetTest(unittest.TestCase):
    def getNameTest(self) -> None:
        # Given
        pet = Pet("Pet name")
        expectedName = "Pet name"
        # When
        actualName = pet.name()
        # Then
        self.assertEqual(expectedName, actualName)

    def setNameTest(self) -> None:
        # Given
        pet = Pet()
        expectedName = "New pet name"
        # When
        pet.name(expectedName)
        actualName = pet.name()
        # Then
        self.assertEqual(expectedName, actualName)

    def getAgeTest(self) -> None:
        # Given
        pet = Pet()
        expectedAge = 0
        # When
        actualAge = pet.age()
        # Then
        self.assertEqual(expectedAge, actualAge)

    def setAgeTest(self) -> None:
        # Given
        pet = Pet()
        expectedAge = 2**31 - 1
        # When
        pet.age(expectedAge)
        actualAge = pet.age()
        # Then
        self.assertEqual(expectedAge, actualAge)

    def setOwnerTest(self) -> None:
        # Given
        pet = Pet()
        expectedName = "Name of Owner"
        expectedOwner = PetOwner(expectedName, None)
        # When
        pet.owner(expectedOwner)
        actualOwner = pet.owner()
        # Then
        self.assertEqual(expectedOwner, actualOwner)

    def getOwnerTest(self) -> None:
        # Given
        pet = Pet()
        expectedName = "Name of Owner"
        expectedOwner = PetOwner(expectedName, [pet])
        # When
        actualOwner = pet.owner()
        # Then
        self.assertEqual(expectedOwner, actualOwner)

if __name__ == "__main__":
    unittest.main()
