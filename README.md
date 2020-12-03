# SQLscan
Una herramienta que utiliza proxies públicos para buscar y escanear sitios en busca de vulnerabilidades de inyección de SQL.<br>

__Usar:__ `python main.py -d product.php?id=`

### Requirements
- Python *v.2.x* **|** *v.3.x*

### Ayuda:
```
usage: main.py [-h] -d DORK [-w]

optional arguments:
  -h, --help            show this help message and exit
  -d DORK, --dork DORK  Dork para buscar ejemplo: product.php?id=
  -w, --write-over      Escribir sobre el archivo de registro existente
```

### Instalar Requirements:
`pip install -r requirements.txt`

### No escriba sobre el archivo de registro existente: 
`python main.py -d product.php?id=`

### Escribir sobre el archivo de registro existente: 
`python main.py -d product.php?id= -w`
