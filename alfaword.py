import os
from PySide6.QtWidgets import QMainWindow,QLineEdit ,QToolBar,QDockWidget  ,QWidget, QApplication,QLabel,QComboBox ,QInputDialog ,QTextEdit, QMessageBox, QFileDialog,QStatusBar,QHBoxLayout,QScrollArea,QPushButton,QVBoxLayout,QStyleFactory
from PySide6.QtGui import QAction, QIcon, QKeySequence, QTextCursor,QFont,QFontDatabase,QColor,QPalette,QTextDocument,QTextCharFormat
from PySide6.QtCore import Qt, QSize


class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.widgets_base()
        self.qwidget()
        self.menubar()


    def configurar_ventana(self):    
        self.setWindowTitle("Mini Word")
        self.setWindowIcon(QIcon("iconoDEF.png"))

       
        

    def widgets_base(self):
        self.texto = QTextEdit()
       
        contenedor = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.texto, alignment=Qt.AlignHCenter | Qt.AlignTop)
        contenedor.setLayout(layout)

        scroll = QScrollArea()
        scroll.setWidget(contenedor)
        scroll.setWidgetResizable(True)
        scroll.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(scroll)

        self.barra_status= QStatusBar()
        self.setStatusBar(self.barra_status)

    def qwidget(self):
        dock = QDockWidget()
        dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
        dock.setTitleBarWidget(QWidget())
        self.addDockWidget(Qt.TopDockWidgetArea,dock)

        
        #botoncursiva
        
        icono_cursiva= os.path.join(os.path.dirname(
            __file__), "italic.png")
        self.cursiva_icono = QIcon(icono_cursiva)  
        self.cursiva_boton = QPushButton(self)
        self.cursiva_boton.setFixedSize(25,25)
        self.cursiva_boton.setIcon(self.cursiva_icono)
        self.cursiva_boton.setIconSize(QSize(16, 16))
        self.cursiva_boton.clicked.connect(self.alternar_cursiva)
        self.cursiva_boton.setCheckable(True)

        #botonnegrita
        icono_negrita= os.path.join(os.path.dirname(
            __file__), "negrita.png")
        self.negrita_icono = QIcon(icono_negrita) 
        self.negrita_boton = QPushButton(self)
        self.negrita_boton.setFixedSize(25, 25)
        self.negrita_boton.setIcon(self.negrita_icono)
        self.negrita_boton.setIconSize(QSize(16, 16))
        self.negrita_boton.clicked.connect(self.alternar_negrita)
        self.negrita_boton.setCheckable(True)

        

        contenedor_dock = QWidget()

        layout_dock = QHBoxLayout() #contenedor horizontal
        layout_dock.setContentsMargins(0, 2, 0, 2)
        layout_dock.setSpacing(2) 
        layout_dock.addWidget(self.cursiva_boton)
        layout_dock.addWidget(self.negrita_boton)
       


        contenedor_botones = QWidget() 
        contenedor_botones.setLayout(layout_dock)


        layout_externo = QVBoxLayout() 
        layout_externo.setContentsMargins(0, 0, 0, 0)
        layout_externo.addWidget(contenedor_botones, alignment=Qt.AlignHCenter)

        contenedor_dock = QWidget()
        contenedor_dock.setLayout(layout_externo)
        dock.setWidget(contenedor_dock)
        
    
        self.combobox_fuentes = QComboBox(self)
        self.combobox_fuentes.setFixedSize(150, 24)
        self.combobox_fuentes.setPlaceholderText("Tipo de fuente")

        fuentes_disponibles = QFontDatabase.families()
        self.combobox_fuentes.addItems(fuentes_disponibles)
        self.combobox_fuentes.textActivated.connect(self.cambiar_fuente)
        layout_dock.addWidget(self.combobox_fuentes)

    
        self.combobox_tamanio = QComboBox(self)
        self.combobox_tamanio.setFixedSize(150, 24)
        self.combobox_tamanio.setPlaceholderText("Tamaño fuentes")
        
        tam_list = ["8","9","10","11","12","14","16","18","20","22","24","26","28","36","48","72"]
        self.combobox_tamanio.addItems(tam_list)
        self.combobox_tamanio.setEditable(True)           
        self.combobox_tamanio.setCurrentText("12")

        self.combobox_tamanio.currentTextChanged.connect(self.on_combobox_tamanio_changed)
        layout_dock.addWidget(self.combobox_tamanio)
        



        self.combobox_color = QComboBox(self)
        self.combobox_color.setFixedSize(150, 24)
        self.combobox_color.setPlaceholderText("Color fuente")

        self.fondo_color = QComboBox(self)
        self.fondo_color.setFixedSize(150, 24)
        self.fondo_color.setPlaceholderText("Fondo")


        self.color_disponibles = {
            "Negro": "black",
            "Rojo": "red",
            "Verde": "green",
            "Azul": "blue",
            "Naranja": "orange",
            "Morado": "purple",
            "Gris": "gray",
            "Blanco":"white"

        }




        self.fondo_color.addItems(self.color_disponibles.keys())   
        self.fondo_color.textActivated.connect(self.cambiar_color_fondo)
        layout_dock.addWidget(self.fondo_color)

        self.combobox_color.addItems(self.color_disponibles.keys())   
        self.combobox_color.textActivated.connect(self.cambiar_color_texto)
        layout_dock.addWidget(self.combobox_color)
        
        self.contador_label = QLabel("Palabras: 0")
        self.barra_status.addPermanentWidget(self.contador_label)  
        self.texto.textChanged.connect(self.actualizar_contador_palabras)

        self.dock_busqueda = QDockWidget("Buscar y reemplazar",self)
        self.dock_busqueda.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dock_busqueda.setFeatures(QDockWidget.DockWidgetClosable)

        widget_busqueda = QWidget()
        layout_busqueda = QVBoxLayout()

        self.input_buscar = QLineEdit()
        self.input_buscar.setPlaceholderText("Texto a buscar")

        self.input_reemplazar = QLineEdit()
        self.input_reemplazar.setPlaceholderText("Reemplazar por...")

        btn_siguiente = QPushButton("Buscar siguiente")
        btn_atras = QPushButton("Buscar anterior")
        btn_todo = QPushButton("Buscar todo")
        btn_reemplazar = QPushButton("Reemplazar")
        btn_reemplazar_todo = QPushButton("Reemplazar todo")

        btn_siguiente.clicked.connect(self.buscar_siguiente)
        btn_atras.clicked.connect(self.buscar_atras)
        btn_todo.clicked.connect(self.buscar_todo)
        btn_reemplazar.clicked.connect(self.reemplazar_uno)
        btn_reemplazar_todo.clicked.connect(self.reemplazar_todo)

        layout_busqueda.addWidget(self.input_buscar)
        layout_busqueda.addWidget(self.input_reemplazar)

        layout_busqueda.addWidget(btn_siguiente)
        layout_busqueda.addWidget(btn_atras)
        layout_busqueda.addWidget(btn_todo)
        layout_busqueda.addWidget(btn_reemplazar)
        layout_busqueda.addWidget(btn_reemplazar_todo)

        widget_busqueda.setLayout(layout_busqueda)
        self.dock_busqueda.setWidget(widget_busqueda)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_busqueda)

        self.dock_busqueda.hide()






    def menubar(self):

        barra_menus = self.menuBar()
        menu_archivo = barra_menus.addMenu("&Archivo")
        menu_editar = barra_menus.addMenu("&Editar")

        icono_nuevo= os.path.join(os.path.dirname(
            __file__), "nuevo.png")
        icono_abrir= os.path.join(os.path.dirname(
            __file__), "abrir.png")
        icono_guardar= os.path.join(os.path.dirname(
            __file__), "guardar.png")
        icono_deshacer= os.path.join(os.path.dirname(
            __file__), "deshacer.png")
        icono_rehacer= os.path.join(os.path.dirname(
            __file__), "rehacer.png")
        icono_cortar= os.path.join(os.path.dirname(
            __file__), "cortar.png")
        icono_copiar= os.path.join(os.path.dirname(
            __file__), "copiar.png")
        icono_pegar= os.path.join(os.path.dirname(
            __file__), "pegar.png")
        icono_buscar= os.path.join(os.path.dirname(
            __file__), "buscar.png")
        icono_reemplazar= os.path.join(os.path.dirname(
            __file__), "reemplazar.png")
        icono_salir= os.path.join(os.path.dirname(
            __file__), "salir.png")
        
        nuevo = QAction(QIcon(icono_nuevo), "Nuevo", self)
        abrir = QAction(QIcon(icono_abrir), "Abrir", self)
        guardar = QAction(QIcon(icono_guardar), "Guardar", self)
        deshacer = QAction(QIcon(icono_deshacer), "Deshacer", self)
        rehacer = QAction(QIcon(icono_rehacer), "Rehacer", self)
        copiar = QAction(QIcon(icono_copiar), "Copiar", self)
        cortar = QAction(QIcon(icono_cortar), "Cortar", self)
        pegar = QAction(QIcon(icono_pegar), "Pegar", self)
        buscar = QAction(QIcon(icono_buscar), "Buscar", self)
        reemplazar = QAction(QIcon(icono_reemplazar), "Reemplazar", self)
        salir = QAction(QIcon(icono_salir),"Salir",self)


        barra_herramientas = QToolBar("Barra de herramientas 1")
        barra_herramientas.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra_herramientas)

        menu_archivo.addAction(nuevo)
        menu_archivo.addAction(abrir)
        menu_archivo.addAction(guardar)
        menu_archivo.addAction(salir)

        menu_editar.addActions([deshacer, rehacer, cortar, copiar, pegar, buscar, reemplazar])

        barra_herramientas.addActions([
            nuevo, abrir, guardar,
            deshacer, rehacer,
            cortar, copiar, pegar,
            buscar, reemplazar
        ])

        
        nuevo.setWhatsThis(
            "Crear nuevo documento")
        nuevo.setShortcut(QKeySequence("Ctrl+n"))
        nuevo.triggered.connect(self.crear_nuevo)

        abrir.setWhatsThis(
            "Abrir nuevo documento")
        abrir.setShortcut(QKeySequence("Ctrl+o"))
        abrir.triggered.connect(self.abrir_archivo)

        guardar.setWhatsThis(
            "Guardar nuevo documento")
        guardar.setShortcut(QKeySequence("Ctrl+s"))
        guardar.triggered.connect(self.guardar_archivo)

        deshacer.setWhatsThis(
            "Abrir nuevo documento")
        deshacer.setShortcut(QKeySequence("Ctrl+z"))
        deshacer.triggered.connect(self.texto_deshacer)

        rehacer.setWhatsThis(
            "Abrir nuevo documento")
        rehacer.setShortcut(QKeySequence("Ctrl+r"))
        rehacer.triggered.connect(self.texto_rehacer)    

        cortar.setWhatsThis(
            "Abrir nuevo documento")
        cortar.setShortcut(QKeySequence("Ctrl+x"))
        cortar.triggered.connect(self.texto_cortar)

        copiar.setWhatsThis(
            "Abrir nuevo documento")
        copiar.setShortcut(QKeySequence("Ctrl+c"))
        copiar.triggered.connect(self.texto_copiar)

        pegar.setWhatsThis(
            "Abrir nuevo documento")
        pegar.setShortcut(QKeySequence("Ctrl+v"))
        pegar.triggered.connect(self.texto_pegar)

        buscar.setWhatsThis(
            "Abrir nuevo documento")
        buscar.setShortcut(QKeySequence("Ctrl+f"))
        buscar.triggered.connect(self.dock_busqueda.show)

        reemplazar.setWhatsThis(
            "Abrir nuevo documento")
        reemplazar.setShortcut(QKeySequence("Ctrl+y"))
        reemplazar.triggered.connect(self.dock_busqueda.show)

        salir.setWhatsThis(
            "Abrir nuevo documento")
        salir.setShortcut(QKeySequence("Alt+F4"))
        salir.triggered.connect(self.salir_programa)
    




    #funciones TOOLBAR/MENUBAR    
    def crear_nuevo(self):
        print("Nuevo documento abierto")
        self.texto.clear()
        self.barra_status.showMessage("Nuevo documento abierto", 3000)

    def abrir_archivo(self):
        nombre, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Texto (*.txt)")
        if nombre:
            with open(nombre, "r", encoding="utf-8") as f:
                self.texto.setPlainText(f.read())
                self.barra_status.showMessage("Archivo abierto con éxito", 3000)   

    def guardar_archivo(self):
        nombre, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Texto (*.txt)")
        if nombre:
            with open(nombre, "w", encoding="utf-8") as f:
                f.write(self.texto.toPlainText())
            QMessageBox.information(self, "Mini Word", "Archivo guardado correctamente")
            self.barra_status.showMessage("Archivo guardado con éxito", 3000)

    def buscar_texto(self):
        texto, ok = QInputDialog.getText(self, "Buscar", "Texto a buscar:")
        if ok and texto:
       
            cursor = self.texto.textCursor()
            cursor.movePosition(QTextCursor.Start)   # <-- aquí
            self.texto.setTextCursor(cursor)
            self.barra_status.showMessage("Archivo encontrado con éxito", 3000)

        
            if not self.texto.find(texto):
                self.barra_status.showMessage("Fallo al buscar", 3000)

    def on_combobox_tamanio_changed(self):
        texto = self.combobox_tamanio.currentText().strip()
        if not texto:
            return
        try:
            puntos = float(texto)
        except ValueError:
            return

        fmt = QTextCharFormat()
        fmt.setFontPointSize(puntos)

        tc = self.texto.textCursor()
        if tc.hasSelection():
            # aplicar al texto seleccionado
            tc.mergeCharFormat(fmt)
            self.texto.mergeCurrentCharFormat(fmt)
        else:
            # aplicar al formato activo (lo que se escriba a continuación)
            self.texto.mergeCurrentCharFormat(fmt)

    def buscar_siguiente(self):
        texto = self.input_buscar.text()
        if not texto:
            return

        doc = self.texto.document()
        cursor = self.texto.textCursor()
        flags = QTextDocument.FindFlag.FindCaseSensitively

        resultado = doc.find(texto, cursor, flags)
        if resultado.isNull():
            start = QTextCursor(doc)
            start.movePosition(QTextCursor.MoveOperation.Start)
            resultado = doc.find(texto, start, flags)

        if resultado.isNull():
            self.barra_status.showMessage("No encontrado", 2000)
            return

        self.texto.setTextCursor(resultado)


    def buscar_atras(self):
        texto = self.input_buscar.text()
        if not texto:
            return

        doc = self.texto.document()
        cursor = self.texto.textCursor()
        flags = QTextDocument.FindFlag.FindBackward | QTextDocument.FindFlag.FindCaseSensitively

        resultado = doc.find(texto, cursor, flags)
        if resultado.isNull():
            end = QTextCursor(doc)
            end.movePosition(QTextCursor.MoveOperation.End)
            resultado = doc.find(texto, end, flags)

        if resultado.isNull():
            self.barra_status.showMessage("No encontrado", 2000)
            return

        self.texto.setTextCursor(resultado)


    def buscar_todo(self):
        texto_total = self.texto.toPlainText()
        buscar = self.input_buscar.text()

        if not buscar:
            return

        count = texto_total.count(buscar)
        self.barra_status.showMessage(f"{count} coincidencias", 3000)

    def reemplazar_uno(self):
        buscar = self.input_buscar.text()
        reemplazar = self.input_reemplazar.text()

        cursor = self.texto.textCursor()

        if cursor.selectedText().lower() == buscar.lower():
            cursor.insertText(reemplazar)
            self.barra_status.showMessage("Reemplazado", 2000)

        self.buscar_siguiente()


    def reemplazar_todo(self):
        buscar = self.input_buscar.text()
        reemplazar = self.input_reemplazar.text()
        if not buscar:
            return

        doc = self.texto.document()
        flags = QTextDocument.FindFlag.FindCaseSensitively  

        # empezar desde el inicio
        cur = QTextCursor(doc)
        cur.movePosition(QTextCursor.MoveOperation.Start)

        # buscar y reemplazar en bucle
        encontrado = doc.find(buscar, cur, flags)
        while not encontrado.isNull():

            self.texto.setTextCursor(encontrado)

            tc = self.texto.textCursor()

            tc.insertText(reemplazar)
            # continuar búsqueda desde la posición actual (después del texto insertado)
            encontrado = doc.find(buscar, self.texto.textCursor(), flags)

        self.barra_status.showMessage("Reemplazo completo", 3000)

    def salir_programa(self):
        respuesta = QMessageBox.question(
            self,
            "Salir",
            "¿Seguro que quieres cerrar el programa?",
            QMessageBox.Yes | QMessageBox.No
                )
        if respuesta == QMessageBox.Yes:
            self.close()  

    def texto_deshacer(self):
        self.texto.undo()
        self.barra_status.showMessage("Texto deshecho con éxito", 3000)

    def texto_rehacer(self):
        self.texto.redo()
        self.barra_status.showMessage("Texto rehecho con éxito", 3000)

    def texto_copiar(self):
        self.texto.copy()
        self.barra_status.showMessage("Texto copiado con éxito", 3000)

    def texto_cortar(self):
        self.texto.cut()
        self.barra_status.showMessage("Texto cortado con éxito", 3000)

    def texto_pegar(self):
        self.texto.paste()
        self.barra_status.showMessage("Texto pegado con éxito", 3000)


    #botones del dock
    def alternar_cursiva(self):
        actual = self.texto.fontItalic()
        self.texto.setFontItalic(not actual)

    def alternar_negrita(self):
        actual = self.texto.fontWeight() > QFont.Normal
        self.texto.setFontWeight(QFont.Normal if actual else QFont.Bold)

    def cambiar_fuente(self, fuente):
        fuente_actual = self.texto.font()
        fuente_actual.setFamily(fuente)
        self.texto.setFont(fuente_actual)

    def cambiar_color_texto(self, color_nombre): 
        color_valor = self.color_disponibles[color_nombre]
        self.texto.setTextColor(QColor(color_valor))

    def cambiar_color_fondo(self, color_nombre): 
        color_valor = self.color_disponibles[color_nombre]
        self.texto.setStyleSheet(f"background-color: {color_valor};")
    
    def actualizar_contador_palabras(self):
        texto = self.texto.toPlainText()
        num_palabras = len(texto.split())
        self.contador_label.setText(f"Palabras: {num_palabras}")   


    #responsive?
    def resizeEvent(self, event):
        ancho = self.width() * 0.6
        alto = ancho * 1.414  # proporción A4
        self.texto.setFixedSize(ancho, alto)
        super().resizeEvent(event)

    




if __name__ == "__main__": #declarar el main
    app = QApplication([]) #se quede escuchando
    app.setStyle(QStyleFactory.create("Fusion")) 
    
    ventana = VentanaPrincipal() #crea un objeto de la clase de arriba
    ventana.show() #muestra el objeto ventana
    app.exec() #inicia bucle evento que escucha
    
    

