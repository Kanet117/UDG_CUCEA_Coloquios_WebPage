# Coloquio de Cuerpos Académicos (CCAs) — Página Web

Sitio web oficial del Coloquio de Cuerpos Académicos del Centro Universitario de Ciencias Económico Administrativas (CUCEA) de la Universidad de Guadalajara.

- **Sitio en producción (Drupal)**: [https://ccas.cucea.udg.mx/inicio](https://ccas.cucea.udg.mx/inicio)
- **Repositorio GitHub**: [github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage](https://github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage)
- **Wiki del proyecto**: [github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage/wiki](https://github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage/wiki)
- **Documento de entrega**: [ENTREGA_FINAL.md](ENTREGA_FINAL.md)

## Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Flask 3.1 (Python 3) con Jinja2 |
| Frontend | HTML5, CSS3 (Flexbox + Grid), JavaScript vanilla |
| Dependencias | Solo Flask (sin Bootstrap, jQuery, o FontAwesome) |
| CMS (producción) | Drupal 10 |

## Estructura del proyecto

```
├── app.py                       # Servidor Flask con 8 rutas
├── requirements.txt             # flask>=3.0
├── .gitignore                   # Excluye venv/, memory-bank/, etc.
├── ENTREGA_FINAL.md             # Documento completo para entrega
├── CHECKLIST_ENTREGA.md         # Lista de verificación pre-entrega
├── README.md                    # Este archivo
├── LICENSE                      # MIT
├── drupal_raw/                  # Código HTML/CSS/JS para copiar a Drupal
│   ├── inicio.html
│   ├── convocatorias.html
│   ├── comite.html
│   ├── conferencistas.html
│   ├── guias.html
│   ├── registro.html
│   ├── programa.html
│   └── footer_navbar.html
├── templates/                   # Templates Flask (Jinja2)
│   ├── base.html                # Layout base (navbar + footer compartidos)
│   ├── inicio.html              # Página principal
│   ├── comite.html              # Comité organizador
│   ├── conferencistas.html      # Conferencistas plenarios
│   ├── convocatorias.html       # Convocatorias
│   ├── guias.html               # Guías para ponencias y capítulos
│   ├── programa.html            # Programa del evento
│   └── registro.html            # Formularios de registro
├── static/
│   ├── css/
│   │   ├── global.css           # Estilos compartidos (navbar, footer, reset)
│   │   ├── inicio.css           # Banner, acordeones
│   │   ├── comite.css           # Tarjetas de comité
│   │   ├── conferencistas.css   # Speaker cards
│   │   ├── convocatorias.css    # Convocatorias
│   │   ├── guias.css            # Cajas informativas, tablas
│   │   ├── programa.css         # Programa, enlaces YouTube
│   │   └── registro.css         # Botones de formulario
│   └── js/main.js
└── wiki/                        # Documentación (cargada en GitHub Wiki)
    ├── Home.md
    ├── Experiencia-y-Lecciones.md
    ├── Arquitectura-del-Sistema.md
    ├── Guia-de-Modificacion-Drupal.md
    ├── Guia-de-Solucion-de-Fallos.md
    ├── Cronologia-del-Proyecto.md
    ├── Enlaces-y-Recursos.md
    └── _Sidebar.md
```

## Instalación y ejecución (Flask)

```bash
# 1. Clonar el repositorio
git clone git@github.com:Kanet117/UDG_CUCEA_Coloquios_WebPage.git
cd UDG_CUCEA_Coloquios_WebPage

# 2. Crear entorno virtual e instalar Flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Ejecutar
python app.py
```

El servidor corre en `http://localhost:5000`.

## Rutas disponibles

| Ruta | Página | Producción |
|---|---|---|
| `/` | Inicio | [ccas.cucea.udg.mx/inicio](https://ccas.cucea.udg.mx/inicio) |
| `/inicio` | Inicio | mismo |
| `/comite` | Comité organizador | [ccas.cucea.udg.mx/comite](https://ccas.cucea.udg.mx/comite) |
| `/conferencistas` | Conferencistas | [ccas.cucea.udg.mx/conferencistas](https://ccas.cucea.udg.mx/conferencistas) |
| `/convocatorias` | Convocatorias | [ccas.cucea.udg.mx/convocatorias](https://ccas.cucea.udg.mx/convocatorias) |
| `/programa` | Programa del evento | [ccas.cucea.udg.mx/programa](https://ccas.cucea.udg.mx/programa) |
| `/guias` | Guías | [ccas.cucea.udg.mx/guias](https://ccas.cucea.udg.mx/guias) |
| `/registro` | Registro | [ccas.cucea.udg.mx/registro](https://ccas.cucea.udg.mx/registro) |

## Documentación

- **Documento de entrega**: [ENTREGA_FINAL.md](ENTREGA_FINAL.md) — arquitectura, qué se hizo, cómo, por qué, guía de modificación, solución de fallos
- **Checklist de verificación**: [CHECKLIST_ENTREGA.md](CHECKLIST_ENTREGA.md) — ~80 ítems para verificar antes de entregar
- **GitHub Wiki**: [github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage/wiki](https://github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage/wiki) — experiencia, cronología, guías Drupal, solución de fallos

## Cómo modificar el sitio en Drupal

1. Iniciar sesión en `https://ccas.cucea.udg.mx/user`
2. Ir a **Contenido** → buscar la página → **Editar**
3. Click en **Fuente HTML** (`<>`) → seleccionar **"HTML completo"**
4. Editar y **Guardar**

Para más detalles, ver [Guia-de-Modificacion-Drupal.md](wiki/Guia-de-Modificacion-Drupal.md) o la [Wiki](https://github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage/wiki/Guia-de-Modificacion-Drupal).

## Créditos

| Rol | Persona |
|---|---|
| Contenido | Dra. Karen Hernández |
| Desarrollo | Jesús A. García Pérez |
| Frontend | [Kanet Sahid Ochoa Guzmán](https://www.linkedin.com/in/kanet-sahid-ochoa-guzman-chaptter/) |
| Web | Ángela Jusuneith Silva Ramírez |

## Licencia

MIT License — ver [LICENSE](LICENSE).