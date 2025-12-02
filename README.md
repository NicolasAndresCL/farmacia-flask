# 🏥 Sistema de Gestión de Medicamentos (Flask + SQLAlchemy)
Este proyecto es una aplicación web desarrollada con Flask que simula la gestión de medicamentos en un entorno de farmacia. Permite registrar ingresos y salidas de medicamentos, mantener un stock actualizado automáticamente y visualizar historiales de movimientos. Es parte de mi portafolio personal para mostrar habilidades en desarrollo backend, frontend y manejo de datos con persistencia real en base de datos.

## 🚀 Tecnologías utilizadas
- Python 3

- Flask (framework web)

- Jinja2 (templates HTML)

- CSS (tema oscuro estilo VS Code)

- SQLite (base de datos inicial, con posibilidad de migrar a MySQL/PostgreSQL)

- SQLAlchemy (ORM para modelos y relaciones)

- Flask-Migrate (migraciones de base de datos)

## 🎯 Objetivo del proyecto
Practicar y demostrar habilidades en desarrollo web backend con Flask.

Simular un sistema real de farmacia con ingresos, salidas y stock automático persistente.

Mostrar buenas prácticas de arquitectura, modularización y documentación para mi portafolio en GitHub.

Preparar el proyecto para migraciones futuras hacia MySQL o bases de datos más robustas.

Integrar conceptos de relaciones entre tablas (Ingresos, Salidas, Medicamentos, Stock).

## ⚙️ Cómo correr el proyecto
### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/farmacia-flask.git
cd farmacia-flask
```
### 2. Crear entorno virtual
```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Inicializar la base de datos
```bash
flask db init
flask db migrate -m "Inicial"
flask db upgrade
```
### 5. Ejecutar la aplicación
```bash
flask run
La aplicación estará disponible en: 👉 http://127.0.0.1:5000
```
## 📌 Próximos pasos
Añadir autenticación de usuarios y roles (ej. administrador, tens, médico).

Mejorar interfaz con Bootstrap o frameworks modernos.

Implementar reportes exportables (PDF/Excel).

Migrar a MySQL/PostgreSQL para producción.

Integrar pruebas unitarias y de integración.

## 👨‍💻 Autor
Nicolás Andrés Cano Leal Desarrollador Fullstack autodidacta y arquitecto técnico en formación. Actualmente explorando integración de Flask, SQLAlchemy y sistemas inteligentes para optimizar procesos en entornos reales.