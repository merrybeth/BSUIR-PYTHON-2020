class Singletone:
    __instance = None

    def __init__(self):
        if not Singletone.__instance:
            print("called")
        else:
            print("instance created:", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singletone()
        return cls.__instance


a = Singletone()
print("object created", Singletone.get_instance())
a1 = Singletone()
