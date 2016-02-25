# InvestigacionTracker

Archivos principales:
  gep.py
  reg.py
  regCE.py
  gepCE.py
  
Descripción:
Todos los archivos necesitan un archivo de tipo .csv para funcionar llamado "output.csv" dentro de la carpeta donde se encuentren.
  gep.py: Script de python que permite crear 2 archivos (Nodes[Name].csv, Edges[Name].csv), donde [Name] es uno de los           parámetros de llamada a este script. Toma todos los datos de la base de datos de aplicaciones y documentos del tracker y los   convierte en nodos y aristas para ser usados en Gephi.
    Uso:  
      python gep.py [Name]
        [Name] -> 3 valores distintos ("App", "Doc", "All"(Por defecto)) para filtrar de la base de datos.
        
  reg.py: Script de python capaz de tabular y generar histogramas a partir de los datos de la base de datos de aplicaciones y      documentos del tracker.
    Uso:  
      python reg.py [Name] [Start_date] [End_date] [Scale]
        [Name] -> 3 valores distintos ("App", "Doc", "All"(Por defecto)) para filtrar de la base de datos.
        [Start_date] -> Fecha inicial de filtro para datos. "YYYY-MM-DD" es el único formato válido por ahora. "2016-01-01" por         defecto.
        [End_Date] -> Fecha final de filtro para datos. "YYYY-MM-DD" es el único formato válido por ahora. "2020-01-01" por            defecto.
        [Scale] -> Escala de tiempo para el eje Y del histograma. Medido en segundos. Valor por defecto 3600 (1 hora).
        
  gepCE.py: Script de python que permite crear 2 archivos (NodesCE[argv1].csv, EdgesCE[argv1].csv). Toma todos los datos de la   base de datos de aplicaciones y documentos del tracker que tengan caracteres de tipo web (Ej: "www.", ".com", ".org", etc.)
    Uso:  
      python gep.py [argv1]
        [argv1] -> Argumento usado para nombre de archivo de salida
        
  regCE.py: Script de python capaz de tabular y generar histogramas a partir de los datos de la base de datos de aplicaciones y   documentos del tracker. Filtra para obtener sólo items con caracteres de tipo web (Ej: "www.", ".com", ".org", etc.)
    Uso:  
      python reg.py [Name] [Start_date] [End_date] [Scale]
        [Name] -> 3 valores distintos ("App", "Doc", "All"(Por defecto)) para filtrar de la base de datos.
        [Start_date] -> Fecha inicial de filtro para datos. "YYYY-MM-DD" es el único formato válido por ahora. "2016-01-01" por         defecto.
        [End_Date] -> Fecha final de filtro para datos. "YYYY-MM-DD" es el único formato válido por ahora. "2020-01-01" por            defecto.
        [Scale] -> Escala de tiempo para el eje Y del histograma. Medido en segundos. Valor por defecto 3600 (1 hora).
