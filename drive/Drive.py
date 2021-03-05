# classe raiz para ser herdada por todos os drivers que se deseja utilizar
# defini apenas os atributos principais de um driver para que o sistema possa 
# funcionar de forma mínima para testes ou demonstrações.

import Channels
class Drive(Channels):
    qntChannel = Channels.SIXTEEN_CHAN    
    
    def __init__(self):
        self.samplerate = 1024

    print (qntChannel)
    print (samplerate)