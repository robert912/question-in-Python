import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(enunciado[0] + "\n")
    #las letras de A hasta la D en ASCII es  65 - 69
    for index, alternativa in enumerate(alternativas):
        print(chr(index + 65)+ ". " +alternativa[0])
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4