#**DOMINANDO LA PUESTA EN PRODUCCION**
---

Empecemos identificando la creacion  de directorios. Con el comando django.
Primero crearemos un entorno virtual.

1. Estoy creando el environment: C:\Users\soporte\Documents\TEST_HEROKU_10032025>python -m venv h_money_env
2. Actvivamos en windows: h_money_env\Scripts\activate
3. pip install django
4. django-admin startproject Paz_proyecto
5. Esto crea la carpeta PAZ_proyecto y dentro tenemos 
6. Lo que puedo indicar es que el repositorio deberia estar en la carpeta Paz_proyecto, esto quiere decir que el git clone nombre_repositorio, deberia descargar la carpeta y al ingresar a la carpeta clonada nombre del proyecto, usar o acceder directamente al contenido del proyecto, aplicacion o manage.py.

```
Paz_proyecto/
    manage.py
    Paz_proyecto/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

7. Paso 7 seria ir a github y crear el repositorio.
![alt text](image.png)


8. Comando para entrar al directorio, si estamos en windows sugiero hacerlo con la aplicacion git bash.

```
$ cd PAZ_proyecto
$ git init
$ git status
$ git add *
$ git commit -m "update"
$ git remote add origin git@github.com:sebastianVP/PAZ_proyecto.git
$ git push -u origin master
```

9. Aqui solo una pausa, la cuenta de mi consola en windows es avaldezp22 lo cual esta asociado a mi correo igp.gob.pe, por este motivo **tengo que invitar al proyecto como colaborar**, la cuenta de github esta asociada al correo sebastianVP.