# Arquitectura del Sistema

## Stack Tecnologico

| Capa | Tecnologia | Version |
|---|---|---|
| Backend | Flask (Python) | 3.1 |
| Template Engine | Jinja2 | (incluido en Flask) |
| Frontend | HTML5 + CSS3 (Flexbox + Grid) | — |
| JavaScript | Vanilla JS | — |
| CMS (produccion) | Drupal | 10 |
| Dependencias | Solo Flask | — |

## Diagrama de Carpetas (Flask)

```
UDG_CUCEA_Coloquios_WebPage/
├── app.py                       # Servidor Flask (8 rutas REST)
├── requirements.txt             # flask>=3.0
├── .gitignore                   # Exclusiones estandar
├── ENTREGA_FINAL.md             # Documento completo de entrega
├── CHECKLIST_ENTREGA.md         # Lista de verificacion pre-entrega
├── README.md                    # Instrucciones de instalacion
├── LICENSE                      # MIT
├── drupal_raw/                  # Codigo HTML/CSS/JS para copiar a Drupal
│   ├── inicio.html
│   ├── convocatorias.html
│   ├── comite.html
│   ├── conferencistas.html
│   ├── guias.html
│   ├── registro.html
│   ├── programa.html
│   └── footer_navbar.html
├── templates/                   # Templates Flask (Jinja2)
│   ├── base.html                # Layout base (navbar + footer)
│   ├── inicio.html              # Pagina principal
│   ├── comite.html              # Comite organizador
│   ├── conferencistas.html      # Conferencistas plenarios
│   ├── convocatorias.html       # Convocatorias + iframe PDF
│   ├── guias.html               # Guias para ponencias
│   ├── programa.html            # Programa del evento
│   └── registro.html            # Formularios de registro
├── static/
│   ├── css/
│   │   ├── global.css           # Navbar, footer, reset
│   │   ├── inicio.css           # Acordeones, banner, botones
│   │   ├── comite.css           # Tarjetas de comite
│   │   ├── conferencistas.css   # Speaker cards
│   │   ├── convocatorias.css    # Convocatorias
│   │   ├── guias.css            # Cajas informativas
│   │   ├── programa.css         # Programa, enlaces YouTube
│   │   └── registro.css         # Botones de formulario
│   └── js/main.js
└── wiki/                        # Documentacion (GitHub Wiki)
```

## Instalacion y Ejecucion (Flask)

### Requisitos Previos

- Python 3.10 o superior
- Git
- pip (incluido con Python)

### Pasos

```bash
# 1. Clonar el repositorio
git clone git@github.com:Kanet117/UDG_CUCEA_Coloquios_WebPage.git
cd UDG_CUCEA_Coloquios_WebPage

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar el entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicacion
python app.py
```

El servidor estara disponible en `http://localhost:5000`.

## Rutas Disponibles

| Ruta | Pagina | URL Produccion |
|---|---|---|
| `/` | Inicio | [ccas.cucea.udg.mx](https://ccas.cucea.udg.mx) |
| `/inicio` | Inicio | [ccas.cucea.udg.mx/inicio](https://ccas.cucea.udg.mx/inicio) |
| `/comite` | Comite organizador | [ccas.cucea.udg.mx/comite](https://ccas.cucea.udg.mx/comite) |
| `/conferencistas` | Conferencistas | [ccas.cucea.udg.mx/conferencistas](https://ccas.cucea.udg.mx/conferencistas) |
| `/convocatorias` | Convocatorias | [ccas.cucea.udg.mx/convocatorias](https://ccas.cucea.udg.mx/convocatorias) |
| `/programa` | Programa del evento | [ccas.cucea.udg.mx/programa](https://ccas.cucea.udg.mx/programa) |
| `/guias` | Guias | [ccas.cucea.udg.mx/guias](https://ccas.cucea.udg.mx/guias) |
| `/registro` | Registro | [ccas.cucea.udg.mx/registro](https://ccas.cucea.udg.mx/registro) |

## Decisiones de Diseno

### Navbar (Flexbox)
```css
.navbar-nav {
    display: flex;
    flex-direction: row;
    align-items: center;
}
.navbar-nav li:first-child {
    margin-right: auto;  /* Primer elemento (CCAs) empuja los demas a la derecha */
}
```

### Footer (3 bandas + Grid)
```css
.footer-info-flex {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}
```

### Acordeones (CSS puro)
```css
.accordion input[type="checkbox"]:checked ~ .accordion_text {
    height: auto;
}
```

### Banner Full-width
```css
.banner-ccas {
    width: 100vw;
    left: 50%;
    transform: translateX(-50%);
}
```

## Diagrama de Flujo de Datos

```
[Usuario] → Navegador → [Flask / Drupal] → [HTML + CSS + JS] → Renderizado
```

- **Sin base de datos**: Todo el contenido es estatico
- **Sin API**: Las rutas de Flask solo renderizan templates
- **Sin sesiones**: Sitio informativo, no requiere login