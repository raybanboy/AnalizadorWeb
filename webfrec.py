# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:31:48 2019

@author: josete
"""
import requests
import html2text
import re

def descargar_pagina(url):
    '''
    Lee una pagina web y la convierte a texto plano
    '''
    page = requests.get(url)
    content = html2text.html2text(page.text)
    return content

def contar_palabras(texto):
    '''Con que frecuencia aparece una palabra, y ordena las mismas de mayor amenor frecuencia'''
    frec = {}
    texto = re.sub('[^\w\s]+','',texto)
    for w in texto.lower().split():
        if len(w) > 3:
            frec[w] = frec.get(w,0) + 1
    frec_sorted = sorted(frec.items(),key=lambda x:x[1],reverse=True)
    
    return frec_sorted