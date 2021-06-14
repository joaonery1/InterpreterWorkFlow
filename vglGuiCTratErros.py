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
        self.lst_par = []                       #parameter list
        self.lst_input = []                     #glyph input list
        self.lst_output = []                    #glyph output list

    #Add glyph parameter function
    def funcGlyphAddPar (self, vGlyphPar):
        self.lst_par.append(vGlyphPar)

    #Add glyph input function
    def funcGlyphAddIn (self, vGlyphIn):
        self.lst_input.append(vGlyphIn)

    #Add glyph output function 
    def funcGlyphAddOut (self, vGlyphOut):
        self.lst_output.append(vGlyphOut)

    #Function to update if the glyph is ready and return status
    #When all glyph entries are READY=TRUE, the glyph changes status to READY=TRUE
    def getGlyphReady(self):
        return self.ready

    #Assign ready to glyph
    def setGlyphReady(self, status):

        vGlyphReady = status

        #Identifies if all glyph entries were used
        if vGlyphReady == True and len(self.lst_input) > 0:
            
            #If there is an entry without using
            for vGlyphIn in self.lst_input:            
                if vGlyphIn.getStatus() == False:
                    vGlyphReady = False
                    self.ready = False
                    exit    
    
            #If all inputs were used
            if vGlyphReady:
                self.ready = vGlyphReady

        #self.ready = status

    #Assign done to glyph
    def setGlyphDone(self, status):
        self.done = status

    #Return Done status
    def getGlyphDone(self):
        return self.done

    #Assign ready to glyph inputs
    def setGlyphInputAll(self, status):
        for i, vGlyphIn in enumerate(self.lst_input):
           self.lst_input[i].setGlyphInput(vGlyphIn, status)

    #Assign ready to glyph outputs
    def setGlyphOutputAll(self, status):
        for i, vGlyphOut in enumerate(self.lst_output):
           self.lst_output[i].setGlyphOutput(vGlyphOut, status)
    
    def getGlypX(self):
        return self.glyph_x

# Structure for storing Parameters in memory
class objGlyphParameters(object):

    def __init__(self, namepar, valuepar):
        self.name = namepar      #variable name
        self.value = valuepar    #variable value

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

# Structure for storing Glyphs input list in memory
class objGlyphInput(object):

    def __init__(self, namein, statusin):
        self.namein = namein         #glyph input name
        self.statusin = statusin     #glyph input status

    def getStatus(self):
        return self.statusin

    #Assign status to glyph output
    def setGlyphInput(self, status):
        self.statusin = status


# Structure for storing Glyphs output list in memory
class objGlyphOutput(object):

    def __init__(self, nameout, statusout):
        self.nameout = nameout      #glyph output name
        self.statusout = statusout  #glyph output status

    #Assign status to glyph output
    def setGlyphOutput(self, status):
        self.statusout = status

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
        self.ready = False     
 #False = unread or unexecuted image; True = image read or executed

class Error (Exception): #classe para tratar uma execeção definida pelo usuário
    pass
    '''
        FALTA OS AJUSTES PARA SAÍDA DA CLASSE, POREM SÓ COM A FUNÇÃO 'raise' JÁ FUNCIONA
    '''
# File to be read
vfile = 'arquivoteste.wk'

lstGlyph = []                   #List to store Glyphs
lstGlyphPar = []                #List to store Glyphs Parameters
lstConnection = []              #List to store Connections
lstGlyphIn = []                 #List to store Glyphs Inputs
lstGlyphOut = []                #List to store Glyphs Outputs
lst_sizes = []
vGlyph = objGlyph               #Glyph in memory 
vGlyphPar = objGlyphParameters  #Glyph parameters in memory
vGlyphIn = objGlyphInput        #Glyph input in memory
vGlyphOut = objGlyphOutput      #Glyph output in memory
vConnection = objConnection     #Connection in memory

