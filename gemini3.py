#!/usr/bin/env python3

import os
import sys
import json
import requests
import argparse
from typing import Optional

# --- CAMBIO 1: Define aquí tu API Key de forma definitiva ---
# REEMPLAZA "AIza..." CON TU PROPIA API KEY REAL
HARDCODED_API_KEY = "AIzaSyDxqezPIWswXI3pr4QVHCr84cANEDK847s" 

class GeminiCLI:
    def __init__(self, api_key: str):
        # El API key se pasa ahora correctamente al inicializar la clase
        self.api_key = api_key
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        # Modelo por defecto (Requisito cumplido)
        self.model = "gemini-2.5-pro-preview-03-25"
        
        # Modelos disponibles
        self.available_models = {
            # Gemini 2.5 (Los más avanzados)
            "2.5-flash": "gemini-2.5-flash-preview-04-17",
            "2.5-pro": "gemini-2.5-pro-preview-03-25",
            
            # Gemini 2.0 (Más recientes)
            "2.0-flash": "gemini-2.0-flash",
            "2.0-lite": "gemini-2.0-flash-lite", 
            "2.0-live": "gemini-2.0-flash-live-001",
            
            # Gemini 1.5 (Estables)
            "1.5-flash": "gemini-1.5-flash",
            "1.5-flash-8b": "gemini-1.5-flash-8b",
            "1.5-pro": "gemini-1.5-pro",
            
            # Alias comunes
            "flash": "gemini-2.0-flash",
            "pro": "gemini-2.5-pro-preview-03-25",
            "lite": "gemini-2.0-flash-lite",
        }
    
    def list_models(self):
        """Muestra todos los modelos disponibles"""
        print("🤖 Modelos disponibles:")
        print("\n📍 Gemini 2.5 (Los más avanzados):")
        print("  2.5-flash  - Mejor precio-rendimiento, capacidades equilibradas")
        print("  2.5-pro    - Más poderoso, máxima precisión (thinking model)")
        
        print("\n📍 Gemini 2.0 (Características nuevas):")
        print("  2.0-flash  - Multimodal con características de próxima generación")
        print("  2.0-lite   - Optimizado para costos y baja latencia")
        print("  2.0-live   - Para interacciones en tiempo real")
        
        print("\n📍 Gemini 1.5 (Estables y confiables):")
        print("  1.5-flash  - Rápido y versátil")
        print("  1.5-flash-8b - Modelo pequeño, menor complejidad")
        print("  1.5-pro    - Tamaño medio, amplio rango de tareas")
        
        print("\n📍 Alias rápidos:")
        print("  flash, pro, lite")
        
        print(f"\n🎯 Modelo actual por defecto: {self.model}")

    def send_message(self, message: str, model: Optional[str] = None) -> str:
        """Envía un mensaje a Gemini y retorna la respuesta"""
        model_name = model or self.model
        
        if model_name in self.available_models:
            model_name = self.available_models[model_name]
        
        url = f"{self.base_url}/{model_name}:generateContent"
        headers = {'Content-Type': 'application/json'}
        data = {"contents": [{"parts": [{"text": message}]}]}
        params = {'key': self.api_key}
        
        try:
            response = requests.post(url, headers=headers, json=data, params=params)
            response.raise_for_status()
            
            result = response.json()
            # Limpiamos la respuesta para evitar Markdown o espacios extra
            return result['candidates'][0]['content']['parts'][0]['text'].strip()
            
        except requests.exceptions.HTTPError as e:
            # Intentar decodificar el error de la API de Google
            error_details = e.response.json()
            error_message = error_details.get('error', {}).get('message', str(e))
            return f"Error en la API de Gemini: {error_message}"
        except requests.exceptions.RequestException as e:
            return f"Error en la petición: {e}"
        except (KeyError, IndexError) as e:
            return f"Error procesando respuesta (posiblemente no hay contenido): {response.text}"
        except Exception as e:
            return f"Error inesperado: {e}"

