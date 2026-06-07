# Guia de Solucion de Fallos

## Continuidad Operativa del Sitio

Esta guia documenta los escenarios mas comunes que pueden presentarse durante la operacion del sitio y las acciones recomendadas para restablecer el servicio.

### 1. La pagina se visualiza en blanco

**Causa probable**: El filtro de seguridad de Drupal puede bloquear ciertas etiquetas HTML si el formato de texto no es el correcto.

**Solucion**:
1. Ir a la pagina en Drupal → Editar
2. Click en **Fuente HTML** (icono `<>`)
3. Verificar que el formato de texto sea **"HTML completo"**
4. Pegar el codigo de la carpeta `drupal_raw/` (archivo correspondiente a la pagina)
5. Click en **Guardar**

### 2. Los estilos visuales del sitio no se aplican

**Causa probable**: El bloque global que contiene los estilos CSS puede estar despublicado o la region de footer puede haber cambiado.

**Solucion**:
1. Ir a **Estructura → Diseno de bloques**
2. Localizar el bloque **Footer Global CCAs**
3. Verificar que este **publicado** y asignado a la region **Footer**
4. Si es necesario, editar el bloque y pegar el codigo de `drupal_raw/footer_navbar.html`

### 3. Enlaces a formularios o documentos rotos

**Causa probable**: Las URLs de Google Forms, Google Drive u otros recursos externos fueron actualizadas.

**Solucion**:
1. Ir a la pagina que contiene el enlace
2. Editar → Fuente HTML
3. Localizar el atributo `href` del enlace y actualizar con la nueva URL
4. Guardar

### 4. Error 500 al ejecutar Flask localmente

**Causa probable**: El servidor Flask se detuvo o el entorno virtual esta desactivado.

**Solucion**:
```bash
cd /ruta/al/proyecto/UDG_CUCEA_Coloquios_WebPage
source venv/bin/activate
python app.py
```

### 5. Error 404 en una ruta de Flask

**Causa probable**: La ruta solicitada no esta definida en `app.py`.

**Solucion**: Agregar la ruta faltante:
```python
@app.route('/nueva-pagina')
def nueva_pagina():
    return render_template('nueva-pagina.html')
```

### 6. Imagen no se carga

**Causa probable**: La URL de la imagen cambio o el servidor de origen no esta disponible.

**Solucion**:
1. Editar la pagina → Fuente HTML
2. Localizar la etiqueta `<img>` y reemplazar el atributo `src` por la nueva URL
3. Si la imagen es local, subirla a Drupal en **Contenido → Archivos** y copiar la URL generada

### 7. Puerto 5000 ocupado

**Causa probable**: Otra instancia de Flask esta corriendo en el mismo puerto.

**Solucion**:
```bash
# Identificar y liberar el puerto
fuser -k 5000/tcp
# O ejecutar Flask en un puerto alternativo
python app.py
```

### 8. Drupal elimina el codigo al guardar

**Causa probable**: El formato de texto seleccionado no es "HTML completo". Drupal filtra etiquetas HTML en otros formatos.

**Solucion**: Antes de guardar, confirmar que el selector de formato de texto indique **"HTML completo"**, no "Texto plano" ni "Filtrado".

### 9. El menu de navegacion se ve diferente

**Causa probable**: Los estilos del navbar estan vinculados al bloque del footer. Si el bloque se despublica, los estilos se pierden.

**Solucion**: Verificar que el bloque **Footer Global CCAs** este publicado y asignado correctamente (ver punto 2).

### 10. Mensajes de seguridad en la consola del navegador

**Causa probable**: Politicas de seguridad de contenido (CSP) del servidor Drupal.

**Impacto**: Los mensajes son visibles unicamente en la consola de herramientas de desarrollador. **No afectan la experiencia del usuario ni el funcionamiento del sitio**.