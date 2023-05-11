import json

class User:
    def __init__(self, name):
        self.name = name
        self.interactions = []

    def add_interaction(self, interaction):
        self.interactions.append(interaction)

    def save(self):
        with open(f"users/{self.name}.json", "w") as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        user = cls(data["name"])
        user.interactions = data["interactions"]
        return user
