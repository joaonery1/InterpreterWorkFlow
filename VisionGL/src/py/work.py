from readWorkflow import *

# IMPORTING METHODS FROM VISIONGL
#sys.path.insert(0,'VisionGL/src/py')
#from VisionGL.src.py import benchmark_clnd

import os
os.environ['PYOPENCL_COMPILER_OUTPUT'] = '1'

#import pyopencl as cl

# VGL LIBRARYS
#import vglImage as vl

# TO WORK WITH MAIN
import numpy as np

# IMPORTING METHODS
#from cl2py_ND import * 

# IMPORTING METHODS FROM VGLGui
import sys

import time as t

#vl.vglClInit()     #inicio das estruturas vgl

#Show info
def procShowInfo():
    for vGlyph in lstGlyph:
        print("Library:", vGlyph.library, "Function:", vGlyph.func, "Localhost:", vGlyph.localhost, "Glyph_Id:", vGlyph.glyph_id, 
            "Position_Line:", vGlyph.glyph_x, "Position_Column:", vGlyph.glyph_y)#, "Parameters:", vGlyph.lst_par)

        #Shows the list of glyph inputs
        for vGlyphIn in vGlyph.lst_input:
            print("Glyph_Id:", vGlyph.glyph_id, "Glyph_In:", vGlyphIn)

        #Shows the list of glyph outputs
        for vGlyphOut in vGlyph.lst_output:
            print("Glyph_Id:", vGlyph.glyph_id, "Glyph_Out:", vGlyphOut)

    # Shows the content of the Connections
    for vConnection in lstConnection:
        print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
            "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)

# Program execution

# Reading the workflow file and loads into memory all glyphs and connections
fileRead(lstGlyph)

def salvando2d(img, name):
	# SAVING IMAGE img
	ext = name.split(".")
	ext.reverse()

	#vl.vglClDownload(img)
	vl.vglCheckContext(img, vl.VGL_RAM_CONTEXT())

	if( ext.pop(0).lower() == 'jpg' ):
		if( img.getVglShape().getNChannels() == 4 ):
			vl.rgba_to_rgb(img)
	
	vl.vglSaveImage(name, img)



img_in_path = sys.argv[1]
nSteps		= int(sys.argv[2])
img_out_path= sys.argv[3]

msg = ""

vl.vglClInit()



#Update the status of glyph entries
for vGlyph in lstGlyph:

    #Glyph execute
    if vGlyph.getGlyphReady() and vGlyph.getGlyphDone() == False:
        #Image Input
        if vGlyph.func == 'in':
            img_input = vl.VglImage(img_in_path, None, vl.VGL_IMAGE_2D_IMAGE())
            vl.vglLoadImage(img_input)
            if( img_input.getVglShape().getNChannels() == 3 ):
                vl.rgb_to_rgba(img_input)
            
            vl.vglClUpload(img_input)
            
            img_output = vl.create_blank_image_as(img_input)
            img_output.set_oclPtr( vl.get_similar_oclPtr_object(img_input) )
            vl.vglAddContext(img_output, vl.VGL_CL_CONTEXT())
            
            convolution_window_2d_3x3 = np.array((	(1/16, 2/16, 1/16),
                                                    (2/16, 4/16, 2/16),
                                                    (1/16, 2/16, 1/16) ), np.float32)
            convolution_window_2d_5x5 = np.array((	(1/256, 4/256,  6/256,  4/256,  1/256),
                                                    (4/256, 16/256, 24/256, 16/256, 4/256),
                                                    (6/256, 24/256, 36/256, 24/256, 6/256),
                                                    (4/256, 16/256, 24/256, 16/256, 4/256),
                                                    (1/256, 4/256,  6/256,  4/256,  1/256) ), np.float32)

        #elif vGlyph.func == 'vstrflat': #Structuring element 
        #    window = vl.VglStrEl()
        #    window.constructorFromTypeNdim(vl.VGL_STREL_CROSS(), 2)

        #elif vGlyph.func == 'out': #Image Output
        #    img_output = vl.create_blank_image_as(img_input)
        #    img_output.set_oclPtr( vl.get_similar_oclPtr_object(img_input) )
        #    vl.vglAddContext(img_output, vl.VGL_CL_CONTEXT())

        #elif vGlyph.func == 'kmul': #Function copy
        #    inicio = t.time()
        #    vglClNdCopy(img_input, img_output)
        #    fim = t.time()
        #    vl.vglCheckContext(img_output, vl.VGL_RAM_CONTEXT())
        #    vl.vglSaveImage("img-vglNdCopy.jpg", img_output)
        #    msg = msg + "Tempo de execução do método vglClNdCopy:\t" +str( round( (fim-inicio), 9 ) ) +"s\n"
        #    print(msg)

        #elif vGlyph.func == 'vero': #Function erosion
        #    inicio = t.time()
        #    vglClNdDilate(img_input, img_output, window)
        #    fim = t.time()
        #    vl.vglCheckContext(img_output, vl.VGL_RAM_CONTEXT())
        #    vl.vglSaveImage("img-vglNdDilate.jpg", img_output)
        #    msg = msg + "Tempo de execução do método vglClNdDilate:\t" +str( round( (fim-inicio), 9 ) ) +"s\n"
        #    print(msg)

        #Sets all glyph outputs as executed 
        vGlyph.setGlyphOutputAll(True)

        #Sets all glyph outputs as executed
        vGlyph.setGlyphInputAll(True)

        #Defines that the glyph was executed
        vGlyph.setGlyphDone(True)

# Shows the content of the Glyphs
procShowInfo()
