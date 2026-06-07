# Arquitectura del Sistema

## Stack Tecnológico

| Capa | Tecnología | Versión |
|---|---|---|
| Backend | Flask (Python) | 3.1.3 |
| Template Engine | Jinja2 | (incluido en Flask) |
| Frontend | HTML5 + CSS3 | — |
| JavaScript | Vanilla JS | — |
| CMS (producción) | Drupal | 10 |
| Servidor web | Nginx / Apache | — |
| Dependencias | Solo Flask | — |

## Diagrama de Carpetas (Flask)

```
UDG_CUCEA_Coloquios_WebPage/
├── app.py                 # 7 rutas REST
├── requirements.txt       # flask>=3.0
├── static/
│   ├── css/               # 8 archivos CSS
│   └── js/main.js
├── templates/
│   ├── base.html          # Layout base (herencia Jinja2)
│   ├── inicio.html
│   ├── comite.html
│   ├── conferencistas.html
│   ├── convocatorias.html
│   ├── guias.html
│   ├── programa.html
│   └── registro.html
├── drupal_raw/            # Código para copiar a Drupal
└── wiki/                  # Documentación en GitHub Wiki
```

## Flujo de Datos

```
[Usuario] → Navegador → [Flask / Drupal] → [HTML + CSS + JS] → Renderizado
```

- **No hay base de datos**: Todo el contenido es estático
- **No hay API**: Las rutas de Flask solo renderizan templates
- **No hay sesiones**: Es un sitio informativo, no requiere login

## Decisiones de Diseño

### Navbar (Flexbox)
```css
.navbar-nav {
    display: flex;
    flex-direction: row;
    align-items: center;
}
.navbar-nav li:first-child {
    margin-right: auto;  /* Empuja los demás a la derecha */
}
```

### Footer (3 bandas + Grid)
```css
.footer-info-flex {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
}
```

### Acordeones (CSS puro, sin JS)
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