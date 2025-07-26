import random
import string

# String alvo
target = "FOA"
target_len = len(target)

# Função para gerar string aleatória
def random_string(length):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

# Contadores
total_iterations = 0
found_count = 0

print("Iniciando busca pela string 'FOA'...")

while found_count < 3:
    attempts = 0  # tentativas para esta ocorrência
    while True:
        attempts += 1
        total_iterations += 1
        generated = random_string(target_len)
        if generated == target:
            found_count += 1
            print(f"Ocorrência {found_count}: '{generated}' encontrada após {attempts} tentativas.")
            break

print(f"\nTotal de tentativas para encontrar 'FOA' 3 vezes: {total_iterations}")
