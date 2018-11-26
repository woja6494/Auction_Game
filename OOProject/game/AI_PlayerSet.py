



class AIPlayerSet:
    instance = None

    @staticmethod
    def get_instance():
        if AIPlayerSet.instance is None:
            AIPlayerSet()
            print("BackgroundSet instance created")
        return AIPlayerSet.instance

    def __init__(self):
        if AIPlayerSet.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AIPlayerSet.instance = self


    AI_ID = 0
    money = 0

    public