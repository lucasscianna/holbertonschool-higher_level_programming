#!/usr/bin/python3
"""Module Square avec getter et setter pour size"""

class Square:
    """Classe qui définit un carré avec taille privée et validation"""

    def __init__(self, size=0):
        """Constructeur d'un carré

        Args:
            size (int): taille du côté du carré (par défaut 0)
        """
        # On utilise le setter pour valider et stocker la taille
        self.size = size

    @property
    def size(self):
        """Getter pour récupérer la taille du carré

        Returns:
            int: taille du côté du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour modifier la taille du carré avec validation

        Args:
            value (int): nouvelle taille du carré

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré

        Returns:
            int: aire du carré
        """
        return self.__size * self.__size

