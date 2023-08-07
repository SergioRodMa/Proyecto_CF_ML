# Data ocupada para el modelo
El archivo que se ocupo para este proyecto es muy grande y puede encontrarse en este [enlace](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
Tambien si se hace un ```git clone``` se puede ocupar el siguiente codido para descomprimir el archivo **Data.zip**

```
import zipfile
zip_file = "data.zip"
# Open the zip file for reading
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    # Extract all the contents to the specified path
    zip_ref.extractall()
```
