# Definindo um enumerador de canais
# Canais são a quantidade de eletrodos de captação utilizados
# por aparelhos de eeg.

from enum import Enum

class Channels(Enum):
    SIXTEEN_CHAN               = 16
    TWENTYFOUR_CHAN            = 24
    THIRTYTWO_CHAN             = 32
    SIXTFOUR_CHAN              = 64
    ONEHUNDREDTWENTYEIGHT_CHAN = 128
    TWOHUNDREDFIFTYSIX_CHAN    = 256