#!/usr/bin/env python3

import os
import sys
import json
import requests
import argparse
from typing import Optional

class GeminiCLI:
    def __init__(self, api_key: str):
        self.api_key = "AIzaSyDxqezPIWswXI3pr4QVHCr84cANEDK847s"
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        self.model = "gemini-2.5-pro-preview-03-25"  # Gemini 2.5 Pro por defecto
        
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
        
        print(f"\n🎯 Modelo actual: {self.model}")

    def send_message(self, message: str, model: Optional[str] = None) -> str:
        """Envía un mensaje a Gemini y retorna la respuesta"""
        model_name = model or self.model
        
        # Resolver alias de modelo
        if model_name in self.available_models:
            model_name = self.available_models[model_name]
        
        url = f"{self.base_url}/{model_name}:generateContent"
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": message
                        }
                    ]
                }
            ]
        }
        
        params = {'key': self.api_key}
        
        try:
            response = requests.post(url, headers=headers, json=data, params=params)
            response.raise_for_status()
            
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
            
        except requests.exceptions.RequestException as e:
            return f"Error en la petición: {e}"
        except KeyError as e:
            return f"Error procesando respuesta: {e}"
        except Exception as e:
            return f"Error inesperado: {e}"

def main():
    parser = argparse.ArgumentParser(description='CLI para interactuar con Gemini')
    parser.add_argument('message', nargs='?', help='Mensaje para enviar a Gemini')
    parser.add_argument('-k', '--key', help='API Key de Gemini')
    parser.add_argument('-m', '--model', default='2.5-pro', help='Modelo a usar (por defecto: 2.5-pro)')
    parser.add_argument('-i', '--interactive', action='store_true', help='Modo interactivo')
    parser.add_argument('--list', action='store_true', help='Listar modelos disponibles')
    
    args = parser.parse_args()
    
    # Obtener API key
    api_key = args.key or os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: No se encontró API key.")
        print("Úsala con -k tu_api_key o establece la variable GEMINI_API_KEY")
        sys.exit(1)
    
    cli = GeminiCLI(api_key)
    
    if args.list:
        cli.list_models()
        return
    
    if args.interactive:
        print(f"🤖 Modo interactivo de Gemini CLI")
        print(f"🧠 Usando: {current_model} (el más potente)")
        print("Comandos especiales:")
        print("  /model <nombre> - Cambiar modelo")
        print("  /list          - Ver modelos disponibles") 
        print("  /quit o /exit  - Salir")
        print("-" * 50)
        
        current_model = args.model
        
        while True:
            try:
                message = input("🗣️  Tú: ").strip()
                if message.lower() in ['quit', 'exit', 'salir', '/quit', '/exit']:
                    print("¡Hasta luego! 👋")
                    break
                
                if message.startswith('/model '):
                    new_model = message[7:].strip()
                    if new_model in cli.available_models or new_model.startswith('gemini-'):
                        current_model = new_model
                        print(f"✅ Modelo cambiado a: {new_model}")
                    else:
                        print("❌ Modelo no válido. Usa /list para ver opciones.")
                    continue
                
                if message == '/list':
                    cli.list_models()
                    continue
                
                if not message:
                    continue
                
                print("🤖 Gemini:", end=" ")
                response = cli.send_message(message, current_model)
                print(response)
                print("-" * 50)
                
            except KeyboardInterrupt:
                print("\n¡Hasta luego! 👋")
                break
            except EOFError:
                break
    
    elif args.message:
        response = cli.send_message(args.message, args.model)
        print(response)
    
    else:
        print("Error: Proporciona un mensaje o usa el modo interactivo (-i)")
        parser.print_help()

if __name__ == "__main__":
    main()
