#Esse programa deve ser executado no PyCharm
import speech_recognition as sr

def obter_audio(microfone):
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    return audio

def transformar_audio_em_texto(microfone, audio):
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        return frase
    except:
        print("Não entendi")


def escutar_microfone():
    microfone = sr.Recognizer()
    audio = obter_audio(microfone)
    texto =  transformar_audio_em_texto(microfone, audio)
    return texto


def find_operands(text, operator_text = "divida", operator_simble = "/"):
    try:
        index_operator = text.index(operator_simble)
    except:
        index_operator = text.index(operator_text)
    return [text[index_operator - 1] , text[index_operator + 1]]



number_dictionary = {"um":1, "dois":2,"três":3, "quatro":4, "cinco":5, "seis":6, "sete":7, "oito":8, "nove":9}

def text_to_number(first_operand, second_operand):
    # Transform text to numbers if needed
    try:
        first_operand = int(number_dictionary[first_operand])
        second_operand = int(number_dictionary[second_operand])
    except:
        pass
    # Transform string to int
    try:
        return int(first_operand), int(second_operand)
    except:
        print("A entrada dos dados não é válida para o algoritmo")

if __name__ == '__main__':
    texto = escutar_microfone()
    print("A frase que você disse foi: " + texto)
    split_texto = texto.split(" ")   
    if("+" in split_texto or "mais" in split_texto):
        first_operand, second_operand = find_operands(split_texto, "+", "mais")
        first_operand, second_operand = text_to_number(first_operand, second_operand)
        print(f"Sua soma é: {first_operand} + {second_operand} = {first_operand + second_operand}")
    elif("-" in split_texto or "menos" in split_texto):
        first_operand, second_operand = find_operands(split_texto, "-", "menos")
        first_operand, second_operand = text_to_number(first_operand, second_operand)
        print(f"Sua subtração é: {first_operand} - {second_operand} =  {first_operand - second_operand}")
    elif("x" in split_texto or "vezes" in split_texto):
        print("O algoritmo trata apenas as operações de Adição e Subtração")
        #first_operand, second_operand = find_operands(split_texto, "x", "vezes")
        #first_operand, second_operand = text_to_number(first_operand, second_operand)
        #print(f"Sua multiplicação é: {first_operand} * {second_operand} =  {first_operand * second_operand}")
    else:
        print("A entrada dos dados não é válida para o algoritmo")


# =============================================================================
# Saídas
# =============================================================================
# =============================== #1# ========================================#
# Diga alguma coisa: 
# A frase que você disse foi: 1 + 2
# Sua soma é: 1 + 2 = 3
# =============================== #2# ========================================#
# Diga alguma coisa: 
# A frase que você disse foi: 3 - 2
# Sua subtração é: 3 - 2 =  1
# =============================== #3# ========================================#
# Diga alguma coisa: 
# A frase que você disse foi: três vezes dois
# O algoritmo trata apenas as operações de Adição e Subtração
# =============================== #4# ========================================#
# Diga alguma coisa: 
# A frase que você disse foi: isso é um teste
# A entrada dos dados não é válida para o algoritmo