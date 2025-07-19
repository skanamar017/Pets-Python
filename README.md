# Pets-Python

* **Objective:** To implement a `PetOwner` which manipulates composite `Pet` objects.
* **Description** Pets are Animals that can be either Dog or Cat. An Owner can have multiple Pets.

## Pet

* Ensure each of the test cases in the class [Pet](pkg/Pet.py) successfully passes upon completion of each of the method stubs in the class [PetTest](PetTest.py).
  * Constructor option
    * `Pet() -> None`
    * `Pet(str) -> None`
    * `Pet(int) -> None`
    * `Pet(str, int) -> None`
  * `name() -> str`
  * `age() -> int`
  * `owner(PetOwner owner) -> None`
  * `owner() -> PetOwner`

### Step 1 - Define instance variables

* To create a programmatic representation of a `Pet`, begin by declaring an instance variable for each of the following properties:
  * `str name`
    * a collection of characters, representative of a name.
  * `int age`
    * an integer, representative of an age in years.
  * `PetOwner owner`
    * the owner of this `Pet`.

### Step 2 - Define the constructor

* Define a `Pet` constructor whose parameters are used to initialize its instance variables.
* A `Pet` can be constructed in 4 ways.
    1. `Pet()`
        * Upon [nullary construction](https://en.wikipedia.org/wiki/Nullary_constructor), pet has `age` of 0 and `name` of "".
    2. `Pet(str)`
        * Upon construction, `name` field should be set to respective parameter value, pet has default age of 0.
    3. `Pet(int)`
        * Upon construction, `age` field should be set to respective parameter value, pet has default name of "".
    4. `Pet(str, int)`
        * `name` and `age` variables should set to respective parameter values.

### Step 3 - Define getter and setter methods

* Understand that instance variables are not directly exposed outside of the class. We use getter and setter methods to retrieve and assign values, respectively, to gatekeep their contents.
* Define a [getter and setter](https://en.wikipedia.org/wiki/Mutator_method#Python) for each of the instance variables declared in the `Pet` class.
  * `name() -> str`
  * `age() -> int`
  * `owner(PetOwner owner) -> None`
  * `owner() -> PetOwner`

## Cats and Dogs

* Understand that `Pet` is the parent class. `Cat` and `Dog` inherit from `Pet`, and implement the `Animal` interface, via `AnimalMixin`.
* **Cat**
  * Ensure the class [Cat](pkg/Cat.py) supports all methods of `Pet` construction, successfully completing each of the method stubs in the class [CatTest](CatTest.py).
  * The mechanism by which a `Cat` speaks is by meowing; ensure a cat's `speak` method returns `meow` as a string.
* **Dog**
  * Ensure the class [Dog](pkg/Dog.py) supports all methods of `Pet` construction, successfully completing each of the method stubs in the class [DogTest](DogTest.py).
  * Note that the mechanism by which a `Dog` speaks is by barking; ensure a dog's `speak` method returns `bark` as a string.

## PetOwner

* Ensure each of the test cases in the class [PetOwner](pkg/PetOwner.py) successfully passes upon completion of each of the method stubs in the class [PetOwnerTest](PetOwnerTest.py).
  * `PetOwner(name: str, pets: List[Pet]) -> None`
  * `addPet(pet: Pet) -> None`
  * `removePet(pet: Pet) -> None`
  * `isOwnerOf(pet: Pet) -> bool`
  * `getYoungestPetAge() -> int`
  * `getOldestPetAge() -> int`
  * `getAveragePetAge() -> float`
  * `getNumberOfPets() -> int`
  * `name() -> str`
  * `pets() -> List[Pet]`
