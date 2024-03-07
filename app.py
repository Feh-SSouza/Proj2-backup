from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_zergo = Restaurante('Zergo', 'Hamburgeria')
bebida_suco = Bebida('Suco de Laranja', 7.90, 'Tamanho grande')
bebida_suco.aplicar_desconto()

prato_refeicao = Prato('Burger', 18.90, '1x Carne, 1x Queijo, 1x Molho-Casa')
prato_refeicao.aplicar_desconto()

restaurante_zergo.adicionar_cardapio(bebida_suco)
restaurante_zergo.adicionar_cardapio(prato_refeicao)

restaurante_place = Restaurante('Place', 'Pizzaria')
restaurante_italy = Restaurante('Italy', 'Italiana')

def main():
    '''Chama o método "listar_restaurantes" que lista os restaurantes.'''
    restaurante_zergo.exibir_cardapio

if __name__ == '__main__': 
    main()