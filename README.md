<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Character API</h3>

  <p align="center">
    CRUD API with FastAPI, SQLAlchemy, SQLite and Pydantic
    <a href="https://github.com/jbozas/todo-challenge"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jbozas/todo-challenge">Report Bug</a>
    <a href="https://github.com/jbozas/todo-challenge">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



### Built With

[![FastAPI][FastAPI-url]][FastAPI-url]
[![Sqlite][Sqlite-url]][Sqlite-url]
[![Sqlalchemy][Sqlalchemy-url]][Sqlalchemy-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Resolución del enunciado ERS:

* Crear una API con Python, usando el framework FastAPI. Crear una base de datos relacional SQlite, que se gestione
mediante la ORM SQAlchemy.
* Crear un modelo Character que disponga de los atributos id: int(PK), name: str, height: float, mass: float, hair_color: str, skin_color: str, eye_color: str, birth_year: int.
* Crear las siguientes rutas:
  * /character/getAll [GET] -> Retornar la lista de todos los ítems existentes:
      Deberá retornar la lista con todos los Characters. Los datos de cada Character
      deberán ser: id, name, height, mass, birth_year, eye_color
  * /character/get/{id} [GET] -> Retornar Characters buscados por su id(todos los datos)
  * /character/add [POST] -> Insertar un nuevo Character
      Ningun campo puede ser null.
      Respetar los tipos de cada campo.
      No debería existir un item con ese ID.
      En caso de que algun error de estos ocurra, retornar 400 con el problema.
  * /character/delete/{id} [DELETE] -> Eliminar un Character
    Si el character existe se elimina y se deberá retornar un HTTP CODE 200
    con un detalle acorde a la acción que se realizó
    Si el character no existe deberá retornar un HTTP Code 400 – Bad Request
    con el detalle acorde al problema que se produjo.


Consideraciones
* Crear Colección en POSTMAN - DONE 
* Agregar Dockerfile - DONE
* Agregar Documentación - DONE
* Agregar Logs - DONE
* Deployarlo
* Agregar pre-commit - DONE
* Agregar mypy - DONE
* Agregar requirements con versions - DONE

### Installation

1. Build the image.
   ```
   docker build -t character-api .
   ```
2. Run it.
   ```
   docker run -p 8000:8000 character-api
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jbozas/todo-challenge.svg?style=for-the-badge
[contributors-url]: https://github.com/jbozas/todo-challenge/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jbozas/todo-challenge.svg?style=for-the-badge
[forks-url]: https://github.com/jbozas/todo-challenge/network/members
[stars-shield]: https://img.shields.io/github/stars/jbozas/todo-challenge.svg?style=for-the-badge
[stars-url]: https://github.com/jbozas/todo-challenge/stargazers
[issues-shield]: https://img.shields.io/github/issues/jbozas/todo-challenge.svg?style=for-the-badge
[issues-url]: https://github.com/jbozas/todo-challenge/issues
[license-shield]: https://img.shields.io/github/license/jbozas/todo-challenge.svg?style=for-the-badge
[license-url]: https://github.com/jbozas/todo-challenge/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jbozas
[product-screenshot]: images/screenshot.png
[Fastapi-url]: https://img.shields.io/badge/fastapi-%252300ADD8.svg?style=for-the-badge&logo=fastapi&logoColor=white
[Sqlalchemy-url]: https://img.shields.io/badge/sqlalchemy-%252300ADD8.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white
[Sqlite-url]: https://img.shields.io/badge/sqlite-%252300ADD8.svg?style=for-the-badge&logo=sqlite&logoColor=white