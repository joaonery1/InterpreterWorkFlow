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



vl.vglClInit()

fileRead(lstGlyph) #leitura do arquivo



for vGlyph in lstGlyph:
    if vGlyph.func == 'in':
        img_input = vl.VglImage(sys.argv[1], None, vl.VGL_IMAGE_2D_IMAGE(), vl.IMAGE_ND_ARRAY())
        vl.vglLoadImage(img_input)
        vl.vglClUpload(img_input)
    
    elif vGlyph.func == 'vstrflat':
        window = vl.VglStrEl()
        window.constructorFromTypeNdim(vl.VGL_STREL_CROSS(), 2)
    
    elif vGlyph.func == 'out':
        img_output = vl.create_blank_image_as(img_input)
        img_output.set_oclPtr( vl.get_similar_oclPtr_object(img_input) )
        vl.vglAddContext(img_output, vl.VGL_CL_CONTEXT())


    elif vGlyph.func == 'copy':
        inicio = t.time()
        vglClNdCopy(img_input, img_output)
        fim = t.time()
        vl.vglCheckContext(img_output, vl.VGL_RAM_CONTEXT())
        vl.vglSaveImage("img-vglNdCopy.jpg", img_output)
        msg = msg + "Tempo de execução do método vglClNdCopy:\t" +str( round( (fim-inicio), 9 ) ) +"s\n"
    else:
        print("ERROR")





