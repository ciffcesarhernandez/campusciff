# repositorio campusciff creado en GitHub:

![Data Science Toolkit 1](/img/1.png)


# campusciff
Repositorio Entrega de Ejercicios

# Realizo la configuración inicial
Sara Otero@SARA MINGW64 ~ (master)
$ git config --global user.name "César"

Sara Otero@SARA MINGW64 ~ (master)
$ git config --global user.email "cesarhernandez@campusciff.net"

# Creo el directorio 20151130, me sitúo en él e inicio git
Sara Otero@SARA MINGW64 ~ (master)
$ mkdir 20151130

Sara Otero@SARA MINGW64 ~ (master)
$ cd 20151130/

Sara Otero@SARA MINGW64 ~/20151130 (master)
$ git init
Initialized empty Git repository in C:/Users/Sara Otero/20151130/.git/

# Realizo el clonado del repositorio campusciff en mi repositorio local
Sara Otero@SARA MINGW64 ~/20151130 (master)
$ git clone git@github.com:ciffcesarhernandez/campusciff.git
Cloning into 'campusciff'...
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
Checking connectivity... done.

# Clonado realizado
![Data Science Toolkit 2](/img/2.png)

# Me sitúo en el repositorio creado campusciff, 
# Añado el archivo README.md, realizo el commit y el push
Sara Otero@SARA MINGW64 ~/20151130 (master)
$ cd campusciff

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git add README.md

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git commit -m "commit inicial"
[master 37b42c3] commit inicial
 1 file changed, 29 insertions(+)

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git push origin master
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 706 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@github.com:ciffcesarhernandez/campusciff.git
   82cfde1..37b42c3  master -> master

# Creo archivo de texto privado.txt con texto privado
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ echo privado > privado.txt


# Creo carpeta privada
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ mkdir privada
![Data Science Toolkit 3](/img/3.png)


# Añado a .gitignore tanto el archivo como la carpeta
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ echo privada > .gitignore

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ echo privado.txt >> .gitignore

# Compruebo con un cat que he añadido a .gitignore tanto la carpeta como el txt
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ cat .gitignore
privada
privado.txt

# Añado al repositorio local el .gitignore, realizo un commit y un push para comprobar
# Así compruebo que solo he subido al repositorio el .gitignore 
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git add .gitignore

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git commit -m "añado archivo .gitignore"
[master 4e558c5] añado archivo .gitignore
warning: LF will be replaced by CRLF in .gitignore.
The file will have its original line endings in your working directory.
 1 file changed, 2 insertions(+)
 create mode 100644 .gitignore
![Data Science Toolkit 4](/img/4.png)

# Genero el archivo 1.txt con texto 1
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ echo 1 > 1.txt

# Añado el archivo 1.txt, hago commit y creo la tag ligera v0.1
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ echo 1 > 1.txt

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git add 1.txt
warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git commit -m "commit con 1.txt"
[master 2e39946] commit con 1.txt
warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.
 1 file changed, 1 insertion(+)
 create mode 100644 1.txt

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git tag v0.1

# Con el comando git tag compruebo que se ha creado la etiqueta v0.1 y con git show su contenido
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git tag
v0.1

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git show v0.1
commit 2e399468ee557ca5c9ed83ad177425f3988e993b
Author: César <cesarhernandez@campusciff.net>
Date:   Mon Nov 30 18:39:04 2015 +0100

    commit con 1.txt

diff --git a/1.txt b/1.txt
new file mode 100644
index 0000000..d00491f
--- /dev/null
+++ b/1.txt
@@ -0,0 +1 @@
+1

# Subo al repositorio remoto

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git push origin master
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 316 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@github.com:ciffcesarhernandez/campusciff.git
   4e558c5..2e39946  master -> master

# El fichero de texto 1.txt se ha subido correctamente al repositorio remoto
![Data Science Toolkit 5](/img/5.png)


# Creo la rama v0.2 y directamente me sitúo sobre ella con el comando git checkout -b
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git checkout -b v0.2
Switched to a new branch 'v0.2'

# Sobre la rama creo el archivo de texto 2.txt, lo añado y hago un commit
Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ echo 2 > 2.txt

Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ git add 2.txt
warning: LF will be replaced by CRLF in 2.txt.
The file will have its original line endings in your working directory.

Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ git commit -m "commit con 2.txt"
[v0.2 b915ed2] commit con 2.txt
warning: LF will be replaced by CRLF in 2.txt.
The file will have its original line endings in your working directory.
 1 file changed, 1 insertion(+)
 create mode 100644 2.txt

