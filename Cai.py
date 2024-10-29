class VariationUser:
    args = {}
    def __init__(self,**kwargs):
        self.args = kwargs

    def printinfo(self,processFunction:function):
        print(processFunction(self.args))
