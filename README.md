# Estrategia-de-busqueda

# Búsqueda en Espacio de Estados (FSI)
Este proyecto implementa y compara diferentes estrategias de búsqueda en el espacio de estados para resolver el problema del viajante en el mapa de Rumanía
## Modificaciones e Implementación

Para cumplir con los requisitos de la práctica, se han realizado las siguientes modificaciones sobre el código base:

### Nuevas Estrategias de Búsqueda (`search.py`)
Se han implementado dos nuevas funciones respetando la interfaz original:

* **`branch_and_bound_graph_search(problem)`**: 
    * Utiliza una `PriorityQueue` ordenando los nodos exclusivamente por su coste acumulado (`g(n)`).
    * Garantiza encontrar la solución óptima en coste.
* **`astar_search(problem)`**: 
    * Implementa A* ordenando la cola de prioridad mediante la función de evaluación $f(n) = g(n) + h(n)$.
    * La heurística $h(n)$ utilizada es la distancia en línea recta (euclídea) entre ciudades.

### Gestión de Empates en la Cola de Prioridad
La librería estándar `heapq` de Python (usada por `PriorityQueue`) requiere que los elementos sean comparables. Se modificó la clase `Node` añadiendo el método `__lt__`:

```python
def __lt__(self, other):
    return self.state < other.state
