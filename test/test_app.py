import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import agregar_tarea

def test_agregar_tarea():
    resultado = agregar_tarea("Estudiar Python")
    assert "Estudiar Python" in resultado