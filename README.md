# Music

Este proyecto genera un sistema de música utlizando nuestras propias playlist,basado en las características de sonido de nuestras canciones.



![Music](https://i.blogs.es/f1970b/nuevo-diseno-inicio-spotify-2/840_560.jpg)

 

## Carpetas
- **INPUT**
	Contiene todos los csv sobre los que se va a trabajar y sobre los que se entrenarán los modelos para hacer las predicciones.
- **OUTPUT**
	Tiene todos los nuevos csv con las predicciones.
- **Src**
	Dentro se encuentran todos recursos necesarios que hya que importar
## Objetivos del proyecto
- **Utilizar la API de spotiy**
  Se utiliza la api de espotify para devolver las canciones de la playlist con sus correspondientes características
- **Análisis y limpieza del dataset**
	Utilizando la base de datos de de kaggle se hace una limpieza de los datos y un análisis exploratorio que determinará la posterior clasificación.
- **Entrenamiento **
  Usando varios algoritmos de ML intentamos clasificar las canciones en base a sus características
- **Recomendación**
  Se crea una función para que basado en nuestro sistema de clsaificación recomiende canciones de nuestro dataset con las mismas características pero en el porcentaje en el que están en nuestra playlist
  

