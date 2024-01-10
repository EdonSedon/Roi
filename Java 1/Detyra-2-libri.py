class Libri:
    
    def __init__(self):
        
        self.librat = ["Vdekja e bene me koncert", "Toke e permbytur", "Kronikat e Narnias", "Toke e shemtuar"]
        
        self.teDhenat = {
            "Vdekja e bene me koncert": {"ISBN":'', "numriLibrit":None, "autori":'',"vitiBotimit":None },
            "Toke e permbytur": {"ISBN":'', "numriLibrit":None, "autori":'',"vitiBotimit":None },
            "Kronikat e Narnias": {"ISBN":'',"numriLibrit":None, "autori":'',"vitiBotimit":None },
            "Toke e shemtuar": {"ISBN":'',"numriLibrit":None, "autori":'', "vitiBotimit":None }
        }
    
    
    def addDetails(self,libri, isbn, numriLibrit, autori, vitiBotimit):
        self.teDhenat[libri]["ISBN"] = isbn
        self.teDhenat[libri]["numriLibrit"] = numriLibrit
        self.teDhenat[libri]["autori"] = autori
        self.teDhenat[libri]["vitiBotimit"] = vitiBotimit
        
    def __str__(self) -> str:
        detajetELibrit = ""
        for libri, detajet in self.teDhenat.items():
            detajetELibrit += f'Libri me numer: ({detajet["numriLibrit"]}): Titulli: {libri}, Autori: {detajet["autori"]} botuar ne vitin {detajet["vitiBotimit"]}\n'
        return detajetELibrit
    
    def setVitiBotimit(self, libri, newPublishYear):
        self.teDhenat[libri]["vitiBotimit"] = newPublishYear
        
    
    
librat = Libri()

# Shto detajet ne libra
librat.addDetails("Vdekja e bene me koncert","ISBN123",1, "Robert Dalla", 2020)
librat.addDetails("Toke e permbytur","ISBN123", 2, "Izabela Xheka",2019)
librat.addDetails("Kronikat e Narnias","ISBN1234",3, "K.S Luis",1950)
librat.addDetails("Toke e shemtuar","ISBN1234", 4, "John Doe",2015)

# Ndrysho vitin e botimit te nje libri
librat.setVitiBotimit("Vdekja e bene me koncert",2024)

# Zgjedh librit per te ndryshuar vitin e botimit
def ndrroVitin():
    while True:
        print("Zgjidhni nje liber per te ndryshuar vitin e botimit:")
        
        for i, libri in enumerate(librat.librat, start=1):
            print(f"{i}. {libri}")

        try:
            numriLibrit = int(input("Zgjedhni nje numer te librit (shtypni 0 për të mbyllur programin), Printimi i Librave do te shfaqet pas mbylljes se programit: "))
            
            if numriLibrit == 0:
                break
            
            if 1 <= numriLibrit <= len(librat.librat):
                #indeksi fillon prej 0-os
                viti_i_ri = int(input(f"Shkruani vitin e ri të botimit për librin '{librat.librat[numriLibrit-1]}': "))
                librat.setVitiBotimit(librat.librat[numriLibrit-1], viti_i_ri)
                libriZgjedur = librat.librat[numriLibrit-1]
                print(f'viti i botimit te librit me titull : {libriZgjedur} u ndryshua me sukses')
                print('-------------------------------------------------------------')
            else:
                print("Numer i gabuar i librit.")
        
        except ValueError:
            print("Ju lutem shkruani nje numer të plotë.")

ndrroVitin()
# Printo te gjitha librat
print(librat)

