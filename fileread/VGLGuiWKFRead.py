# Objective: read VGLGui workflow file and load content into memory
# File type: structure.txt

#
import re
import os
import string
from collections import defaultdict

# Structure for storing Glyphs in memory
# Glyph represents a function
class objGlyph(object):
        
    #Glyph:[Library]:comment::localhost:[Glyph_ID]:[Glyph_X]:[Glyph_Y]:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]    
    def __init__(self, vlibrary, vfunc, vlocalhost, vglyph_id, vglyph_x, vglyph_y):       
        self.library = vlibrary                 #library name (Ex: VisionGL)
        self.func = vfunc                       #function
        self.localhost = vlocalhost             #folder where the image file or library function is located
        self.glyph_id = vglyph_id               #glyph identifier code
        self.glyph_x = vglyph_x                 #numerical coordinate of the glyph's linear position on the screen 
        self.glyph_y = vglyph_y                 #numerical coordinate of the column position of the Glyph on the screen
        self.ready = False                      #TRUE = glyph is ready to run
        self.done = False                       #TRUE = glyph was executed
        self.lst_par = [objGlyphParameters]     #parameter list
        self.lst_input = [objGlyphInput]        #glyph input list
        self.lst_output = [objGlyphOutput]      #glyph output list

    #Add glyph parameter function
    def funcGlyphAddPar (self, vGlyphPar):
        self.lst_par.append(vGlyphPar)

    #Add glyph input function
    def funcGlyphAddIn (self, vGlyphIn):
        self.lst_input.append(vGlyphIn)

    #Add glyph output function 
    def funcGlyphAddOut (self, vGlyphOut):
        self.lst_output.append(vGlyphOut)

    #Function to update glyph status
    #def funcGlyphUpdateStatus(self:
    #    for vGlyphIn in lst_input:
    #        self.ready = True
    #        if self. 

# Structure for storing Parameters in memory
class objGlyphParameters(object):

    def __init__(self, vnamepar, vvaluepar):
        self.name = vnamepar           #variable name
        self.value = vvaluepar         #variable value

# Structure for storing Glyphs input list in memory
class objGlyphInput(object):

    def __init__(self, vnamein, vstatusin):
        self.namein = vnamein         #glyph input name
        self.statusin = vstatusin     #glyph input status

        #def __repr__(self):
        #    return "{},{}".format(self.namein,self.statusin)

# Structure for storing Glyphs output list in memory
class objGlyphOutput(object):

    def __init__(self, vnameout, vstatusout):
        self.nameout = vnameout     #glyph output name
        self.statusout = vstatusout       #glyph output status

# Structure for storing Connections in memory
# Images are stored on edges (connections between Glyphs)
class objConnection(object):

    #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
    def __init__(self, vtype, voutput_glyph_id, voutput_varname, vinput_glyph_id, vinput_varname):       
        self.type = vtype                           #type 'data', 'controle' 
        self.output_glyph_id = voutput_glyph_id     #glyph identifier code output
        self.output_varname = voutput_varname       #variable name output
        self.input_glyph_id = vinput_glyph_id       #glyph identifier code input
        self.input_varname = vinput_varname         #variable name input
        self.image = None                           #image
        self.ready = False                          #False = unread or unexecuted image; True = image read or executed

# File to be read
vfile = 'fileread/data.wksp'

lstGlyph = []                   #List to store Glyphs
lstGlyphPar = []                #List to store Glyphs Parameters
lstConnection = []              #List to store Connections
lstGlyphIn = []                 #List to store Glyphs Inputs
lstGlyphOut = []                #List to store Glyphs Outputs

vGlyph = objGlyph               #Glyph in memory 
vGlyphPar = objGlyphParameters  #Glyph parameters in memory
vGlyphIn = objGlyphInput        #Glyph input in memory
vGlyphOut = objGlyphOutput      #Glyph output in memory
vConnection = objConnection     #Connection in memory

