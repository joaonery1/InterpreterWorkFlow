#!/usr/bin/env python3
# OPENCL LIBRARY
import pyopencl as cl

# VGL LIBRARYS
import vgl_lib as vl

# TO WORK WITH MAIN
import numpy as np

# IMPORTING METHODS
from cl2py_ND import * 



# IMPORTING METHODS FROM VGLGui
import sys
import os

sys.path.append(os.getcwd())
sys.path.insert(0,'/VGLGui/')
from VGLGui.readWorkflow import *


import time as t



vl.vglClInit()     #inicio das estruturas vgl

fileRead(lstGlyph) #leitura do arquivo
msg = ""
img_input = vl.VglImage(sys.argv[1], None, vl.VGL_IMAGE_2D_IMAGE(), vl.IMAGE_ND_ARRAY())
vl.vglLoadImage(img_input)
vl.vglClUpload(img_input)

img_output = vl.create_blank_image_as(img_input)
img_output.set_oclPtr( vl.get_similar_oclPtr_object(img_input) )
vl.vglAddContext(img_output, vl.VGL_CL_CONTEXT())







for vGlyph in lstGlyph:

    if vGlyph.func == 'in': #imagem de entrada
        print("")
    
    elif vGlyph.func == 'vstrflat': #elementro estruturante 
        window = vl.VglStrEl()
        window.constructorFromTypeNdim(vl.VGL_STREL_CROSS(), 2)
    
    elif vGlyph.func == 'out': #imagem de saida
        print("")

    elif vGlyph.func == 'kmul': #funcao copy
        inicio = t.time()
        vglClNdCopy(img_input, img_output)
        fim = t.time()
        vl.vglCheckContext(img_output, vl.VGL_RAM_CONTEXT())
        vl.vglSaveImage("img-vglNdCopy.jpg", img_output)
        msg = msg + "Tempo de execução do método vglClNdCopy:\t" +str( round( (fim-inicio), 9 ) ) +"s\n"
        print(msg)

    elif vGlyph.func == 'vero': #funcao erosion
        inicio = t.time()
        vglClNdDilate(img_input, img_output, window)
        fim = t.time()
        vl.vglCheckContext(img_output, vl.VGL_RAM_CONTEXT())
        vl.vglSaveImage("img-vglNdDilate.jpg", img_output)
        msg = msg + "Tempo de execução do método vglClNdDilate:\t" +str( round( (fim-inicio), 9 ) ) +"s\n"
        print(msg)
  

	

'''
para execução no MakeFile:
abrir diretório do arquivo no terminal por exemplo: cd /InterpreterWorkflow/VisionGL/src/py
verificar no arquivo MakeFile_Python qual o programa a ser executado
executar programa : make -f Makefile_python rundemopy
'''



