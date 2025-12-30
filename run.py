import search

casos = [
    ('A', 'B'),                 # Caso 1 (Arad -> Bucharest)
    ('O', 'E'),                 # Caso 2 (Oradea -> Eforie)
    ('G', 'Z'),                 # Caso 3 (Giurgiu -> Zerind)
    ('N', 'D'),                 # Caso 4 (Neamt -> Dobreta)
    ('M', 'F')                  # Caso 5 (Mehadia -> Fagaras)
]


# Definimos los algoritmos a ejecutar
algoritmos = [
    ("Amplitud (BFS)", search.breadth_first_graph_search),
    ("Profundidad (DFS)", search.depth_first_graph_search),
    ("Ramif. y Acotación", search.branch_and_bound_graph_search),
    ("A* (Subestimación)", search.astar_search)
]

print("\n" + "="*80)
print(f"{'EJECUCIÓN DE PRUEBAS - PRÁCTICA DE BÚSQUEDA':^80}")
print("="*80)

for origen, destino in casos:
    print(f"\n>>> PROCESANDO RUTA: {origen} -> {destino}")
    print("-" * 80)
    
    # Creamos el problema una vez para este par origen-destino
    problem = search.GPSProblem(origen, destino, search.romania)
    
    for nombre_alg, func_alg in algoritmos:
        print(f"Algoritmo: {nombre_alg}")
        
        try:
            nodo_final = func_alg(problem)
            
            if nodo_final:
                coste = nodo_final.path_cost
                
                # search.py devuelve el camino desde el Meta hasta el Inicio (inverso),
                ruta_lista = nodo_final.path()
                
                # Convertimos la lista a string directamente
                ruta_str = str(ruta_lista)
                
                print(f"   -> Coste Total: {coste}")
                print(f"   -> Ruta: {ruta_str}")
            else:
                print("   -> SIN SOLUCIÓN")
        
        except Exception as e:
            print(f"   -> ERROR EJECUTANDO: {e}")
            
        print("." * 40)
