from modelos.restaurante import Restaurante

restaurante_zergo = Restaurante('Zergo', 'Hamburgeria')
restaurante_zergo.receber_avaliacao('Jom Pidru', 9)
restaurante_place = Restaurante('Place', 'Pizzaria')
restaurante_italy = Restaurante('Italy', 'Italiana')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__': 
    main()