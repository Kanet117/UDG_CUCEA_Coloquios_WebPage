# Guía de Solución de Fallos

## Problemas Comunes y Soluciones

### 1. La página se ve en blanco

**Causa probable**: Drupal bloqueó scripts o CSS por seguridad. Esto pasa cuando el contenido HTML tiene etiquetas que Drupal considera inseguras.

**Solución**:
1. Ir a la página en Drupal → Editar
2. Click en **Fuente HTML** (ícono `<>`)
3. Verificar que el dropdown de formato de texto diga **"HTML completo"**
4. Pegar el código de la carpeta `drupal_raw/` (el archivo correspondiente a la página)
5. Click en **Guardar**

---

### 2. El CSS del sitio desapareció

**Causa probable**: El bloque de footer que contiene los estilos globales se despublicó o Drupal sobrescribió los estilos del theme.

**Solución**:
1. Ir a **Estructura → Diseño de bloques**
2. Buscar el bloque **Footer Global CCAs**
3. Verificar que esté **publicado** (check activo)
4. Verificar que esté asignado a la región **Footer**
5. Si está todo bien, editar el bloque y pegar el código de `drupal_raw/footer_navbar.html`

---

### 3. Links rotos (Google Forms, Drive, etc.)

**Causa probable**: La Dra. Karen modificó las URLs de los formularios o documentos.

**Solución**:
1. Ir a la página que contiene el link roto
2. Editar → Fuente HTML
3. Buscar el `href` del link y reemplazar por la nueva URL
4. Guardar

---

### 4. Error 500 al cargar Flask

**Causa probable**: El servidor Flask se cayó o el virtualenv está desactivado.

**Solución**:
```bash
cd /ruta/al/proyecto/UDG_CUCEA_Coloquios_WebPage
source venv/bin/activate
python app.py
```

---

### 5. Error 404 en una ruta de Flask

**Causa probable**: La ruta no existe en `app.py`.

**Solución**: Agregar la ruta faltante:
```python
@app.route('/nueva-pagina')
def nueva_pagina():
    return render_template('nueva-pagina.html')
```

---

### 6. Imagen no carga

**Causa probable**: La URL de la imagen en Drupal cambió o el servidor está caído.

**Solución**:
1. Editar la página → Fuente HTML
2. Buscar el `<img>` y reemplazar `src` por la nueva URL
3. Si la imagen es local, subirla a Drupal en **Contenido → Archivos** y copiar la URL

---

### 7. Puerto 5000 ocupado

**Causa probable**: Otra instancia de Flask está corriendo.

**Solución**:
```bash
# Matar proceso en puerto 5000
fuser -k 5000/tcp
# O alternativamente
python app.py  # Flask usará otro puerto si el 5000 está ocupado
```

---

### 8. Drupal borra el código al guardar

**Causa probable**: El formato de texto no es "HTML completo". Drupal filtra etiquetas HTML si está en otro formato.

**Solución**: Antes de guardar, verificar que el dropdown de formato de texto diga **"HTML completo"**, no "Texto plano" ni "Filtrado".

---

### 9. El navbar se ve diferente

**Causa probable**: Los estilos del navbar están en el footer. Si el bloque del footer se despublicó, el navbar pierde los estilos.

**Solución**: Verificar que el bloque **Footer Global CCAs** esté publicado (ver punto 2).

---

### 10. Error de seguridad en consola del navegador

**Causa probable**: Drupal bloquea scripts inline por políticas de seguridad CSP (Content Security Policy).

**Impacto**: Solo visible en consola del navegador. **No afecta la experiencia del usuario**. Es un efecto secundario de no tener acceso al theme Drupal para configurar las políticas CSP correctamente.