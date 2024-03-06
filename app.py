from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_zergo = Restaurante('Zergo', 'Hamburgeria')
bebida_suco = Bebida('Suco de Laranja', 7, 'Tamanho grande')
prato_refeicao = Prato('Burger', 18, '1x Carne, 1x Queijo, 1x Molho-Casa')
restaurante_place = Restaurante('Place', 'Pizzaria')
restaurante_italy = Restaurante('Italy', 'Italiana')

def main():
    '''Chama o método "listar_restaurantes" que lista os restaurantes.'''
    print(bebida_suco)
    print(prato_refeicao)

if __name__ == '__main__': 
    main()