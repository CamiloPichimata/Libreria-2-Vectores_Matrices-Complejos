import Libreria_Vectores_y_Matrices as vm
import math

def test_adicion_vectores_complejos():
    assert vm.adicion_vectores_complejos([[[ 8, 3]], [[-1,-4]], [[ 0,-9]]], [[[ 8,-3]], [[ 2, 5]], [[ 3, 0]]]) == [[[16, 0]], [[1, 1]], [[3, -9]]], 'Debe ser [[[16, 0]], [[1, 1]], [[3, -9]]]'

def test_inverso_aditivo_vc():
    assert vm.inverso_aditivo_vc([[[-5, 2]], [[ 3, 0]], [[ 0,-1]]]) == [[[5, -2]], [[-3, 0]], [[0, 1]]], 'Debe ser [[[5, -2]], [[-3, 0]], [[0, 1]]]'

def test_mult_escalar_vector():
    assert vm.mult_escalar_vector([-1,1], [[[-2,5], [-1,-1], [2,-9]]]) == [[[-3, -7], [2, 0], [7, 11]]], 'Debe ser [[[-3, -7], [2, 0], [7, 11]]]'

def test_adicion_matrices_complejas():
    assert vm.adicion_matrices_complejas([[[-8,-3], [-6, -4], [ 0,-4]], [[-1, 8], [ 6,-10], [ 8,-5]], [[ 4, 0], [ 8,  5], [-7,-9]]], [[[-7,-2], [-4,-2], [7, 7]], [[ 5, 9], [ 0, 3], [6,-5]], [[ 1, 5], [-6,-6], [5, 8]]]) == [[[-15, -5], [-10, -6], [7, 3]], [[4, 17], [6, -7], [14, -10]], [[5, 5], [2, -1], [-2, -1]]], 'Debe ser [[[-15, -5], [-10, -6], [7, 3]], [[4, 17], [6, -7], [14, -10]], [[5, 5], [2, -1], [-2, -1]]]'

def test_inverso_aditivo_mc():
    assert vm.inverso_aditivo_mc([[[ 7, 3], [-1, 7]], [[-9,-4], [-7,-9]]]) == [[[-7, -3], [1, -7]], [[9, 4], [7, 9]]], 'Debe ser [[[-7, -3], [1, -7]], [[9, 4], [7, 9]]]'

def test_mult_escalar_matriz():
    assert vm.mult_escalar_matriz([-2,3], [[[3,- 2], [ 8,-4]], [[4,-10], [-2,-8]]]) == [[[0, 13], [-4, 32]], [[22, 32], [28, 10]]], 'Debe ser [[[0, 13], [-4, 32]], [[22, 32], [28, 10]]]'

def test_transpuesta():
    assert vm.transpuesta([[[5,9], [-7,-5], [-1,-4]], [[8,2], [-3,-7], [ 7,-8]]]) == [[[5, 9], [8, 2]], [[-7, -5], [-3, -7]], [[-1, -4], [7, -8]]], 'Debe ser [[[5, 9], [8, 2]], [[-7, -5], [-3, -7]], [[-1, -4], [7, -8]]]'

def test_conjugada_mv():
    assert vm.conjugada_mv([[[-6, 1], [3,8]], [[ 2,-6], [3,0]]]) == [[[-6, -1], [3, -8]], [[2, 6], [3, 0]]], 'Debe ser [[[-6, -1], [3, -8]], [[2, 6], [3, 0]]]'

def test_adjunta():
    assert vm.adjunta([[[7,7], [3, 8], [  8, 4]], [[5,0], [8,-6], [-10,-1]]]) == [[[7, -7], [5, 0]], [[3, -8], [8, 6]], [[8, -4], [-10, 1]]], 'Debe ser [[[7, -7], [5, 0]], [[3, -8], [8, 6]], [[8, -4], [-10, 1]]]'

def test_producto_matricial():
    assert vm.producto_matricial([[[-6,2], [ 0,6], [ 7, 2]], [[ 6,9], [ 7,7], [-6,-6]], [[ 5,8], [-6,8], [ 6, 9]]], [[[9,-6], [-3,-4], [ 5,-2]], [[3, 6], [-1,-5], [ 0,-5]], [[9, 9], [ 8,-4], [-8,-4]]]) == [[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]], [[0, 165], [147, 26], [69, -36]]], 'Debe ser [[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]], [[0, 165], [147, 26], [69, -36]]]'
    assert vm.producto_matricial([[[2,1], [3, 0], [1,-1]], [[0,0], [0,-2], [7,-3]], [[3,0], [0, 0], [1,-2]]], [[[0,-1], [1,0]], [[0, 0], [0,1]]]) == "El tamaño de las matrices no es el apropiado", 'Debe ser "El tamaño de las matrices no es el apropiado"'

