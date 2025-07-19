import unittest

from pkg import Dog, Pet, Animal

class DogTest(unittest.TestCase):
    def testInheritance(self) -> None:
        # Given
        p = Dog()
        self.assertTrue(isinstance(p, Pet))

    def testImplementation(self) -> None:
        p = Dog()
        self.assertTrue(isinstance(p, Animal))

    def nullaryConstructorTest(self) -> None:
        # Given
        expectedOwner = None
        expectedName = ""
        expectedAge = 0
        dog = Dog()
        # When
        actualName = dog.name()
        actualAge = dog.age()
        actualOwner = dog.owner()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)
        self.assertEqual(expectedOwner, actualOwner)

    def constructorWithNameTest(self) -> None:
        # Given
        expectedName = "Name of Dog"
        expectedAge = 0
        dog = Dog(expectedName)
        # When
        actualName = dog.name()
        actualAge = dog.age()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)

    def constructorWithAgeTest(self) -> None:
        # Given
        expectedName = ""
        expectedAge = 2**31 - 1
        dog = Dog(expectedAge)
        # When
        actualName = dog.name()
        actualAge = dog.age()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)

    def constructorWithNameAndAgeTest(self) -> None:
        # Given
        expectedName = "Name of Dog"
        expectedAge = 2**31 - 1
        dog = Dog(expectedName, expectedAge)
        # When
        actualName = dog.name()
        actualAge = dog.age()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)

    def speakTest(self) -> None:
        # Given
        dog = Dog()
        expected = "bark"
        # When
        actual = dog.speak()
        # Then
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
