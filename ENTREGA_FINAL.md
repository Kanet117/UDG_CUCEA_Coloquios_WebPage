# Coloquio de Cuerpos Académicos (CCAs) — Documento de Entrega

## 1. Portada

| Campo | Valor |
|---|---|
| **Proyecto** | Sitio web del Coloquio de Cuerpos Académicos (CCAs) |
| **Institución** | Centro Universitario de Ciencias Económico Administrativas (CUCEA) — Universidad de Guadalajara |
| **Departamento** | Departamento de Sistemas de Información (DSI) |
| **Desarrollador frontend** | Kanet Sahid Ochoa Guzmán |
| **Repositorio GitHub** | [github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage](https://github.com/Kanet117/UDG_CUCEA_Coloquios_WebPage) |
| **Sitio en producción** | [https://ccas.cucea.udg.mx/inicio](https://ccas.cucea.udg.mx/inicio) |
| **Fecha de entrega** | Junio 2026 |

---

## 2. Resumen Ejecutivo

Se desarrolló el sitio web oficial del Coloquio de Cuerpos Académicos (CCAs) del CUCEA UdeG. Originalmente implementado en Drupal 10, el proyecto enfrentó severos retrasos por burocracia institucional (~3 meses para obtener el primer acceso al sistema, y permisos de CSS incompletos después de 4 meses de desarrollo). Para sortear estas limitaciones, se utilizaron técnicas como inyección de CSS/JS mediante bloques HTML, redirecciones por script en el footer, y sobreescritura de estilos Drupal con `!important`. Finalmente, se entregó una versión equivalente en Flask + HTML/CSS/JS puro para garantizar independencia tecnológica futura.

---

## 3. Arquitectura del Sistema

### 3.1 Stack Tecnológico

| Capa | Tecnología | Propósito |
|---|---|---|
| Backend | **Flask 3.1.3** (Python 3.12) | Servidor web con 7 rutas REST |
| Templates | **Jinja2** (incluido en Flask) | Herencia de layouts con `base.html` |
| Frontend | **HTML5 + CSS3** (Flexbox + Grid) | Maquetación responsive |
| JavaScript | **Vanilla JS** | Mínimo, solo redirecciones |
| Base de datos | Ninguna | Sitio 100% estático |
| Dependencias | Solo Flask | Sin Bootstrap, jQuery, o FontAwesome |

### 3.2 Diagrama de Carpetas

```
UDG_CUCEA_Coloquios_WebPage/
├── app.py                    # Servidor Flask (6 rutas)
├── requirements.txt          # flask>=3.0
├── .gitignore                # Excluye venv, __pycache__, etc.
├── templates/
│   ├── base.html             # Layout base (navbar + footer)
│   ├── inicio.html           # Página principal
│   ├── comite.html           # Comité organizador
│   ├── conferencistas.html   # Conferencias plenarias
│   ├── convocatorias.html    # Convocatorias + iframe PDF
│   ├── guias.html            # Guías para ponencias y capítulos
│   ├── programa.html         # Programa del evento
│   └── registro.html         # Formularios de registro
├── static/
│   ├── css/
│   │   ├── global.css        # Navbar, footer, reset
│   │   ├── inicio.css        # Acordeones, banner, botones
│   │   ├── comite.css        # Tarjetas de comité
│   │   ├── conferencistas.css # Speaker cards
│   │   ├── convocatorias.css  # Convocatorias
│   │   ├── guias.css          # Cajas informativas + fechas
│   │   ├── programa.css       # Programa, enlaces YouTube
│   │   └── registro.css       # Botones de formulario
│   ├── js/main.js
├── drupal_raw/               # Código para copiar/pegar en Drupal
│   ├── inicio.html
│   ├── convocatorias.html
│   ├── comite.html
│   ├── conferencistas.html
│   ├── guias.html
│   ├── registro.html
│   ├── programa.html
│   └── footer_navbar.html
└── drupal_inicio_clase.html
```

### 3.3 Diagrama de Rutas

```
/ ──────────► inicio.html
/inicio ────► inicio.html
/comite ────► comite.html
/conferencistas ──► conferencistas.html
/convocatorias ──► convocatorias.html
/programa ──► programa.html
/guias ─────► guias.html
/registro ──► registro.html
```

---

## 4. ¿Qué se hizo?

Se migró el sitio de Drupal 10 a Flask + HTML/CSS/JS puro, y se dejó una copia del código crudo (carpeta `drupal_raw/`) para mantener la versión Drupal funcional.

### Páginas creadas:

| Página | Contenido |
|---|---|
| **Inicio** | Banner principal, descripción del coloquio, acordeón de objetivos (CSS puro), acordeón de eventos anteriores con botones a ediciones pasadas, modalidad virtual y costo |
| **Comité** | Tarjetas con header de color y borde para cada CA participante, agrupación responsiva en columnas |
| **Conferencistas** | Speaker cards con foto a izquierda/derecha alternante (nth-child even), biografía, fecha/hora, y enlaces a publicaciones |
| **Convocatorias** | Caja informativa, grid de fechas (3 columnas con colores), sección de publicación de libro científico, iframe con PDF de convocatoria |
| **Guías** | Caja informativa + tabla de fechas para ponencias y publicación de capítulos, con enlaces a Google Docs |
| **Programa** | Banner azul con fechas, imágenes del programa, enlaces a YouTube por día |
| **Registro** | Botones de registro para asistentes y ponentes, con estado disabled para registro no disponible |

### Componentes compartidos:
- **Navbar**: Barra azul con 8 enlaces, primer elemento (CCAs) empuja los demás a la derecha con `margin-right: auto`
- **Footer**: 3 bandas (azul "Instituciones participantes", blanca con logos, gris con contacto y créditos minimalistas con LinkedIn)

---

## 5. ¿Cómo se hizo?

### 5.1 Migración Drupal → Flask

1. **Extracción de contenido**: Se copió el HTML + CSS inline de cada página Drupal (página básica → fuente HTML).
2. **Separación de CSS**: Todo el CSS que estaba inline en Drupal se extrajo a archivos `.css` dedicados.
3. **Eliminación de `!important`**: En Drupal eran necesarios para vencer al tema. En Flask sobran y se eliminaron.
4. **Unificación de componentes**: Navbar y footer se unificaron en `templates/base.html` con herencia Jinja2.
5. **Ruteo**: Flask mapea 7 rutas a sus respectivos templates.

### 5.2 En Drupal (versión original)

- Las páginas se crearon como **páginas básicas** en `Contenido → Agregar contenido → Página básica`.
- El CSS/JS se inyectó directamente en el cuerpo HTML usando etiquetas `<style>` y `<script>`.
- El navbar se configuró como **bloque personalizado** y el footer como **bloque global CCAs**.
- Se usaron selectores `!important` para invalidar los estilos del tema Drupal (a los que no se tenía acceso).
- Se añadió un script en el footer para redirigir `/` a `/inicio`.

---

## 6. ¿Por qué se hizo así?

### Contexto del proyecto

| Hecho | Detalle |
|---|---|
| **Proyecto original** | Iba a ser una app con machine learning para predicción de sarcopenia, pero alguien borró el nombre del desarrollador del Excel de asignación y la coordinadora no intervino |
| **Elección tecnológica inicial** | Se preguntó qué tecnologías usar; primero dijeron "las que quieras", luego un maestro dijo "Drupal o PHP", forzando Drupal |
| **Primer acceso a Drupal** | ~3 meses de espera (febrero a mayo 2025) |
| **Acceso a CSS** | Nunca se otorgó completamente — después de 4 meses de desarrollo, los permisos de diseño seguían sin habilitarse |
| **Solución** | Se usaron páginas básicas (permiten HTML/CSS/JS) y se inyectó todo mediante `<style>` y `<script>`, incluyendo hacks como desactivar la animación Smoove del tema Drupal |

### Decisiones técnicas:

| Decisión | Razón |
|---|---|
| Flask en vez de mantener Drupal | Independencia tecnológica, cero burocracia, deploy simple |
| CSS en archivos separados | Mejor organización, mantenibilidad, eliminación de `!important` |
| Navbar/footer copiados en cada template | Sin dependencias JS para estructura base |
| Iconos SVG inline | Sin FontAwesome, cero dependencias externas |
| Acordeones con checkbox | Sin JavaScript para funcionalidad básica |

---

## 7. Guía de modificación del sitio

### 7.1 En Flask (código fuente)

| Tarea | Archivo(s) | Acción |
|---|---|---|
| Cambiar texto | `templates/[pagina].html` | Buscar el texto y reemplazar |
| Cambiar imagen | `templates/[pagina].html` | Cambiar `src="..."` por la nueva URL |
| Agregar enlace | `templates/[pagina].html` | Añadir `<a href="URL">Texto</a>` |
| Cambiar color | `static/css/[pagina].css` | Modificar el valor `color:` o `background-color:` |
| Agregar página | `app.py` + `templates/nueva.html` + `static/css/nueva.css` | Añadir ruta en Flask, template, y CSS |
| Cambiar navbar | `templates/base.html` | Editar los `<li>` dentro de `<ul class="navbar-nav">` |

### 7.2 En Drupal (producción)

1. **Iniciar sesión** en `https://ccas.cucea.udg.mx/user`
2. Ir a **Contenido** → buscar la página por título (ej. "inicio", "convocatoria")
3. Click en **Editar**
4. Click en **Fuente HTML** (ícono `<>`) para ver el código completo
5. **Importante**: Verificar que "HTML completo" esté seleccionado en el dropdown de formato de texto
6. Realizar los cambios necesarios
7. Click en **Guardar**

#### Para modificar el footer:
- Ir a **Estructura → Diseño de bloques → Biblioteca de bloques personalizados → Footer Global CCAs**
- El flujo es el mismo que editar una página básica

#### Para modificar el menú (navbar):
- Ir a **Estructura → Menús → Main navigation**
- Ahí se pueden agregar, quitar o reordenar enlaces
- Para cambiar el diseño (colores, fuente): modificar el CSS en el footer o en una página que tenga los estilos

---

## 8. Solución de fallos

| Síntoma | Causa probable | Solución |
|---|---|---|
| Página en blanco | Drupal bloqueó scripts/CSS por seguridad | Copiar código de `drupal_raw/`, pegarlo en Fuente HTML con "HTML completo" |
| CSS desaparecido | Drupal sobrescribió estilos o se perdió el bloque de footer | Revisar que el bloque Footer Global CCAs esté publicado en la región footer |
| Links rotos | La maestra modificó URLs de Google Forms, Drive, etc. | Editar la página y actualizar los `href` |
| Error "500 Internal Server" | Flask cayó o venv desactivado | `cd proyecto && source venv/bin/activate && python app.py` |
| Error 404 en ruta | La ruta no existe en `app.py` | Agregar `@app.route('/nueva')` y `return render_template('nueva.html')` |
| Imagen no carga | URL de Drupal cambió o servidor caído | Reemplazar `src` por URL alternativa o archivo local |
| Puerto 5000 ocupado | Otra app usando el puerto | Usar `python app.py` con puerto diferente o matar proceso anterior |
| Drupal borra el código | Seguridad de Drupal bloquea scripts | Pegar con "HTML completo" y verificar que no haya etiquetas mal formadas |

---

## 9. Links del sitio

| Página | URL Producción |
|---|---|
| Inicio | [https://ccas.cucea.udg.mx/inicio](https://ccas.cucea.udg.mx/inicio) |
| Convocatorias | [https://ccas.cucea.udg.mx/convocatorias](https://ccas.cucea.udg.mx/convocatorias) |
| Comité | [https://ccas.cucea.udg.mx/comite](https://ccas.cucea.udg.mx/comite) |
| Conferencistas | [https://ccas.cucea.udg.mx/conferencistas](https://ccas.cucea.udg.mx/conferencistas) |
| Guías | [https://ccas.cucea.udg.mx/guias](https://ccas.cucea.udg.mx/guias) |
| Registro | [https://ccas.cucea.udg.mx/registro](https://ccas.cucea.udg.mx/registro) |
| Programa | [https://ccas.cucea.udg.mx/programa](https://ccas.cucea.udg.mx/programa) |

### Documentos de referencia

| Recurso | Link |
|---|---|
| Google Sites (original) | [https://sites.google.com/d/1juGwGRJvkvc0qsvHg4X1eQ3EasGGFcrC/p/17iz2SYk2ob8sLvcpTD9FIV1rW0FKpC74/edit](https://sites.google.com/d/1juGwGRJvkvc0qsvHg4X1eQ3EasGGFcrC/p/17iz2SYk2ob8sLvcpTD9FIV1rW0FKpC74/edit) |
| Google Sites (actualizado) | [https://sites.google.com/d/1FDUiWyMUUeJvXgsT6Pg5_ipFKD9Y5BHA/p/12JgSB5wSs6Bt-ZTxMRXKtCamqLhVR6uD/edit](https://sites.google.com/d/1FDUiWyMUUeJvXgsT6Pg5_ipFKD9Y5BHA/p/12JgSB5wSs6Bt-ZTxMRXKtCamqLhVR6uD/edit) |
| Excel asignación | [https://docs.google.com/spreadsheets/d/1eVdrT9ZNAildLU46KgzS-z14LLtEddlu/edit?gid=111446450](https://docs.google.com/spreadsheets/d/1eVdrT9ZNAildLU46KgzS-z14LLtEddlu/edit?gid=111446450) |
| Drive requerimientos | [https://drive.google.com/drive/folders/1r0YyhaHqHGxSPT3g1cR9dxe_zX_10_4U](https://drive.google.com/drive/folders/1r0YyhaHqHGxSPT3g1cR9dxe_zX_10_4U) |

---

## 10. Créditos

| Rol | Persona |
|---|---|
| Contenido | Dra. Karen Hernández |
| Desarrollo | Jesús A. García Pérez |
| Frontend | Kanet Sahid Ochoa Guzmán |
| Web | Ángela Jusuneith Silva Ramírez |

## 11. Licencia

MIT License — ver archivo [LICENSE](LICENSE).