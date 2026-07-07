"""
    Module ecrit pour leçon9.
    Cet module contient des fonctions divers.

    >>> print(__tous__) # Liste toutes les fonctions de la module
"""

__all__ = [
    "Null", "notre_pow", "notre_max", "notre_min",
    "multiplier_par_2", "texte_brute",
    "temp_conv_table", "mots_compteur"
]

Null = 0
SETX = 1 # on flag

# MACROS
notre_pow = lambda x,y: x ** y
notre_pow.__doc__ = "Elever x a la puissance de y"

notre_max = lambda x,y: x if (x-y >= Null) else y
notre_max.__doc__ = "Donne la valeur qui est maximale x ou y"

notre_min = lambda x,y: y if notre_max(x,y) == x else x
notre_min.__doc__ = "Donne la valeur qui est minimale x ou y"

multiplier_par_2 = lambda x: x << SETX
multiplier_par_2.__doc__ = "Multiplie x(entier) par 2"

texte_brute = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

def temp_conv_table(debut=0, fin=100, etape=10, **plus):
    """
        Tableau de conversion de temperature
        (celcius -> fahrenheit -> kelvin)

        debut: valeur initiale a convertir en centigrade
        fin: valeur finale a convertir en centigrade
        etape: increment de debut a la fin
        **kwargs: TBA
    """

    print(
        f"{'°Centigrade':^20s}\t{'°Fahrenheit':^20s}\t{'Kelvin':^20s}")

    while(debut <= fin):
        fahr = ((9/5) * (debut)) + 32
        kelv = debut + 273.15
        print(f"{str(debut)+'°C':^20s}=>\t{str(int(fahr)) + '°F':^20s}=>\t{str(int(kelv)) + 'K':^20s}")
        debut += etape
    print(f"{'fin du tableau!'.upper():^72s}")

def __enlever_ponctuation__(word):
    """ Function Privee - enlever la ponctuation d'un mot """

    ponctuation = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~"
    for i in word:
        if(i in ponctuation):
            word = word.replace(i, "")

    return word

def mots_compteur(texte, limite=None) -> list:

    """
        Compte le nombre d'occurence des mots d'un texte
        texte: texte a traverser
        limit: arrete quand c'est atteign
    """

    result = {}
    mot_totale = 0
    boucle_compteur = 0

    texte = texte.replace('\n', " ")

    for i in texte.split(" "):
        i = __enlever_ponctuation__(i).lower()
        mot_compte = result.get(i, 0) + 1
        result[i] = mot_compte

        if(mot_compte == 1):
            mot_totale += 1
        boucle_compteur +=1

        if(limite and limite == boucle_compteur):
            break

    result['__total__'] = mot_totale
    result['__length__'] = len(texte)
    return [(i,v) for i,v in result.items()]

class ArtisteMalien(object):
    __nom__ = None
    __en_vie = None
    __sexe = None # 1 or 0 -> feminin par defaut
    _nationalite = "Mali"

    def __init__(self, nom, vie, sexe):
        self.__nom__ = nom
        self.__en_vie = vie
        self.__sexe = sexe

    def _vie_en_str(self):
        if(self.__en_vie):
            return "vivant"
        return "decedé" if self.__sexe else "decedée"

    def _sexe_en_str(self):
        if(self.__sexe == 1):
            return "masculin"
        return "feminine"

    def change_nom(self, nom):
        self.__nom__ = nom

    def change_vie(self, vie):
        self.__vie = vie

    def change_sexe(self, sexe):
        self.__sexe = sexe

    def en_string(self):
        return f"Artiste {self.__nom__} est du {self._nationalite}, est de sexe {self._sexe_en_str()} et {self._vie_en_str()}"