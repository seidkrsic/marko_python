

class Vagon:
    def __init__(self, code):
        self.code = code 
        self.passengers = [] 

  


class Train(Vagon):
    def __init__(self,code):
        super.__init__(code) 
        self.wagons = []
