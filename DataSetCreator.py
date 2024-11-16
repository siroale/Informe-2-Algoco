import random
import string

# Parámetros configurables
N = 50  # Número de líneas en cada dataset (puedes cambiar este valor)
small_word_len_min = 3   # Longitud mínima para palabras pequeñas
small_word_len_max = 7   # Longitud máxima para palabras pequeñas
medium_word_len_min = 8  # Longitud mínima para palabras medianas
medium_word_len_max = 12 # Longitud máxima para palabras medianas
large_word_len_min = 13  # Longitud mínima para palabras grandes
large_word_len_max = 17  # Longitud máxima para palabras grandes

# Generador de palabras aleatorias
def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Generador de pares de palabras para cada tipo de caso
def generate_word_pairs(case_type, word_length1, word_length2, N):
    word_pairs = []

    for i in range(N):
        if case_type == 'different':
            # Generar palabras completamente diferentes
            word1 = generate_random_word(word_length1)
            word2 = generate_random_word(word_length2)
            word_pairs.append((word1, word2))

        elif case_type == 'empty':
            # Generar un par con una palabra y una cadena vacía
            word1 = generate_random_word(word_length1)
            word_pairs.append((word1, '\0'))

        elif case_type == 'repeated':
            # Generar una palabra con al menos dos caracteres repetidos
            repeated_chars = ''.join(random.choices(string.ascii_lowercase, k=2))
            word = ''.join(random.choice(repeated_chars) for _ in range(word_length1))
            word_pairs.append((word, word))

        elif case_type == 'transpose':
            # Generar palabras que necesitan múltiples transposiciones
            base_word = generate_random_word(word_length1)
            modified_word = list(base_word)
            
            # Realizar varias transposiciones
            num_transpositions = random.randint(2, 4)  # Número de transposiciones
            for _ in range(num_transpositions):
                if len(modified_word) > 1:
                    i = random.randint(0, len(modified_word) - 2)
                    # Intercambiar dos caracteres adyacentes
                    modified_word[i], modified_word[i + 1] = modified_word[i + 1], modified_word[i]
                    
            word_pairs.append((base_word, ''.join(modified_word)))

        elif case_type == 'similar':
            # Generar palabras similares con una pequeña modificación
            base_word = generate_random_word(word_length1)
            modified_word = list(base_word)
            idx = random.randint(0, len(modified_word) - 1)
            # Modificar un solo carácter para hacer las palabras similares
            modified_word[idx] = random.choice(string.ascii_lowercase)
            word_pairs.append((base_word, ''.join(modified_word)))

        elif case_type == 'mixed':
            # Generar pares con longitudes diferentes
            # word1 y word2 tendrán longitudes diferentes
            word_length1 = random.randint(small_word_len_min, large_word_len_max)
            word_length2 = random.randint(small_word_len_min, large_word_len_max)
            while word_length1 == word_length2:  # Asegurarse que sean diferentes
                word_length2 = random.randint(small_word_len_min, large_word_len_max)
            
            word1 = generate_random_word(word_length1)
            word2 = generate_random_word(word_length2)
            word_pairs.append((word1, word2))

    return word_pairs

# Guardar el dataset en un archivo
def save_dataset(filename, word_pairs):
    with open(filename, 'w') as file:
        for word1, word2 in word_pairs:
            file.write(f"{word1} {word2}\n")

# Generar y guardar cada dataset con incrementos de tamaño

def generate_incremental_datasets(word_len_min, word_len_max, category, case_type):
    word_pairs = []
    for i in range(0, N, 10):
        # Calcular la longitud del tamaño de las palabras para cada bloque de 10
        word_length = word_len_min + (i // 10)  # Incrementar la longitud de la palabra
        if word_length > word_len_max:
            word_length = word_len_max
        
        # Generar las parejas de palabras con el tamaño calculado
        word_pairs += generate_word_pairs(case_type, word_length, word_length, 10)

    save_dataset(f"Datasets/{category}_{case_type}_dataset.txt", word_pairs)

# Generar datasets para cada caso
generate_incremental_datasets(small_word_len_min, small_word_len_max, 'small', 'different')
generate_incremental_datasets(medium_word_len_min, medium_word_len_max, 'medium', 'different')
generate_incremental_datasets(large_word_len_min, large_word_len_max, 'large', 'different')

generate_incremental_datasets(small_word_len_min, small_word_len_max, 'small', 'empty')
generate_incremental_datasets(medium_word_len_min, medium_word_len_max, 'medium', 'empty')

generate_incremental_datasets(small_word_len_min, small_word_len_max, 'small', 'repeated')
generate_incremental_datasets(medium_word_len_min, medium_word_len_max, 'medium', 'repeated')

generate_incremental_datasets(small_word_len_min, small_word_len_max, 'small', 'transpose')
generate_incremental_datasets(medium_word_len_min, medium_word_len_max, 'medium', 'transpose')

generate_incremental_datasets(small_word_len_min, small_word_len_max, 'small', 'similar')
generate_incremental_datasets(medium_word_len_min, medium_word_len_max, 'medium', 'similar')
generate_incremental_datasets(large_word_len_min, large_word_len_max, 'large', 'similar')

# Nuevo tipo de dataset con longitudes diferentes para las palabras
generate_incremental_datasets(small_word_len_min, small_word_len_max, 'small', 'mixed')
generate_incremental_datasets(medium_word_len_min, medium_word_len_max, 'medium', 'mixed')
generate_incremental_datasets(large_word_len_min, large_word_len_max, 'large', 'mixed')

print("Datasets generados y guardados en los archivos correspondientes.")
