#!/usr/bin/python3
"""Module contenant la classe Square pour la task 3"""

class Square:
    """Classe qui définit un carré avec validation de taille et calcul de l'aire"""

    def __init__(self, size=0):
        """Constructeur d'un carré

        Args:
            size (int): taille du côté du carré (par défaut 0)

        Raises:
            TypeError: si size n'est pas un entier
            ValueError: si size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """Retourne l'aire du carré

        Returns:
            int: aire du carré
        """
        return self.__size * self.__size