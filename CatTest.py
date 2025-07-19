import unittest

from pkg import Cat, Pet, Animal

class CatTest(unittest.TestCase):
    def testInheritance(self) -> None:
        # Given
        p = Cat()
        self.assertTrue(isinstance(p, Pet))

    def testImplementation(self) -> None:
        p = Cat()
        self.assertTrue(isinstance(p, Animal))

    def nullaryConstructorTest(self) -> None:
        # Given
        expectedOwner = None
        expectedName = ""
        expectedAge = 0
        cat = Cat()
        # When
        actualName = cat.name()
        actualAge = cat.age()
        actualOwner = cat.owner()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)
        self.assertEqual(expectedOwner, actualOwner)

    def constructorWithNameTest(self) -> None:
        # Given
        expectedName = "Name of Cat"
        expectedAge = 0
        cat = Cat(expectedName)
        # When
        actualName = cat.name()
        actualAge = cat.age()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)

    def constructorWithAgeTest(self) -> None:
        # Given
        expectedName = ""
        expectedAge = 2**31 - 1
        cat = Cat(expectedAge)
        # When
        actualName = cat.name()
        actualAge = cat.age()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)

    def constructorWithNameAndAgeTest(self) -> None:
        # Given
        expectedName = "Name of Cat"
        expectedAge = 2**31 - 1
        cat = Cat(expectedName, expectedAge)
        # When
        actualName = cat.name()
        actualAge = cat.age()
        # Then
        self.assertEqual(expectedAge, actualAge)
        self.assertEqual(expectedName, actualName)

    def speakTest(self) -> None:
        # Given
        cat = Cat()
        expected = "meow"
        # When
        actual = cat.speak()
        # Then
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
