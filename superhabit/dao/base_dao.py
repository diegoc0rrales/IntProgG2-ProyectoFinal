import json
import os
from typing import List, Dict, Any, Optional

class BaseDAO:
    """Clase base para el manejo de datos usando archivos JSON"""
    
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.datos = self._cargar_datos()
        self._siguiente_id = self._obtener_siguiente_id()
    
    def _cargar_datos(self) -> List[Dict[str, Any]]:
        """Carga los datos desde el archivo JSON"""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def _guardar_datos(self):
        """Guarda los datos en el archivo JSON"""
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.datos, f, indent=2, ensure_ascii=False)
    
    def _obtener_siguiente_id(self) -> int:
        """Obtiene el siguiente ID disponible"""
        if not self.datos:
            return 1
        return max(item.get('id', 0) for item in self.datos) + 1
    
    def _generar_id(self) -> int:
        """Genera un nuevo ID único"""
        nuevo_id = self._siguiente_id
        self._siguiente_id += 1
        return nuevo_id
    
    def obtener_todos(self) -> List[Dict[str, Any]]:
        """Obtiene todos los elementos"""
        return self.datos.copy()
    
    def obtener_por_id(self, id_elemento: int) -> Optional[Dict[str, Any]]:
        """Obtiene un elemento por su ID"""
        for item in self.datos:
            if item.get('id') == id_elemento:
                return item.copy()
        return None
    
    def crear(self, elemento: Dict[str, Any]) -> Dict[str, Any]:
        """Crea un nuevo elemento"""
        elemento['id'] = self._generar_id()
        self.datos.append(elemento)
        self._guardar_datos()
        return elemento.copy()
    
    def actualizar(self, id_elemento: int, elemento: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Actualiza un elemento existente"""
        for i, item in enumerate(self.datos):
            if item.get('id') == id_elemento:
                elemento['id'] = id_elemento
                self.datos[i] = elemento
                self._guardar_datos()
                return elemento.copy()
        return None
    
    def eliminar(self, id_elemento: int) -> bool:
        """Elimina un elemento por su ID"""
        for i, item in enumerate(self.datos):
            if item.get('id') == id_elemento:
                del self.datos[i]
                self._guardar_datos()
                return True
        return False

