# wiki-crawler

Crawler de Wikipedia para aprender a trabajar con [Scrapy](https://scrapy.org/)
(y de paso, con [neo4j](https://neo4j.com/))

![Example image](images/graph_readme.png)

## Requisitos

- python 3 3 3 

	- Las librerías adicionales (como *scrapy*) se encuentran en el archivo *requeriments.txt*. 

- [OPCIONAL] neo4j (se puede desactivar en *wiki/settings.py*)

## Instalación

Es recomendable trabajar con un *virtual environment*:

``` sh
virtualenv -p python3 venv;
source venv/bin/activate;
```

Instalación de requisitos:

```
pip install -r requeriments.txt
```


## Ejecución

Para lanzar el crawler, ejecutar desde el directorio base:

```
scrapy crawl spider
```
