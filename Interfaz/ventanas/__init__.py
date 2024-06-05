
from .database import Database

__all__ = ['Database']

# Cualquier inicialización adicional si es necesaria
print("Paquete de base de datos inicializado")

# Interfaz/ventanas/__init__.py
from .Login import Login
from .registrarUsuario import FormularioRegistro
from .cliente import ClienteWindow
from .administrador import AdministradorWindow
from .veterinario import VeterinarioWindow

__all__ = ['Login', 'FormularioRegistro', 'ClienteWindow', 'AdministradorWindow', 'VeterinarioWindow']

# Cualquier inicialización adicional si es necesaria
print("Paquete de ventanas inicializado")
