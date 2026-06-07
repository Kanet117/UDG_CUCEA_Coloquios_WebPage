# Checklist de Verificación Pre-Entrega — CCAs CUCEA

Marca cada ítem como ✅ (ok) o ❌ (falla) antes de la sesión de entrega.

---

## Funcionalidad del Sitio

- [ ] **Inicio** — La página /inicio carga correctamente
- [ ] **Comité** — La página /comite carga correctamente
- [ ] **Conferencistas** — La página /conferencistas carga correctamente
- [ ] **Convocatorias** — La página /convocatorias carga correctamente
- [ ] **Guías** — La página /guias carga correctamente
- [ ] **Programa** — La página /programa carga correctamente
- [ ] **Registro** — La página /registro carga correctamente
- [ ] **Redirección** — Entrar a `/` redirige a `/inicio`
- [ ] **Navbar** — Todos los enlaces del navbar llevan a la página correcta
- [ ] **Navbar activo** — La página actual se marca con `.active` (texto con sombra)
- [ ] **Acordeón Objetivos** — Abre y cierra al hacer click (Inicio)
- [ ] **Acordeón Eventos** — Abre y cierra al hacer click (Inicio)
- [ ] **Botones eventos anteriores** — Los 3 botones activos abren en nueva pestaña
- [ ] **Botones disabled** — CCAs 2026 y CCAs 2028 no son clickeables
- [ ] **Modalidad Virtual** — Texto e indicador de costo gratuito visibles
- [ ] **Links RESDO** — Abren en nueva pestaña correctamente
- [ ] **Registro asistentes** — Botón abre formulario Jotform
- [ ] **Someter ponencia** — Botón abre formulario Jotform
- [ ] **Registro disabled** — Botón "Registro de ponencia" no es clickeable
- [ ] **YouTube en Programa** — Los 5 botones abren los livestreams correctos
- [ ] **Imágenes programa** — Las 2 imágenes del programa cargan
- [ ] **PDF convocatorias** — El iframe de Google Drive carga el PDF

---

## Estilos y Diseño

- [ ] **Navbar azul** — Fondo #203864, texto blanco
- [ ] **Fuente navbar** — Roboto, 16px (22px el primer elemento CCAs)
- [ ] **Footer 3 bandas** — Azul, blanca (con logos), gris (con contacto)
- [ ] **Footer créditos** — Formato minimalista: label + nombre, links LinkedIn funcionales
- [ ] **Títulos de página** — Rojo #B22222, centrados, bold
- [ ] **Conferencistas: foto** — 220px de ancho, con borde 1px
- [ ] **Conferencistas: nombre bajo foto** — Rojo #B22222, bold, 16px
- [ ] **Conferencistas: "Título"** — Rojo #B22222, bold, antes del nombre de la charla
- [ ] **Conferencistas: título de charla** — Negro #000000
- [ ] **Conferencistas: fecha** — Naranja #FF6600, **sin año**
- [ ] **Conferencistas: sin h3 duplicado** — El nombre solo aparece bajo la foto
- [ ] **Comité: tarjetas** — Header de color + borde del mismo color
- [ ] **Guías: cajas** — Borde naranja/azul según sección
- [ ] **Guías: tablas fechas** — Fondo naranja o azul, texto blanco
- [ ] **Acordeones** — Fondo blanco, texto rojo #D90000, borde negro
- [ ] **Botones formulario** — Fondo #203864, hover más oscuro
- [ ] **Responsive** — El sitio se ve bien en móvil (navbar wrap, footer columna)
- [ ] **Banner** — Ocupa 100vw, centrado con transform translateX(-50%)

---

## Código Fuente (Flask)

- [ ] **Sin comentarios de IA** — No hay comentarios tipo "🔹", "/* Aquí va... */"
- [ ] **Sin `!important`** — No hay `!important` en archivos .css de Flask
- [ ] **HTML válido** — Sin etiquetas sin cerrar
- [ ] **CSS organizado** — global.css + 1 CSS por página
- [ ] **app.py funcional** — Todas las rutas retornan 200
- [ ] **requirements.txt** — flask>=3.0
- [ ] **.gitignore** — Excluye venv/, __pycache__/, .vscode/
- [ ] **README.md** — Actualizado con instrucciones completas

---

## Código Drupal (drupal_raw/)

- [ ] **inicio.html** — CSS + HTML completo listo para copiar
- [ ] **comite.html** — CSS + HTML completo listo para copiar
- [ ] **conferencistas.html** — CSS + HTML con cambios finales
- [ ] **convocatorias.html** — Incluye iframe de Google Drive
- [ ] **guias.html** — CSS + HTML completo
- [ ] **registro.html** — CSS + HTML completo
- [ ] **programa.html** — CSS + HTML completo
- [ ] **footer_navbar.html** — CSS + JS + HTML completo (navbar blindado + footer)

---

## Documentación y Repositorio

- [ ] **ENTREGA_FINAL.md** — Creado con arquitectura, qué/cómo/por qué, guías
- [ ] **CHECKLIST_ENTREGA.md** — Este documento, completado
- [ ] **README.md** — Actualizado con instrucciones, rutas, troubleshooting
- [ ] **Wiki GitHub** — Páginas creadas (Home, Experiencia, Arquitectura, Guías, etc.)
- [ ] **LICENSE** — Archivo MIT presente
- [ ] **Último commit pusheado** — `git push origin main` ejecutado

---

## Seguridad

- [ ] **Sin claves/secretos** — No hay passwords, tokens, o API keys en el código
- [ ] **debug=False** — Flask en producción con `debug=False`
- [ ] **CORS/seguridad** — Los iframes cargan de fuentes confiables (Google Drive, YouTube)
- [ ] **Links externos** — Todos los `target="_blank"` tienen `rel="noopener"`

---

## Instrucciones para modificar

- [ ] Se explicó cómo editar páginas en Drupal (Fuente HTML)
- [ ] Se explicó cómo editar el footer (Bloques personalizados)
- [ ] Se explicó cómo editar el menú (Main navigation)
- [ ] Se explicó cómo agregar/quitar años en la página de inicio
- [ ] Se explicó cómo reemplazar el PDF de convocatorias
- [ ] Se explicó cómo cambiar un link de YouTube en Programa