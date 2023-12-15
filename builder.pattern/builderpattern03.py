class SandWich:
    def __init__(self) -> None:
        self._bread = None
        self._meat = None
        self._cheese = None
        self._vegetables = []
        self._sauces = []

    def __str__(self) -> str:
        ingredients = f"bread:{self._bread}|meat:{self._meat}"
        if self._cheese:
            ingredients += f"|cheese:{self._cheese}"
        ingredients += "|vegetable:" + "".join(self._vegetables)
        ingredients += "|sauces:" + "".join(self._sauces)
        return ingredients

class SandWitchBuilder:
    def __init__(self) -> None:
        self.sandwich = SandWich()

    def add_bread(self):
        pass
    def add_meat(self):
        pass
    def add_cheese(self):
        pass
    def add_vegetables(self):
        pass
    def add_sauces(self):
        pass
    def get_sandwich(self):
        pass

class ClubSandWichBuilder(SandWitchBuilder):
    def add_bread(self):
        self.sandwich._bread = 'white bread'
    def add_cheese(self):
        self.sandwich._cheese = 'chedar'
    def add_meat(self):
        self.sandwich._meat = 'chicken'
    def add_vegetables(self):
        self.sandwich._vegetables.append('carot')
        self.sandwich._vegetables.append('tomato')

    def add_sauces(self):
        self.sandwich._sauces.append('mayone')
        self.sandwich._sauces.append('mustard')

class VeggieSandWichBuilder(SandWitchBuilder):
    def add_bread(self):
        self.sandwich._bread = 'whole white bread'
    def add_cheese(self):
        self.sandwich._cheese = 'chedar'
    def add_meat(self):
        self.sandwich._meat = 'tofu'
    def add_vegetables(self):
        self.sandwich._vegetables.append('spinach')
        self.sandwich._vegetables.append('bell pepper')

    def add_sauces(self):
        self.sandwich._sauces.append('hummus')
        self.sandwich._sauces.append('tahini')

class Waiter:
    def __init__(self) -> None:
        self.sandwich_builder = None

    def get_builder(self, builder):
        self.sandwich_builder = builder
    def create_sandwich(self):
        self.sandwich_builder.add_bread()
        self.sandwich_builder.add_meat()
        self.sandwich_builder.add_cheese()
        self.sandwich_builder.add_vegetables()
        self.sandwich_builder.add_sauces()

    def serve_sandwich(self):
        return self.sandwich_builder.get_sandwich()
    
waiter = Waiter()