# Lo subo al repositorio remoto poniendo la rama destino v0.2
Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ git push origin v0.2
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 345 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@github.com:ciffcesarhernandez/campusciff.git
 * [new branch]      v0.2 -> v0.2

# Compruebo en el repositorio remoto que se ha creado la rama v0.2
# Donde se ha añadido el archivo 2.txt
![Data Science Toolkit 6](/img/6.png)


# Me sitúo en la rama master
Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.

# Realizo un merge con la rama v0.2
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git merge v0.2
Updating 2e39946..b915ed2
Fast-forward
 2.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 2.txt

# En la rama master añado Hola en el fichero 1.txt y hago commit
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ echo Hola>>1.txt

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ cat 1.txt
1
Hola

# Realizo el commit en master
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git add 1.txt
warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git commit -m "Hola en 1.txt"
[master warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.
cb0cb65] Hola en 1.txt
warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.
 1 file changed, 1 insertion(+)

# Me sitúo en la rama v0.2 y añado Adios en el archivo 1.txt
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git checkout v0.2
Switched to branch 'v0.2'

Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ echo Adios>>1.txt

Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ cat 1.txt
1
Adios

# Realizo el commit en la rama v0.2
Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ git add 1.txt
warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.

Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ git commit -m "Adios en 1.txt"
[v0.2 warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.
c439f18] Adios en 1.txt
warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.
 1 file changed, 1 insertion(+)

# Me posiciono de nuevo en la rama master
Sara Otero@SARA MINGW64 ~/20151130/campusciff (v0.2)
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

# Realizo el merge con la rama v0.2 y aparece el siguiente conflicto
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git merge v0.2
Auto-merging 1.txt
CONFLICT (content): Merge conflict in 1.txt
Automatic merge failed; fix conflicts and then commit the result.

# Listo ramas con merge
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master|MERGING)
$ git branch --merged
* master


# Listo ramas sin merge
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master|MERGING)
$ git branch --no-merged
  v0.2
# Para suprimir el conflicto, modifico 1.txt y lo dejo con el texto Hola y Adios
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master|MERGING)
$ echo Hola y Adios > 1.txt

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master|MERGING)
$ cat 1.txt
Hola y Adios

# Lo añado y hago commit
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master|MERGING)
$ git add 1.txt
warning: LF will be replaced by CRLF in 1.txt.
The file will have its original line endings in your working directory.

Sara Otero@SARA MINGW64 ~/20151130/campusciff (master|MERGING)
$ git commit -m "Hola y Adios en 1.txt"
[master e09b0d6] Hola y Adios en 1.txt

# Creo la tag v0.2
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git tag v0.2

# Listo los commits con sus ramas y tags
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git log --oneline --decorate --graph --all
*   e09b0d6 (HEAD -> master, tag: v0.2) Hola y Adios en 1.txt
|\
| * c439f18 (v0.2) Adios en 1.txt
* | cb0cb65 Hola en 1.txt
|/
* b915ed2 (origin/v0.2) commit con 2.txt
* 2e39946 (tag: v0.1, origin/master, origin/HEAD) commit con 1.txt
* 4e558c5 añado archivo .gitignore
* 37b42c3 commit inicial
* 82cfde1 Initial commit

# Borro la rama v0.2
Sara Otero@SARA MINGW64 ~/20151130/campusciff (master)
$ git branch -d v0.2
Deleted branch v0.2 (was c439f18).

# Imagen de perfil
![Data Science Toolkit 7](/img/7.png)

# Doble factor de autenticación activado
![Data Science Toolkit 8](/img/8.png)

# Compañeros a los que sigo
![Data Science Toolkit 9](/img/9.png)

# Repositorios seguidos y estrellas añadidas
![Data Science Toolkit 10](/img/10..png)

