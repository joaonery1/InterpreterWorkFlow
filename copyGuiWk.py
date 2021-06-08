# Objective: read VGLGui workflow file and load content into memory
# File type: structure.txt

#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import string
from collections import defaultdict

# Structure for storing Glyphs in memory
class objGlyph(object):
        
    #Glyph:[Library]:comment::localhost:[Glyph_ID]:[Glyph_X]:[Glyph_Y]:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]    
    def __init__(self, vlibrary, vfunc, vlocalhost, vglyph_id, vglyph_x, vglyph_y, vlst_par):       
        self.library = vlibrary       #library name (Ex: VisionGL)
        self.func = vfunc             #function
        self.localhost = vlocalhost   #folder where the image file or library function is located
        self.glyph_id = vglyph_id     #glyph identifier code
        self.glyph_x = vglyph_x       #numerical coordinate of the glyph's linear position on the screen 
        self.glyph_y = vglyph_y       #numerical coordinate of the column position of the Glyph on the screen
        self.lst_par = vlst_par       #parameter list

# Structure for storing Parameters in memory
class objGlyphParameters(object):

    def __init__(self, vglyph_id, vname, vvalue):
        self.glyph_id = vglyph_id   #glyph identifier code
        self.name = vname           #variable name
        self.value = vvalue         #variable value
        
# Structure for storing Connections in memory
class objConnection(object):

    #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
    def __init__(self, vtype, voutput_glyph_id, voutput_varname, vinput_glyph_id, vinput_varname):       
        self.type = vtype                           #type 'data', 'controle' 
        self.output_glyph_id = voutput_glyph_id     #glyph identifier code output
        self.output_varname = voutput_varname      #nome variável saída
        self.input_glyph_id = vinput_glyph_id       #glyph identifier code input
        self.input_varname = vinput_varname         #nome variável entrada

class objNodeParameters(object):
    def __init__(self,vinput,voutput,vready,vdone):
        self.input = vinput
        self.ouptut = voutput
        vready = False
        vdone = False
        self.ready = vready
        self.done = vdone

# File to be read
vfile = 'fileread/data.wksp'

lstGlyph = []                   #List to store Glyphs
lstGlyphPar = []                #List to store Glyphs Parameters
lstConnection = []              #List to store Connections
lstNodeParameters = []

vGlyph = objGlyph               #Glyph in memory 
vGlyphPar = objGlyphParameters  #Glyp parameters in memory
vConnection = objConnection     #Connection in memory
vNodePar = objNodeParameters


'''
laço que percorre a lista de glifos
    se o glifo estiver READY=TRUE e DONE=FALSE
        executar o glifo
        atualizar status para DONE=TRUE
        atualizar o status das arestas de saída para READY=TRUE
            se o glifo onde incide a aresta estiver com todas as arestas READY=TRUE
               atualizar o status do glifo para READY=TRUE
'''


# Method for reading the workflow file
def fileRead(lstGlyph):
    try:
        if os.path.isfile(vfile):
            i = 0 #cout variable 
            # Opens the workflow file
            file1 = open(vfile,"r")
            for line in file1:
                i+=1 #count variable for lines

                # Creates the glyphs of the workflow file
                if 'glyph:' in line.lower():
                    try:
                        contentGly = line.split(':')    #extracts the contents of the workflow file line in a list separated by the information between the ":" character
                        contentGlyPar = []              #clears the glyph parameter list
                        vparName = ''
                        vparValue = ''

                        #Creates the parameters of the Glyph
                        #:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]
                        contentGlyPar = contentGly[9].split(' ')
                        for vpar in contentGlyPar:
                            if vpar != '' and vpar != '\n':
                                vparName = vpar.replace('-', '')                        
                                vGlyphPar = objGlyphParameters(contentGly[5], vparName, 'fixo')
                                lstGlyphPar.append(vGlyphPar)
                                
                                #if vparName != '' and vparName != vpar:
                                #    vGlyphPar = objGlyphParameters(contentGly[5], vparName, vparValue)
                                #    lstGlyphPar.append(vGlyphPar)
                                #    vparName = ''
                                #    vparValue = ''
                                #else:
                                #    if vpar.find('-') >= 0:
                                #        vparName = vpar.replace('-', '')
                                #    else:
                                #        vparValue = vpar

                        #Create the Glyph
                        vGlyph = objGlyph(contentGly[1], contentGly[2], contentGly[4], contentGly[5], contentGly[6], contentGly[7], lstGlyphPar)
                        lstGlyph.append(vGlyph)
                    except IndexError as d:
                        print("Falta indices no glifo",{d},'na linha ',{i},'do arquivo')
                # Creates the connections of the workflow file
                if 'nodeconnection:' in line.lower():
                    try:
                        contentCon = line.split(':')
                        vConnection = objConnection(contentCon[1], contentCon[2], contentCon[3], contentCon[4], contentCon[5])
                        lstConnection.append(vConnection)
                        
                    except IndexError as c:
                        print('Falta indices nos nós de conexões',{c},'na linha ',{i},'do arquivo')
    
    finally:
        file1.close()

# Program execution
lstGlyph = []
lstConnection = []
contentGly = []
contentCon = []

# Reading the workflow file
try:
    fileRead(lstGlyph)
except UnboundLocalError as c:
    print("Arquivo inexistente",{c})
'''
# Shows the content of the Glyphs
for vGlyph in lstGlyph: 
    print("Library:", vGlyph.library, "Function:", vGlyph.func, "Localhost:", vGlyph.localhost, "Glyph_Id:", vGlyph.glyph_id, 
          "Position_Line:", vGlyph.glyph_x, "Position_Column:", vGlyph.glyph_y)#, "Parameters:", vGlyph.lst_par)

# Shows the content of the Connections
for vConnection in lstConnection:
    print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
          "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)
'''