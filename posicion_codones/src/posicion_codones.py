'''
NAME

    posicion_codones.py 

VERSION

    2.0

AUTHOR

    Miguel Ángel Flores Varela

CONTACT

    mfvarela@lcg.unam.mx

DESCRIPTION

    Este programa localiza la posición de los codones de inicio y final 
    en una secuencia dada de DNA, mostrando el transcrito derivado de esta.

CATEGORY
        Genómica

USAGE

    % py posicion_codones.py <path_archivo_de_entrada> <condón_de_inicio> <codón_de_paro>
    
'''


# ===========================================================================
# =                            imports
# ===========================================================================

# Importar las librerías necesarias.

import argparse
import re



# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Definir la función del programa.

descripcion = ("Este programa localiza la posición de los codones de \n",
             "inicio y final en una secuencia dada de DNA, mostrando el \n",
              "transcrito derivado de esta.")
parser = argparse.ArgumentParser(description=descripcion)


# Definir los argumentos.

parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='El path del archivo')

parser.add_argument('Inicio',
                    metavar='inicio',
                    type=str,
                    help='El codón de inicio')

parser.add_argument('Final',
                    metavar='final',
                    type=str,
                    help='El codón de paro')


# Ejecutar método parse_args()
args = parser.parse_args()



# ===========================================================================
# =                            main
# ===========================================================================

# Pedir el pad del archivo

ruta_archivo = args.Path


# Verificar que el archivo exista.

try:
    archivo = open(ruta_archivo, "r")
    secuencia = archivo.read().rstrip("\n")


    # Verificar que el archivo no esté vacío.

    if not secuencia:
        print("El archivo está vacío.")
        archivo.close()


    # Verificar que al archivo contenga solo As, Ts, Gs y Cs.

    elif re.search(r"[ATGC]", secuencia):
        if re.search(r"[^ATGC]", secuencia): 
            print("El archivo contiene caracteres no válidos.")
            archivo.close()


        # Obtener posiciones de codones y obtener el transcrito.

        else:
            p_c_inicio=secuencia.find(args.Inicio)
            sec_1=secuencia[p_c_inicio:]
            p_c_termino=sec_1.find(args.Final)+3
            sec_2=sec_1[:p_c_termino]
            transcrito_1=sec_2.replace('A','u').replace('T','a').replace('C','g').replace('G','c')
            transcrito_2=transcrito_1.upper()
            print("\nSecuencia de DNA:", secuencia)
            print("\n\nPosición del codon de inicio:", p_c_inicio) 
            print("\n\nPosición donde termina el codón de paro: ", p_c_termino) 
            print("\n\nFragmento que será RNA es:", transcrito_2, "\n")

    else:
        print("El archivo no contiene una secuencia de DNA.")

except IOError:
    print("No se encontró el archivo.")