# Creo una tabla con los usuarios de mis compañeros
| NOMBRE | GITHUB | 
| ------- | ------- | 
| Sara Otero | [Enlace a URL Sara](https://github.com/ciffSara) | 
| Alejandro Díaz | [Enlace a URL Alejandro](https://github.com/adiazgalache) |
| Goaluix | https://github.com/goaluix |

# Añado a asanzdiego como colaborador de mi repositorio campusciff
![Data Science Toolkit 11](/img/11.png)

# Organización campusciff-ciffcesarhernandez creada
[Este es el enlace de mi organización campusciff-ciffcesarhernandez](https://github.com/campusciff-ciffcesarhernandez)

![Data Science Toolkit 12](/img/12.png)

# Creados los equipos colaboradores y administradores en mi organización
![Data Science Toolkit 13](/img/13.png)

# Creo en mi organización un repositorio para poder ejecutar páginas web ciffcesarhernandez.github.io
![Data Science Toolkit 14](/img/14.png)

# Y realizo un clonado


Sara Otero@SARA MINGW64 ~ (master)
$ git config --global user.name "César"

Sara Otero@SARA MINGW64 ~ (master)
$ git config --global user.email "cesarhernandez@campusciff.net"

Sara Otero@SARA MINGW64 ~ (master)
$ cd 20151130/

Sara Otero@SARA MINGW64 ~/20151130 (master)
$ git init
Reinitialized existing Git repository in C:/Users/Sara Otero/20151130/.git/


Sara Otero@SARA MINGW64 ~/20151130 (master)
$ git clone git@github.com:campusciff-ciffcesarhernandez/campusciff-ciffcesarhernandez.github.io.git
Cloning into 'campusciff-ciffcesarhernandez.github.io'...
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
warning: You appear to have cloned an empty repository.
Checking connectivity... done.

# En esa ubicación de mi máquina dejo una copia de mi index.html
![Data Science Toolkit 15](/img/15.png)

# Y realizo la subida a mi repositorio remoto

Sara Otero@SARA MINGW64 ~/20151130 (master)
$ cd campusciff-ciffcesarhernandez.github.io/



Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git add index.html

Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git commit -m "Subiendo index"
[master (root-commit) 166f124] Subiendo index
 1 file changed, 9 insertions(+)
 create mode 100644 index.html

Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git push origin master
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 335 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@github.com:campusciff-ciffcesarhernandez/campusciff-ciffcesarhernandez.github.io.git
 * [new branch]      master -> master

# Aquí proporciono la URL de mi Servidor web 
[Pincha aquí para acceder a mi servidor WEB en GITHUB](http://campusciff-ciffcesarhernandez.github.io/)

# Mi primer fork
![Data Science Toolkit 16](/img/16.png)

# Y hago un clonado del repositorio
Sara Otero@SARA MINGW64 ~/20151130 (master)
$ git clone git@github.com:campusciff-ciffcesarhernandez/campusciff-Miriam-Asenjo.github.io.git
Cloning into 'campusciff-Miriam-Asenjo.github.io'...
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 9 (delta 1), reused 9 (delta 1), pack-reused 0
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (1/1), done.
Checking connectivity... done.

# Me sitúo en el directorio y creo una nueva rama llamada brCESAR
Sara Otero@SARA MINGW64 ~/20151130 (master)
$ cd campusciff-Miriam-Asenjo.github.io/1

Sara Otero@SARA MINGW64 ~/20151130/campusciff-Miriam-Asenjo.github.io (master)
$ git checkout -b brCESAR
Switched to a new branch 'brCESAR'

# Tras la inclusión de mi nombre, realizo la subida al repositorio remoto
Sara Otero@SARA MINGW64 ~/20151130/campusciff-Miriam-Asenjo.github.io (brCESAR)
$ git add index.html

Sara Otero@SARA MINGW64 ~/20151130/campusciff-Miriam-Asenjo.github.io (brCESAR)
$ git commit -m "Subiendo index-miriam con fork cesar"
[brCESAR 450dbbd] Subiendo index-miriam con fork cesar
 1 file changed, 1 insertion(+)

Sara Otero@SARA MINGW64 ~/20151130/campusciff-Miriam-Asenjo.github.io (brCESAR)
$ git push origin brCESAR
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 343 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To git@github.com:campusciff-ciffcesarhernandez/campusciff-Miriam-Asenjo.github.io.git
 * [new branch]      brCESAR -> brCESAR

# Por último, envío una petición de pull request
![Data Science Toolkit 17](/img/17.png)


# Este es mi segundo fork
![Data Science Toolkit 18](/img/18.png)

# Hago un clonado del repositorio

Sara Otero@SARA MINGW64 ~/20151130 (master)
$ git clone git@github.com:campusciff-ciffcesarhernandez/campusciff-2015-1.github.io.git
Cloning into 'campusciff-2015-1.github.io'...
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
remote: Counting objects: 15, done.
remote: Total 15 (delta 0), reused 0 (delta 0), pack-reused 15
Receiving objects: 100% (15/15), done.
Resolving deltas: 100% (4/4), done.
Checking connectivity... done.

# Me sitúo en el directorio y creo una nueva rama llamada brCESAR
Sara Otero@SARA MINGW64 ~/20151130 (master)
$ cd campusciff-2015-1.github.io/

Sara Otero@SARA MINGW64 ~/20151130/campusciff-2015-1.github.io (master)
$ git checkout -b brCESAR
M       index.html
Switched to a new branch 'brCESAR'




# Tras la inclusión de mi nombre, realizo la subida al repositorio remoto
Sara Otero@SARA MINGW64 ~/20151130/campusciff-2015-1.github.io (brCESAR)
$ git add index.html

Sara Otero@SARA MINGW64 ~/20151130/campusciff-2015-1.github.io (brCESAR)
$ git commit -m "Subiendo index.html elelement con fork cesar"                  [brCESAR 3e2ed2a] Subiendo index.html elelement con fork cesar
 1 file changed, 3 insertions(+)

Sara Otero@SARA MINGW64 ~/20151130/campusciff-2015-1.github.io (brCESAR)
$ git push origin brCESAR                                                       Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 365 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To git@github.com:campusciff-ciffcesarhernandez/campusciff-2015-1.github.io.git
 * [new branch]      brCESAR -> brCESAR

# Por último, envío una petición de pull request
![Data Science Toolkit 19](/img/19.png)

# Acepto la petición de pull request de goaluix pulsando en Merge pull request

![Data Science Toolkit 20](/img/20.png)

# Solicitud aceptada

![Data Science Toolkit 21](/img/21.png)

Este es el cambio realizado:
![Data Science Toolkit 22](/img/22.png)

[Se puede comprobar en la URL de mi servidor web](http://campusciff-ciffcesarhernandez.github.io/)



# Tengo una segunda petición de pull request de crisrodfra que tiene problemas en el Merge 
# Por ello voy a actualizar mi repositorio local con un pull de la rama master para coger este último cambio de goaluix y realizar el merge sobre él.
~~~
Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git pull git@github.com:campusciff-ciffcesarhernandez/campusciff-ciffcesarhernandez.github.io.git master
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 1), reused 4 (delta 1), pack-reused 0
Unpacking objects: 100% (4/4), done.
From github.com:campusciff-ciffcesarhernandez/campusciff-ciffcesarhernandez.github.io
 * branch            master     -> FETCH_HEAD
Updating 166f124..15a8785
Fast-forward
 index.html | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
~~~


# Ahora me posiciono en la rama crisrodfra-cristobal
~~~
Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git checkout -b crisrodfra-cristobal master
Switched to a new branch 'crisrodfra-cristobal'
~~~

# y realizo un pull sobre esa rama, produciendose un conflicto en el merge automático
~~~

Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (crisrodfra-cristobal)
$ git pull https://github.com/crisrodfra/campusciff-ciffcesarhernandez.github.io.git cristobal
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/crisrodfra/campusciff-ciffcesarhernandez.github.io
 * branch            cristobal  -> FETCH_HEAD
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
~~~

# Hago un diff para ver las diferencias
~~~
Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (crisrodfra-cristobal|MERGING)
$ git diff
diff --cc index.html
index 46b5381,d6789cb..0000000
--- a/index.html
+++ b/index.html
@@@ -6,4 -6,5 +6,9 @@@
  <BODY>
  <P>Cesar Hernandez, bienvenido al mundo GIT</P>
  </BODY>
++<<<<<<< HEAD
 +</HTML>Luis Nuño
++=======
+ </HTML>
+ Cristobal - fork
++>>>>>>> de0043d3dade13cc0f0947c24c31e705b3ef2339
~~~
# Una vez resueltos  los problemas de conflicto realizo una nueva subida a mi servidor
~~~
Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (crisrodfra-cristobal)
$ git checkout master
Switched to branch 'master'

Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git add .

Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git commit -m "commit con comentario cristobal"
[master 6e72f38] commit con comentario cristobal
 1 file changed, 1 insertion(+)

Sara Otero@SARA MINGW64 ~/20151130/campusciff-ciffcesarhernandez.github.io (master)
$ git push origin master
Enter passphrase for key '/c/Users/Sara Otero/.ssh/id_rsa':
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 307 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To git@github.com:campusciff-ciffcesarhernandez/campusciff-ciffcesarhernandez.github.io.git
   15a8785..6e72f38  master -> master

~~~

[Se puede comprobar en la URL de mi servidor web que la subida ha sido correcta](http://campusciff-ciffcesarhernandez.github.io/)