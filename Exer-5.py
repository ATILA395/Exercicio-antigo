#Tabela de dados
dados = [
    ["Nome", "Nota 1", "Nota 2", "Nota 3", "Média"],
    ["Alice", 8.5, 7.0, 9.0, (8.5 + 7.0 + 9.0) / 3],
    ["Bob", 6.0, 5.5, 7.0, (6.0 + 5.5 + 7.0) / 3],
    ["Carlos", 9.0, 8.5, 10.0, (9.0 + 8.5 + 10.0) / 3],
    ["Diana", 7.0, 6.0, 8.0, (7.0 + 6.0 + 8.0) / 3],
]


def imprimir_tabela(dados):
    
    col_lengths = [max(len(str(item)) for item in col) for col in zip(*dados)]
    
    
    print("+" + "+".join("-" * (length + 2) for length in col_lengths) + "+")
    
    
    for row in dados:
        print("| " + " | ".join(f"{str(item):<{col_lengths[i]}}" for i, item in enumerate(row)) + " |")
        print("+" + "+".join("-" * (length + 2) for length in col_lengths) + "+")

# Chamar a função para imprimir a tabela
imprimir_tabela(dados)