# Method for reading the workflow file
def fileRead(lstGlyph):
    if os.path.isfile(vfile):

        # Opens the workflow file
        file1 = open(vfile,"r")
        for line in file1:

            # Creates the glyphs of the workflow file
            if 'glyph:' in line.lower():

                contentGly = line.split(':')     #extracts the contents of the workflow file line in a list separated by the information between the ":" character
                contentGlyPar = []               #clears the glyph parameter list
                lstParAux = [objGlyphParameters] #auxiliary parameter list

                #Create the Glyph
                vGlyph = objGlyph(contentGly[1], contentGly[2], contentGly[4], contentGly[5], contentGly[6], contentGly[7])

                #Identifies the parameters
                #:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]
                contentGlyPar = contentGly[9].split(' ')
                for vpar in contentGlyPar:
                    if vpar != '' and vpar != '\n':

                        # Examples:
                        # -wh -hw -dd 
                        # -real 'width_size'
                        # -backvalue 0 -masklogic 1
                        # -conn 1  
                        # -real '100'              
                        vGlyphPar = objGlyphParameters  

                        #Differentiates parameter name and value
                        if vpar[0] == '\'' or vpar.isdigit():
                            vGlyphPar = objGlyphParameters('Value', vpar.replace("'", '')) 

                        if vpar[0] == "-":             
                            if vpar[1].isdigit():
                                vGlyphPar = objGlyphParameters('Value', vpar.replace("-", ''))
                            else:
                                vGlyphPar = objGlyphParameters('Name', vpar.replace('-', ''))

                        lstParAux.append(vGlyphPar)
                        
                #Creates the parameters of the Glyph
                for i in enumerate (lstParAux):

                    vParAux = lstParAux[i].__name__
                    vParAuxNext = lstParAux[i+1].__name__

                    #Um nome de parâmetro seguido de outro nome de parâmetro
                    if vParAux.Name == 'Name' and vParAuxNext.__name__ == 'Name':
                        vGlyphPar = objGlyphParameters(lstParAux[i].Name, '')

                    #Um nome de parâmetro seguido de um valor
                    if vParAux.Name == 'Name' and vParAuxNext.__name__ == 'Value':
                        vGlyphPar = objGlyphParameters(vParAux.Name, vParAuxNext.Value)


                    vGlyph.funcGlyphAddPar(vGlyphPar)                     

                lstGlyph.append(vGlyph)

            #Creates the connections of the workflow file
            #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
            if 'nodeconnection:' in line.lower():
                contentCon = line.split(':')
                vConnection = objConnection(contentCon[1], contentCon[2], contentCon[3], contentCon[4], contentCon[5])
                lstConnection.append(vConnection)           

        file1.close()

# Program execution
lstGlyph = []
lstConnection = []
contentGly = []
contentCon = []
lstGlyphIn = []                 #List to store Glyphs Inputs
lstGlyphOut = []                #List to store Glyphs Outputs

# Reading the workflow file
fileRead(lstGlyph)

#Create the inputs and outputs for the glyph
for vConnection in lstConnection:

    #If the glyph has input
    for i, vGlyph in enumerate(lstGlyph):
        if vConnection.input_varname != '\n' and vGlyph.glyph_id == vConnection.input_glyph_id:
            vGlyphIn = objGlyphInput(vConnection.input_varname, False)
            lstGlyph[i].funcGlyphAddIn (vGlyphIn)

    #If the glyph has output   
    for i, vGlyph in enumerate(lstGlyph):
        if vConnection.output_varname != '\n' and vGlyph.glyph_id == vConnection.output_glyph_id:
            vGlyphIn = objGlyphInput(vConnection.output_varname, False)
            lstGlyph[i].funcGlyphAddOut (vGlyphOut)

# Shows the content of the Glyphs
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
#for vConnection in lstConnection:
#    print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
#          "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)