import unittest

from pkg import Pet, Cat, Dog, PetOwner

class PetOwnerTest(unittest.TestCase):
    def constructorTest(self) -> None:
        # Given
        expectedName = "George"
        expectedPet = Pet()
        # When
        po = PetOwner(expectedName, [ expectedPet ])
        actualName = po.name()
        actualPet = po.pets()[0]
        # Then
        self.assertEqual(expectedName, actualName)
        self.assertEqual(expectedPet, actualPet)

    def addPetTest1(self) -> None:
        # Given
        expected = Pet()
        po = PetOwner("", [])
        # When
        po.addPet(expected)
        actual = po.pets()[0]
        # Then
        self.assertEqual(actual, expected)

    def addPetTest2(self) -> None:
        # Given
        newPet = Pet()
        po = PetOwner("", [])
        # When
        po.addPet(newPet)
        # Then
        outcome = po.isOwnerOf(newPet)
        self.assertTrue(outcome)

    def removePetTest(self) -> None:
        # Given
        newPet = Pet()
        po = PetOwner("", [newPet])
        expected = None

        # When
        po.removePet(newPet)
        actual = po.pets()

        # Then
        self.assertEqual(expected, actual)

    def isOwnerOfTest(self) -> None:
        # Given
        newPet = Pet()
        anotherPet = Pet()
        po = PetOwner("", [newPet])
        # When
        outcome = po.isOwnerOf(newPet)
        poOwnsAnotherPet = po.isOwnerOf(anotherPet)
        # Then
        self.assertTrue(outcome)
        self.assertFalse(poOwnsAnotherPet)

    def getYoungestPetAgeTest(self) -> None:
        # Given
        expected = 1
        oneYearOldPuppy = Dog(expected)
        twoYearOldKitten = Cat(2)
        po = PetOwner("", [oneYearOldPuppy, twoYearOldKitten])
        # When
        actual = po.getYoungestPetAge()
        # Then
        self.assertEqual(expected, actual)

    def getOldestPetAgeTest(self) -> None:
        # Given
        expected = 2
        oneYearOldPuppy = Dog(1)
        twoYearOldKitten = Cat(expected)
        po = PetOwner("", [oneYearOldPuppy, twoYearOldKitten])
        # When
        actual = po.getOldestPetAge()
        # Then
        self.assertEqual(expected, actual)

    def getAveragePetAgeTest(self) -> None:
        # Given
        expected = 3.0
        fourYearOldPuppy = Dog(4)
        twoYearOldKitten = Cat(2)
        po = PetOwner("", [fourYearOldPuppy, twoYearOldKitten])
        # When
        actual = po.getAveragePetAge()
        # Then
        self.assertAlmostEqual(expected, actual, delta=0.05)

    def getNumberOfPetsTest(self) -> None:
        # Given
        expected = 2
        fourYearOldPuppy = Dog(4)
        twoYearOldKitten = Cat(2)
        po = PetOwner("", [fourYearOldPuppy, twoYearOldKitten])
        # When
        actual = po.getNumberOfPets()
        # Then
        self.assertEqual(expected, actual)

    def getNameTest(self) -> None:
        # Given
        expected = "Pet owner name"
        po = PetOwner(expected)
        # When
        actual = po.name()
        # Then
        self.assertEqual(expected, actual)

    def getPetsTest(self) -> None:
        # Given
        fourYearOldPuppy = Dog(4)
        twoYearOldKitten = Cat(2)
        pets = [fourYearOldPuppy, twoYearOldKitten]
        po = PetOwner("", pets)
        # When
        petList = po.pets()
        # Then
        for pet in pets:
            self.assertIn(pet, petList)

if __name__ == "__main__":
    unittest.main()
