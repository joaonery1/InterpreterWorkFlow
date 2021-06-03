from copyGuiWk import lstConnection,lstGlyph


# Shows the content of the Connections
for vConnection in lstConnection:
    print("Conexão:", vConnection.type, "Glyph_Output_Id:", vConnection.output_glyph_id, "Glyph_Output_Varname:", vConnection.output_varname,
          "Glyph_Input_Id:", vConnection.input_glyph_id, "Glyph_Input_Varname:", vConnection.input_varname)

#print(lstConnection)