def main():
    parser = argparse.ArgumentParser(description='CLI para interactuar con Gemini')
    
    # Argumentos para los diferentes modos de operación
    group = parser.add_mutually_exclusive_group()
    group.add_argument('message', nargs='?', default=None, help='Mensaje para enviar a Gemini en modo simple.')
    group.add_argument('-i', '--interactive', action='store_true', help='Iniciar modo interactivo.')
    
    # --- CAMBIO 2: Nuevos argumentos para el modo test ---
    group.add_argument('-t', '--test', help='Pregunta para el modo test de opción múltiple.')
    parser.add_argument('-a', help='Opción A para el modo test.')
    parser.add_argument('-b', help='Opción B para el modo test.')
    parser.add_argument('-c', help='Opción C para el modo test.')
    parser.add_argument('-d', help='Opción D para el modo test.')
    parser.add_argument('-e', help='Opción E para el modo test.')
    
    # Argumentos de configuración
    parser.add_argument('-k', '--key', help='Tu API Key de Gemini (opcional, sobreescribe la hardcodeada).')
    parser.add_argument('-m', '--model', default='2.5-pro', help='Modelo a usar (por defecto: 2.5-pro).')
    parser.add_argument('--list', action='store_true', help='Listar modelos disponibles.')
    
    args = parser.parse_args()
    
    # --- CAMBIO 1 (Lógica): Usa la clave de -k, la variable de entorno o la hardcodeada ---
    api_key = args.key or os.getenv('GEMINI_API_KEY') or HARDCODED_API_KEY
    #if "AIzaSy" in api_key: # Chequeo simple para ver si es la clave de ejemplo
        #print("ADVERTENCIA: Estás usando una API Key de ejemplo. Edita el script para poner tu clave real.", file=sys.stderr)
    
    cli = GeminiCLI(api_key)
    
    if args.list:
        cli.list_models()
        return

    # --- CAMBIO 2 (Lógica): Modo Test ---
    if args.test:
        options = {}
        if args.a: options['A'] = args.a
        if args.b: options['B'] = args.b
        if args.c: options['C'] = args.c
        if args.d: options['D'] = args.d
        if args.e: options['E'] = args.e

        if len(options) < 2:
            print("Error: El modo test requiere al menos dos opciones (-a, -b, etc.).", file=sys.stderr)
            sys.exit(1)

        prompt_lines = [
            "Tarea: Responde a la siguiente pregunta de opción múltiple.",
            "Tu respuesta debe ser ÚNICAMENTE la letra de la opción correcta (ej: A, B, C), sin puntos, explicaciones ni texto adicional.",
            "\n---",
            f"Pregunta: {args.test}",
            "\nOpciones:"
        ]
        for letter, text in options.items():
            prompt_lines.append(f"{letter}. {text}")
        
        final_prompt = "\n".join(prompt_lines)
        
        response = cli.send_message(final_prompt, args.model)
        print(response)
        return

    # --- Lógica existente y corregida ---
    if args.interactive:
        current_model = args.model
        print(f"🤖 Modo interactivo de Gemini CLI")
        # BUG CORREGIDO: Usar current_model que ya está definido
        print(f"🧠 Usando: {current_model} (puedes cambiarlo con /model)")
        print("Comandos especiales:")
        print("  /model <nombre> - Cambiar modelo")
        print("  /list          - Ver modelos disponibles") 
        print("  /quit o /exit  - Salir")
        print("-" * 50)
        
        while True:
            try:
                message = input("🗣️  Tú: ").strip()
                if message.lower() in ['quit', 'exit', 'salir', '/quit', '/exit']:
                    print("¡Hasta luego! 👋")
                    break
                
                if message.startswith('/model '):
                    new_model = message.split(' ', 1)[1].strip()
                    if new_model in cli.available_models or new_model.startswith('gemini-'):
                        current_model = new_model
                        print(f"✅ Modelo cambiado a: {current_model}")
                    else:
                        print("❌ Modelo no válido. Usa /list para ver opciones.")
                    continue
                
                if message == '/list':
                    cli.list_models()
                    continue
                
                if not message:
                    continue
                
                print("🤖 Gemini:", end=" ", flush=True)
                response = cli.send_message(message, current_model)
                print(response)
                print("-" * 50)
                
            except (KeyboardInterrupt, EOFError):
                print("\n¡Hasta luego! 👋")
                break
    
    elif args.message:
        response = cli.send_message(args.message, args.model)
        print(response)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
