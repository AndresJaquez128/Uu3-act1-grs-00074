import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]

# Creamos una lista de listas (conformando la tabla)
lista_redes_sociales = [fb,twt,ig,wsp,tel,lkn]

#print(lista_redes_sociales)
# Utilizar pandas  para organizar la tabla (dataframe o maro de datos)
df_redes_sociales = pd.DataFrame(lista_redes_sociales,columns=["Nombre","Cantidad","Es_FB","Año"])
print (df_redes_sociales)
# Creamos el archivo CSV y lo aguardamos
#df_redes_sociales.to_csv("Redesociales.csv",index=False)
#Crea grafica de linea
# Donde x es nombre en el eje horizontal 
# Donde y es cantidad en el eje vertical 
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title("Grafica redes sociales 0074")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.show()
# Grafica de barras 
plt.bar(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])

# Etiquetas y titulo 
plt.title("Redes sociales 0074")
plt.xlabel("Las redes")
plt.ylabel("Cantidad de usuarios")
# Mostrar Grafica
plt.show()

# Ahora ordenar las graficas de barras de manera descendente 
# De la mas grande a la pequeña

df_rs_ordenar = df_redes_sociales.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()
# Coloreando la grafica 
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"])
plt.show()

# Grafica de pastel
# plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels= df_redes_sociales["Nombre"])
plt.show()