# Method for reading the workflow file
def fileRead(lstGlyph):
    try:
        if os.path.isfile(vfile):
            count = 0 #declaração do contador de linhas

            # Opens the workflow file
            file1 = open(vfile,"r")
            for line in file1:
                count +=1   #varaiavel contador
            
                # Creates the glyphs of the workflow file
                if 'glyph:' in line.lower():
                    try:
                        contentGly = line.split(':')     #extracts the contents of the workflow file line in a list separated by the information between the ":" character
                        contentGlyPar = []               #clears the glyph parameter list
                        lstParAux = []                   #auxiliary parameter list
                        
                        #Create the Glyph
                        vGlyph = objGlyph(contentGly[1], contentGly[2], contentGly[4], contentGly[5], contentGly[6], contentGly[7])
                    except IndexError as d: #rule 2
                        #caso falte alguma informção de contentGly 
                        print("Falta parametros a serem declarados na linha do Glyph","\nLinha",{count}, "{d}")
                    except ValueError as s: #rule 4
                        print("Falta parametros a serem declarados na linha do Glyph","\nLinha",{count} , "{s}")
                    
                    #Caso ultrapasse os limites, ainda falta definir os limites
                    try:
                        if (int(contentGly[6]) or int(contentGly[7])) > 100000 or (int(contentGly[6]) or int(contentGly[7])) < 0:
                            raise Error("Ultrapassou o limite das dimensões", "Verifique a linha: ",{count}) #rule 4
                    except ValueError: #rule 4
                        print("Valores para as coordenadas estão errados." , " Verificar a linha: ",{count})
                
                    



                ##ARAMAZENAR E TRATAR ALTURA E LARGURA , PROVAVELMENTE SERIA A TELA.
                       ###width_size = 2342
                       ###height_size = 1144 
                    
                    

                            
                    # lst_sizes.append(contentGly[5])
                    # lst_sizes.append(contentGly[6])

 
                    #Image type parameter
                    try:
                        if 'image' in contentGly[9]:
                            contentGly[9] = contentGly[9].replace('image', '-image')
                            contentGly[9] = contentGly[9] + ' \'' + contentGly[10].replace('\n','')
                    except IndexError: #rule 2
                        print("Erro nos parametros do Glyph.", "Verifique a linha ", {count})
                        
                    # #Identifies the parameters
                    # #:: -[var_str] '[var_str_value]' -[var_num] [var_num_value]
                    # contentGlyPar = contentGly[9].split(' ')

                    for vpar in contentGlyPar:
                        if vpar != '' and vpar != '\n':

                            vGlyphPar = objGlyphParameters  

                            #Differentiates parameter name and value
                            if vpar[0] == '\'' or vpar.isdigit():
                                vGlyphPar = objGlyphParameters('Value', vpar.replace("'", '')) 

                            if vpar[0] == "-":             
                                if vpar[1].isdigit():
                                    vGlyphPar = objGlyphParameters('Value', vpar.replace("-", ''))
                                else:
                                    vGlyphPar = objGlyphParameters('Name', vpar.replace('-', ''))

                            #Temporary list to differentiate parameters and their values
                            lstParAux.append(vGlyphPar)

                    #Creates the parameters of the Glyph
                    for i, vParAux in enumerate(lstParAux):
                        
                        vParType = vParAux.getName()
                        vParValue = vParAux.getValue()
                        
                        vParTypeNext = ''
                        vParValueNext = ''

                        #If you don't have the next parameter to include
                        if i < (len(lstParAux)-1):
                            vParTypeNext = lstParAux[i+1].getName()
                            vParValueNext = lstParAux[i+1].getValue()
                        
                        ###vParAuxNext = objGlyphParameters(lstParAux[i+1].getName(), lstParAux[i+1].getValue())

                        #A parameter name followed by another parameter name
                        #Write the parameter because it will have no value
                        #Example: -wh -hw -dd
                        if vParType == 'Name' and (vParTypeNext == 'Name' or (vParTypeNext == '' and vParType != 'Value')):
                            vGlyphPar = objGlyphParameters(vParValue, '')
                            vGlyph.funcGlyphAddPar(vGlyphPar)

                        #A parameter name followed by a value
                        #Write the parameter with its value
                        #Example: -conn 1
                        if vParType == 'Name' and vParTypeNext == 'Value':
                            vGlyphPar = objGlyphParameters(vParValue, vParValueNext)
                            vGlyph.funcGlyphAddPar(vGlyphPar)

                            # Examples:
                            # -wh -hw -dd 
                            # -conn 1 
                            # -wh -hw -dd
                            # -ms 0 -mc 0 -mi 0 -mr 0 -col 0 
                            # -append 1 -mapping 0 -e
                            # -real 'width_size'
                            # -backvalue 0 -masklogic 1
                            # -conn 1  
                            # -real '100'                                                   

                    lstGlyph.append(vGlyph)

                #Creates the connections of the workflow file
                #NodeConnection:data:[output_Glyph_ID]:[output_varname]:[input_Glyph_ID]:[input_varname]        
                if 'nodeconnection:' in line.lower():
                    try:
                        contentCon = line.split(':')
                        vConnection = objConnection(contentCon[1], contentCon[2], contentCon[3], contentCon[4], contentCon[5])
                        lstConnection.append(vConnection)
                    except IndexError as f: #rule 2
                        print("Falta indices nas conexões",{f},"na linha",{count},"do arquivo")

                    ##tratar conexões node connection contentcon[2] e contentcon[4]
                    try: #rule 8
                        if int(contentCon[2])  <0 or int(contentCon[4]) < 0:
                            raise Error("Conexões erradas, por favor verifique a linha: ",{count})
                    except ValueError:
                        print("Valores para as coordenadas estão errados." , " Verificar a linha: ",{count})
                    
                
    finally: #rule 5
        #print("ARQUIVO LIDO")
        file1.close()

# Program execution
lstGlyph = []
lstConnection = []
contentGly = []
contentCon = []
lstGlyphIn = []                 #List to store Glyphs Inputs
lstGlyphOut = []                #List to store Glyphs Outputs

# Reading the workflow file and loads into memory all glyphs and connections
try:
    fileRead(lstGlyph)
except UnboundLocalError: #rule 1
    print("Arquivo não encontrado.")

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

#Update the status of glyph entries
for vGlyph in lstGlyph:

    if vGlyph.getGlyphReady() and vGlyph.getGlyphDone() == False:

        #Glyph execute
        # xxxxxxxxx

        #Sets all glyph outputs as executed 
        vGlyph.setGlyphOutputAll(True)

        #Sets all glyph outputs as executed
        vGlyph.setGlyphInputAll(True)

        #Defines that the glyph was executed
        vGlyph.setGlyphDone(True)


# Shows the content of the Glyphs
for vGlyph in lstGlyph:
    print("Library:", vGlyph.library, "Function:", vGlyph.func, "Localhost:", vGlyph.localhost, "Glyph_Id:", vGlyph.glyph_id, 
          "Position_Line:", vGlyph.glyph_x, "Position_Column:", vGlyph.glyph_y)#, "Parameters:", vGlyph.lst_par)
#
#    #Shows the list of glyph inputs
#    for vGlyphIn in vGlyph.lst_input:
#        print("Glyph_Id:", vGlyph.glyph_id, "Glyph_In:", vGlyphIn)
#
#    #Shows the list of glyph outputs
#    for vGlyphOut in vGlyph.lst_output:
#        print("Glyph_Id:", vGlyph.glyph_id, "Glyph_Out:", vGlyphOut)

# Shows the content of the Connections
for vConnection in lstConnection:
    print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
          "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)
##teste