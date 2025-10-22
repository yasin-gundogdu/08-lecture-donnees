"""Lecture de listes d'entiers depuis un fichier et fonctions utilitaires.

Le fichier attendu contient une liste d'entiers par ligne, séparés par ';'.
Ce module fournit :
- read_data(FILENAME) -> list[list[int]]
- get_list_k(data, k) -> list[int]
- get_first(lst) -> int
- get_last(lst) -> int
- get_max(lst) -> int
- get_min(lst) -> int
- get_sum(lst) -> int

La fonction main() exécute des vérifications simples pour montrer le bon
fonctionnement des fonctions secondaires.
"""

from typing import List

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """Lire le fichier <FILENAME> et retourner une liste de listes d'entiers.

    Chaque ligne non vide du fichier doit contenir des entiers séparés par ';'.
    L'encodage utilisé est UTF-8.
    """
    result = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            s = line.strip()
            if not s:
                continue  # ignorer les lignes vides
            integers = list(map(int, s.split(';')))
            result.append(integers)
    return result

def get_list_k(data,k):
    """Retourner la k-ième liste de `data`."""
    return data[k]

def get_first(lst):
    """Retourner le premier élément de la liste. Lève IndexError si vide."""
    return lst[0]

def get_last(lst):
    """Retourner le dernier élément de la liste. Lève IndexError si vide."""
    return lst[-1]

def get_max(lst):
    """Retourner le maximum de la liste. Lève ValueError si vide."""
    return max(lst)

def get_min(lst):
    """Retourner le minimum de la liste. Lève ValueError si vide."""
    return min(lst)

def get_sum(lst: List[int]) -> int:
    """Retourner la somme des éléments de la liste."""
    return sum(lst)


#### Fonction principale

def main() -> None:
    """Point d'entrée : lire les données et vérifier les fonctions secondaires."""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
