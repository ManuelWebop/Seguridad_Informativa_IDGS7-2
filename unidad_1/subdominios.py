'''
programa para encontrar subdominions de un sitio.
explicar que hace este script.
desarrollado por Manuel Francisco Amavizca Barrios.
'''
import requests
from os import path
import argparse
import sys

parse = argparse.ArgumentParser()
#print(f'{parse}\n\n')
parse.add_argument('-t', '--target', help='indica el dominio de la vistima')
parse = parse.parse_args()
#print(parse)
'''
este es un comentario multi-linea
hola, si.
'''
def main():
    if parse.target:
        if path.exists('subdominios.txt'):
            worldlist = open('subdominios.txt','r')
            worldlist = worldlist.read().split('\n')
            