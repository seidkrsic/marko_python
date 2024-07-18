from string import punctuation 

class Analyser: 
    def __init__(self, string): 
        for symbol in punctuation: 
            string = string.replace(symbol,"") 
        
        string = string.lower()
        lista_od_stringa = string.split(" ") 
        self.words = lista_od_stringa 
    
    def number_of_words(self):
        print(len(self.words))


