import hashlib

def md5(sentence):
    return hashlib.md5(sentence.encode('utf-8')).hexdigest()

def permutations(liste, nb_sample):
    if nb_sample == 1:
        return [[i] for i in liste]
    else:
        permutations_list = []
        for i in liste:
            liste_copy = liste.copy()
            liste_copy.remove(i)
            permutations_list += [[i] + j for j in permutations(liste_copy, nb_sample - 1)]
        return permutations_list

indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14 ,15]
characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a" , "b", "c", "d", "e", "f"]
mots = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "a", "b", "c", "d", "e", "f"]

start_of_sentence = "Hello friend ! The beginning of the md5 hash of this sentence starts with "

for length in range(1, 15):
    perms = permutations(indexes, length)
    for selected_indexes in perms:
        sentence = start_of_sentence + ", ".join([mots[i] for i in selected_indexes[:-1]]) + " et " + mots[selected_indexes[-1]] + ". Pretty cool right ?"
        selected_chars = [characters[i] for i in selected_indexes]
        if md5(sentence)[:length] == "".join(selected_chars):
            print(length, sentence, md5(sentence))
