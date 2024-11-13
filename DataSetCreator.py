import random
import string

# Parámetros configurables
N = 100  # Número de líneas en cada dataset (puedes cambiar este valor)
word_min_len = 3  # Longitud mínima de las palabras
word_max_len = 10  # Longitud máxima de las palabras

# Generador de palabras aleatorias
def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Generador de pares de palabras para cada tipo de caso
def generate_word_pairs(case_type, N):
    word_pairs = []

    for _ in range(N):
        if case_type == 'similar':
            # Generar palabras similares con una pequeña modificación
            base_word = generate_random_word(random.randint(word_min_len, word_max_len))
            modified_word = list(base_word)
            idx = random.randint(0, len(modified_word) - 1)
            modified_word[idx] = random.choice(string.ascii_lowercase)
            word_pairs.append((base_word, ''.join(modified_word)))

        elif case_type == 'different':
            # Generar palabras completamente diferentes
            word1 = generate_random_word(random.randint(word_min_len, word_max_len))
            word2 = generate_random_word(random.randint(word_min_len, word_max_len))
            word_pairs.append((word1, word2))

        elif case_type == 'empty':
            # Generar un par con una palabra y una cadena vacía
            word1 = generate_random_word(random.randint(word_min_len, word_max_len))
            word_pairs.append((word1, ''))

        elif case_type == 'repeated':
            # Generar una palabra con caracteres repetidos
            repeated_char = random.choice(string.ascii_lowercase)
            length = random.randint(word_min_len, word_max_len)
            word_pairs.append((repeated_char * length, repeated_char * length))

        elif case_type == 'transpose':
            # Generar palabras que necesitan transposición
            base_word = generate_random_word(random.randint(word_min_len, word_max_len))
            if len(base_word) > 1:
                modified_word = list(base_word)
                i = random.randint(0, len(modified_word) - 2)
                # Intercambiar dos caracteres adyacentes
                modified_word[i], modified_word[i + 1] = modified_word[i + 1], modified_word[i]
                word_pairs.append((base_word, ''.join(modified_word)))
            else:
                # En caso de que la longitud sea 1, agrega el mismo par sin cambio
                word_pairs.append((base_word, base_word))

    return word_pairs

# Guardar el dataset en un archivo
def save_dataset(filename, word_pairs):
    with open(filename, 'w') as file:
        for word1, word2 in word_pairs:
            file.write(f"{word1} {word2}\n")

# Generar y guardar cada dataset
similar_pairs = generate_word_pairs('similar', N)
different_pairs = generate_word_pairs('different', N)
empty_pairs = generate_word_pairs('empty', N)
repeated_pairs = generate_word_pairs('repeated', N)
transpose_pairs = generate_word_pairs('transpose', N)

save_dataset("Codigos/Datasets/similar_dataset.txt", similar_pairs)
save_dataset("Codigos/Datasets/different_dataset.txt", different_pairs)
save_dataset("Codigos/Datasets/empty_dataset.txt", empty_pairs)
save_dataset("Codigos/Datasets/repeated_dataset.txt", repeated_pairs)
save_dataset("Codigos/Datasets/transpose_dataset.txt", transpose_pairs)

print("Datasets generados y guardados en los archivos correspondientes.")
