import os
import string
import unicodedata
from collections import Counter

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))

text_in_file = None

if os.path.exists(desktop + "/texto.txt"):
    with open(desktop + "/texto.txt", 'r', encoding="utf-8") as f:
        content = f.read()
        text_in_file = content

        text_in_file = unicodedata.normalize('NFD', text_in_file)
        text_in_file = ''.join(c for c in text_in_file if unicodedata.category(c) != 'Mn')
        text_in_file = text_in_file.lower()
        word_count =  str(len(text_in_file.split()))
        counter_found = Counter(text_in_file.split())

        print("Total de palabras: " + word_count)
        print("Total de caracteres: " + str(len(text_in_file)))
        print("Las 5 palabras más frecuentes: " + str(counter_found.most_common(5)))

        resultadoFinal = {
            "Total de palabras:": word_count,
            "Total de caracteres:": str(len(text_in_file)),
            "Las 5 palabras más frecuentes:": str(counter_found.most_common(5))
        }

    with open (desktop + "/resultado.txt", "w", encoding="utf-8") as file:
        resultado  = file.write(str(resultadoFinal))
    
    print("¡Archivo creado con exito en el escritorio!")
else:
    print("¡No se encuentra archivo para leer en el escritorio! (texto.txt)")