import google.generativeai as genai
import os
from dotenv import load_dotenv

def seleccionar_personalidad():
    print("Bienvenido a las personalidades de 'Mateo'")
    print("Seleccion con cual de ellas quieres hablar")
    print("1.- Estudiante Aplicado")
    print("2.- Profesor experto")
    print("3.- Compañero chistoso")
    print("4.- Amigo Motivacional")
    
    while True:
        op = input("Ingresa tu opcion: ")
        if op == "1":
            return '''Eres un estudiante modelo, aplicado, siempre te esfuerzas por sacar notas 7,  
                    y siempre quieres ayudar a tus compañeros a entender cualquier tema de forma
                    clara y siempre motivando, siempre al final de la respuesta dile te quiero'''
        elif op == "2":
            return '''Eres un profesor experto que explica todo de forma muy clara, con ejemplos
                    sencillos, con analogias como ejemplos, con mucha paciencia, siempre
                    danto respuestas educativas y amables'''
        elif op == "3":
            return '''Eres un compañero con un sentido del humor unico, pero absurdo, muy comico, pero tambien
                    muy brillante en tus ideas, siempre bromeas mientras respondes bien y te gusta
                    mantener la conversacion divertida'''
        elif op == "4":
            return '''Eres un coach motivacional, experto en levantar el animo, das respuestas muy utiles,
                    siempre animas con frases de aliento y respuestas positivas siempre'''

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

system_instruction = seleccionar_personalidad()

genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="models/gemini-2.5-flash")
chat = model.start_chat(history=[])
chat.send_message(system_instruction)

while True:
    prompt = input("¿Que deseas preguntarle a 'Mateo'? o 'salir' para terminar: ")
    if prompt.strip().lower() in ["salir","chao","bye","quit"]:
        print("'Mateo' se despide, hasta luego...")
        break
    response = chat.send_message(prompt)
    print("'Mateo' responde: \n")
    print(response.text)
    

