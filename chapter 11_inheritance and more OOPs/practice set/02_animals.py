'''example of multi-level inheritance'''

class Animals:
    animalType="mammals"


class Pets(Animals):
    petcolor="white"


class Dogs(Pets):

    @staticmethod #(bark don't use any class/instance attributes)
    def bark():
        print("Bow Bow")


d=Dogs()
d.bark()