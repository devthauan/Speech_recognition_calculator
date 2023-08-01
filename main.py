import speech_recognition as sr

def get_audio(microphone):
    # Select and listen to the default microphone
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Say something: ")
        audio = microphone.listen(source)
    return audio

def speach_to_text(microphone, audio):
    # Transforms audio into text
    try:
        phrase = microphone.recognize_google(audio, language='pt-BR') # Change language if needed *(using portuguese)
        return phrase
    except:
        print("Didn't understand.")


def listen_microphone():
    # Get audio and converts to text
    microphone = sr.Recognizer()
    audio = get_audio(microphone)
    texto =  speach_to_text(microphone, audio)
    return texto


def find_operands(text,  operator_simble):
    # Get the position of the operator and get values before and after it
    index_operator = text.index(operator_simble)
    return [text[index_operator - 1] , text[index_operator + 1]]    


def text_to_number(first_operand, second_operand):
    # Transform string operators to int
    try:
        return int(first_operand), int(second_operand)
    except:
        print("Invalid entry!")

def get_transformed_operands(splited_text):
    # Finds and converts operands to integer
    first_operand, second_operand = find_operands(splited_text, splited_text[1])
    first_operand, second_operand = text_to_number(first_operand, second_operand)
    return first_operand, second_operand
        

if __name__ == '__main__':
    text = listen_microphone()
    print("Said phrase: " + text)
    splited_text = text.split(" ") 

    # Simple calculator logic
    if("+" in splited_text):
        first_operand, second_operand = get_transformed_operands(splited_text)
        print(f"Your sum is: {first_operand} + {second_operand} = {first_operand + second_operand}")
    elif("-" in splited_text or "menos" in splited_text):
        first_operand, second_operand = get_transformed_operands(splited_text)
        print(f"Your subtraction is: {first_operand} - {second_operand} =  {first_operand - second_operand}")
    elif("x" in splited_text or "/" in splited_text):
        print("Not supported operations.")

    else:
        print("Invalid entry!")