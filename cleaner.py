class CleanUtil:

    #Removes leading / from Dropdowns and RadioButtons and CheckBoxes using the 
    #FieldType
    @staticmethod
    def sanitize(input_string, fieldType):
        output_string = ''
        if input_string is None:
            input_string= ""
        if '/Ch' in fieldType or '/Btn' in fieldType:
            for i in input_string:
                if i == '/':
                    outchar = ''
                elif i == '<':
                    outchar = ''
                else:
                    outchar = i
                output_string += outchar
        else:
            output_string = input_string
        #simple country replacement
        if input_string == "United States of America (USA)":
            output_string ="USA"
        return str(output_string)