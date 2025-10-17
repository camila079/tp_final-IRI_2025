import numpy as np
import matplotlib.pyplot as plt
with open ("pacientes_final.csv", encoding="utf-8") as archivo:
  reader=csv.DIctReader(archivo)
  headers=reader.fieldnames
  
