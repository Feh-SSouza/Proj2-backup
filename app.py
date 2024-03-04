from modelos.restaurante import Restaurante

restaurante_zergo = Restaurante('Zergo', 'Hamburgeria')
restaurante_zergo.receber_avaliacao('Jom Pidru', 5)
restaurante_zergo.receber_avaliacao('Gosavo', 5)
restaurante_zergo.receber_avaliacao('Yhago', 3)
restaurante_place = Restaurante('Place', 'Pizzaria')
restaurante_italy = Restaurante('Italy', 'Italiana')

def main():
    '''Chama o método "listar_restaurantes" que lista os restaurantes.'''
    Restaurante.listar_restaurantes()

if __name__ == '__main__': 
    main()