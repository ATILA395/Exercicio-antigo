# Pinheiro
def desenhar_pinheiro(altura):
    for i in range(altura):
        # Desenha espaços à esquerda para centralizar
        print(' ' * (altura - i - 1), end='')
        
        # Desenha o corpo do pinheiro com caracteres aleatórios
        for j in range(2 * i + 1):
            if j % 2 == 0:
                print('*', end='')  # Folhas
            else:
                print('o', end='')  # Enfeite
            
        print()  # Nova linha
    
    # Desenha o tronco do pinheiro
    for i in range(2):
        print(' ' * (altura - 1) + '|')  # Tronco centralizado

# Chama a função com a altura desejada
altura_do_pinheiro = 5
desenhar_pinheiro(altura_do_pinheiro)