def test_accion_mc_vc():
    assert vm.accion_mc_vc([[[-1, 5], [1,-7], [-6,  3]], [[-3,-9], [2,-5], [ 1,-10]], [[-6, 5], [6,-5], [ 3, -2]]], [[[ 1,-3]], [[ 4, 3]], [[-3, 1]]]) == [[[54, -32]], [[0, 17]], [[41, 30]]], 'Debe ser [[[54, -32]], [[0, 17]], [[41, 30]]]'

def test_prod_interno():
    assert vm.prod_interno_v([[[ 2,-1]], [[-8,-5]], [[-2,-6]]], [[[ 6,-3]], [[ 5,-1]], [[-6,-2]]]) == [[[4, 1]]], 'Debe ser [[[4, 1]]]'

def test_norma_v():
    assert vm.norma_v([[[4, 5]], [[3, 1]], [[0,-7]]]) == 10.0, 'debe ser 10.0'

def test_distancia_2v():
    assert vm.distancia_2v([[[2, 7]], [[4,-1]], [[2,-4]]], [[[7, 8]], [[2,-8]], [[1, 4]]]) == 12.0, 'Deber ser 12.0'
    assert vm.distancia_2v([[[ 9,-7]], [[-1,-6]]], [[[7,-8]], [[5,-9]]]) == 7.0710678118654755, 'Debe ser 7.0710678118654755'

def test_mc_es_unitaria():
    assert vm.mc_es_unitaria([[[1/math.sqrt(2), 0], [0, 1/math.sqrt(2)]], [[0, 1/math.sqrt(2)], [1/math.sqrt(2), 0]]]) == True, 'Debe ser True'
    assert vm.mc_es_unitaria([[[0,1], [1,0], [0,0]], [[0,0], [0,1], [1,0]], [[1,0], [0,0], [0,1]]]) == False, 'Debe ser False'

def test_mc_es_hermitiana():
    assert vm.mc_es_hermitiana([[[3,0], [2,-1], [0,-3]], [[2,1], [0, 0], [1,-1]], [[0,3], [1, 1], [0, 0]]]) == True, 'Debe ser True'
    assert vm.mc_es_hermitiana([[[1,0], [3,-1]], [[3,1], [0, 1]]]) == False, 'Debse ser False'

def test_prod_tensor():
    assert vm.prod_tensor([[[1,1], [0,0]], [[1,0], [0,1]]], [[[-1,2], [-2,-2], [0,2]], [[ 2,3], [ 3, 1], [2,2]], [[-2,1], [ 1,-1], [2,1]]]) == [[[-3, 1], [0, -4], [-2, 2], [0, 0], [0, 0], [0, 0]], [[-1, 5], [2, 4], [0, 4], [0, 0], [0, 0], [0, 0]], [[-3, -1], [2, 0], [1, 3], [0, 0], [0, 0], [0, 0]], [[-1, 2], [-2, -2], [0, 2], [-2, -1], [2, -2], [-2, 0]], [[2, 3], [3, 1], [2, 2], [-3, 2], [-1, 3], [-2, 2]], [[-2, 1], [1, -1], [2, 1], [-1, -2], [1, 1], [-1, 2]]], 'Debe ser [[[-3, 1], [0, -4], [-2, 2], [0, 0], [0, 0], [0, 0]], [[-1, 5], [2, 4], [0, 4], [0, 0], [0, 0], [0, 0]], [[-3, -1], [2, 0], [1, 3], [0, 0], [0, 0], [0, 0]], [[-1, 2], [-2, -2], [0, 2], [-2, -1], [2, -2], [-2, 0]], [[2, 3], [3, 1], [2, 2], [-3, 2], [-1, 3], [-2, 2]], [[-2, 1], [1, -1], [2, 1], [-1, -2], [1, 1], [-1, 2]]]'

if __name__ == '__main__':
    test_adicion_vectores_complejos()
    test_inverso_aditivo_vc()
    test_mult_escalar_vector()
    test_adicion_matrices_complejas()
    test_inverso_aditivo_mc()
    test_mult_escalar_matriz()
    test_transpuesta()
    test_conjugada_mv()
    test_adjunta()
    test_producto_matricial()
    test_accion_mc_vc()
    test_prod_interno()
    test_norma_v()
    test_distancia_2v()
    test_mc_es_unitaria()
    test_mc_es_hermitiana()
    test_prod_tensor()
    print('Prueba exitosa')
