#!/usr/bin/env python3
"""
Herramienta simple para gestión de certificados
Simple certificate management tool
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def listar_certificados():
    """Lista todos los certificados en el directorio actual"""
    print("📜 Certificados encontrados:")
    print("-" * 50)
    
    certificados = []
    extensiones_validas = {'.pdf', '.jpg', '.jpeg', '.png', '.doc', '.docx'}
    
    for archivo in Path('.').iterdir():
        if archivo.is_file() and archivo.suffix.lower() in extensiones_validas:
            # Excluir archivos de sistema/documentación
            if archivo.name not in ['README.md', 'inventario.md']:
                tamaño = archivo.stat().st_size
                tamaño_mb = tamaño / (1024 * 1024)
                
                print(f"📄 {archivo.name}")
                print(f"   Tamaño: {tamaño_mb:.2f} MB ({tamaño:,} bytes)")
                print(f"   Tipo: {archivo.suffix.upper()}")
                print()
                
                certificados.append(archivo.name)
    
    print(f"Total: {len(certificados)} certificado(s)")
    return certificados

def verificar_estructura():
    """Verifica si existe una estructura de directorios recomendada"""
    print("🗂️  Verificando estructura de directorios:")
    print("-" * 50)
    
    directorios_recomendados = [
        'certificados/profesionales',
        'certificados/academicos', 
        'certificados/tecnicos',
        'docs',
        'herramientas'
    ]
    
    estructura_ok = True
    
    for directorio in directorios_recomendados:
        if Path(directorio).exists():
            print(f"✅ {directorio}")
        else:
            print(f"❌ {directorio} (no existe)")
            estructura_ok = False
    
    if not estructura_ok:
        print("\n💡 Sugerencia: Ejecuta 'crear_estructura()' para crear los directorios")
    
    return estructura_ok

def crear_estructura():
    """Crea la estructura de directorios recomendada"""
    print("🏗️  Creando estructura de directorios:")
    print("-" * 50)
    
    directorios = [
        'certificados/profesionales',
        'certificados/academicos',
        'certificados/tecnicos', 
        'certificados/otros',
        'docs',
        'herramientas',
        'respaldos'
    ]
    
    for directorio in directorios:
        Path(directorio).mkdir(parents=True, exist_ok=True)
        print(f"📁 Creado: {directorio}")
    
    # Crear archivo .gitkeep en directorios vacíos
    for directorio in directorios:
        gitkeep = Path(directorio) / '.gitkeep'
        if not gitkeep.exists():
            gitkeep.touch()
    
    print("\n✅ Estructura creada exitosamente!")

def mostrar_ayuda():
    """Muestra las opciones disponibles"""
    print("🔧 Herramienta de Gestión de Certificados")
    print("=" * 50)
    print()
    print("Comandos disponibles:")
    print("  listar      - Lista todos los certificados")
    print("  verificar   - Verifica la estructura de directorios")
    print("  crear       - Crea la estructura recomendada")
    print("  ayuda       - Muestra esta ayuda")
    print()
    print("Ejemplo de uso:")
    print("  python herramientas.py listar")
    print("  python herramientas.py crear")

def main():
    """Función principal"""
    if len(sys.argv) < 2:
        mostrar_ayuda()
        return
    
    comando = sys.argv[1].lower()
    
    if comando == 'listar':
        listar_certificados()
    elif comando == 'verificar':
        verificar_estructura()
    elif comando == 'crear':
        crear_estructura()
    elif comando == 'ayuda' or comando == 'help':
        mostrar_ayuda()
    else:
        print(f"❌ Comando desconocido: {comando}")
        print("Usa 'python herramientas.py ayuda' para ver los comandos disponibles")

if __name__ == "__main__":
    main()