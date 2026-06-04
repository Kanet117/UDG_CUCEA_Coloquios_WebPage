# Coloquio de Cuerpos Académicos (CCAs) — Página Web

Sitio web oficial del Coloquio de Cuerpos Académicos del Centro Universitario de Ciencias Económico Administrativas (CUCEA) de la Universidad de Guadalajara.

## Tecnologías

- **Backend**: Flask (Python 3) con Jinja2 templates
- **Frontend**: HTML5, CSS3 (Flexbox + Grid), JavaScript vanilla
- **Sin dependencias externas**: No Bootstrap, no jQuery, no FontAwesome

## Estructura del proyecto

```
├── app.py                 # Servidor Flask con todas las rutas
├── requirements.txt       # flask>=3.0
├── templates/
│   ├── base.html          # Layout base (navbar + footer compartidos)
│   ├── inicio.html        # Página principal
│   ├── comite.html        # Comité organizador
│   ├── conferencistas.html# Conferencistas plenarios
│   ├── convocatorias.html # Convocatorias
│   ├── guias.html         # Guías para ponencias y capítulos
│   ├── programa.html      # Programa del evento
│   └── registro.html      # Formularios de registro
├── static/
│   ├── css/
│   │   ├── global.css     # Estilos compartidos (navbar, footer, reset)
│   │   ├── inicio.css     # Banner, acordeones
│   │   ├── comite.css     # Tarjetas de comité
│   │   ├── conferencistas.css # Speaker cards
│   │   ├── convocatorias.css  # Convocatorias
│   │   ├── guias.css      # Cajas informativas, tablas
│   │   ├── programa.css   # Programa, enlaces YouTube
│   │   └── registro.css   # Botones de formulario
│   └── js/
│       └── main.js
├── LICENSE                # MIT
└── README.md
```

## Instalación y ejecución

```bash
python3 -m venv venv
venv/bin/pip install flask
venv/bin/python app.py
```

El servidor corre en `http://localhost:5000`.

## Rutas disponibles

| Ruta | Página |
|------|--------|
| `/` | Inicio |
| `/inicio` | Inicio |
| `/convocatorias` | Convocatorias |
| `/comite` | Comité |
| `/guias` | Guías |
| `/registro` | Registro |
| `/programa` | Programa |
| `/conferencistas` | Conferencistas |

## Créditos

| Rol | Persona |
|------|---------|
| Contenido | Dra. Karen Hernández |
| Desarrollo | Jesús A. García Pérez |
| Frontend | [Kanet Sahid Ochoa Guzmán](https://www.linkedin.com/in/kanet-sahid-ochoa-guzman-chaptter/) |
| Web | Ángela Jusuneith Silva Ramírez |

## Licencia

MIT License — ver [LICENSE](LICENSE).