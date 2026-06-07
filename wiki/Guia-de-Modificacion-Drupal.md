# Guía de Modificación en Drupal

## Cómo editar una página

### Paso 1: Iniciar sesión
Ir a `https://ccas.cucea.udg.mx/user` e ingresar con credenciales de administrador.

### Paso 2: Encontrar la página
- Ir a **Contenido** → se mostrarán todas las páginas del sitio
- Buscar por título (ej. "inicio", "convocatoria", "comite")
- Click en **Editar**

### Paso 3: Editar el contenido
- La página se verá en modo preview con un editor visual
- **Dos formas de editar**:

#### Opción A: Editor visual (sin código)
- Seleccionar el texto o imagen directamente en el preview
- Usar las opciones de la barra de herramientas (negritas, colores, links)
- Ideal si no sabes HTML

#### Opción B: Fuente HTML (recomendado para cambios precisos)
- Click en el ícono **`<>`** (Fuente HTML)
- Se mostrará el código HTML completo
- **CRÍTICO**: Verificar que "HTML completo" esté seleccionado en el dropdown de formato de texto
- Realizar los cambios directamente en el código

### Paso 4: Guardar
- Click en **Guardar** (abajo)
- Opcional: click en **Preview** para ver cómo queda antes de guardar

---

## Cómo modificar el footer

1. Ir a **Estructura → Diseño de bloques → Biblioteca de bloques personalizados**
2. Buscar y clickear en **Footer Global CCAs**
3. El flujo es idéntico al de editar una página (Fuente HTML + Guardar)

---

## Cómo modificar el menú (navbar)

1. Ir a **Estructura → Menús → Main navigation**
2. Se verán todas las opciones del navbar:

| Enlace | Operations |
|---|---|
| CCAs | Editar |
| Inicio | Editar |
| Convocatoria | Editar |
| Comité | Editar |
| Guías | Editar |
| Registro | Editar |
| Programa | Editar |
| Conferencistas | Editar |

3. Click en **Editar** para modificar un enlace (título, ruta, peso)
4. Para **agregar**: Click en "Agregar enlace"
5. Para **eliminar**: Click en "Eliminar" (ej. para quitar RESDO como pidió la maestra)
6. El orden se controla con los pesos (valores más pequeños = arriba)

---

## Cómo reemplazar el PDF de convocatorias

1. Subir el nuevo PDF a Google Drive
2. Obtener el ID del archivo (ej. `13Y7NFPjp9BVZO2C17iC-ccZwR6ykr1Cu`)
3. Crear el enlace de preview: `https://drive.google.com/file/d/[ID]/preview`
4. Ir a la página **Convocatorias** en Drupal
5. Editar → Fuente HTML
6. Buscar el iframe y reemplazar el `src` por el nuevo
7. Guardar

---

## Cómo cambiar un link de YouTube

1. Ir a la página **Programa**
2. Editar → Fuente HTML
3. Buscar el `<a>` del día a modificar
4. Cambiar el `href` por la nueva URL de YouTube Live
5. Guardar

---

## Cómo agregar/quitar años en página de inicio

1. Ir a la página **Inicio**
2. Editar → Fuente HTML
3. Buscar los botones con clase `botton-events`
4. Agregar o quitar `<a class="botton-events" href="...">CCAs 20XX</a>`
5. Para desactivar un botón (futuro): usar clase `botton-events disabled`
6. Guardar