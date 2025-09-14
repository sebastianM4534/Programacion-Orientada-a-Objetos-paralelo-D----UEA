#GUI BASICA
"""
GUI de ejemplo con Tkinter

Características implementadas:
- Ventana principal con título descriptivo.
- Componentes: etiquetas (Label), campo de texto (Entry), botones (Agregar, Limpiar) y una tabla (ttk.Treeview) para mostrar datos.
- Funcionalidad:
    - "Agregar": toma texto del campo y lo añade a la tabla con un ID incremental.
    - "Limpiar": si hay filas seleccionadas, las elimina; si no hay selección, limpia el campo de texto.
- Eventos:
    - Enter en el campo de texto -> agrega el elemento.
    - Supr (Delete) cuando hay selección -> elimina elementos seleccionados.
    - Doble clic en una fila -> carga su texto en el campo para editarlo (al agregar se guarda como nuevo registro).

Decisiones de diseño (breve):
- Uso de ttk.Treeview para mostrar los datos en formato tabular (ID + Información). Permite selección múltiple y scroll.
- Se mantiene un contador interno para generar IDs únicos y legibles.
- Se evitaron dependencias externas para que la aplicación funcione con Python estándar (3.7+).

El código está comentado y organizado en una clase "DataGUI" para facilitar la lectura y futura extensión.
"""

import tkinter as tk
from tkinter import ttk, messagebox


class DataGUI(tk.Tk):
    """Aplicación principal: ventana con controles para agregar/mostrar/limpiar datos."""

    def __init__(self):
        super().__init__()
        self.title("Gestor Visual de Datos")
        self.geometry("640x420")
        self.minsize(480, 320)
        self.configure(padx=12, pady=12)

        # Contador simple para generar ID numérico para cada fila añadida

        self._next_id = 1

        # Crear y posicionar widgets
        self._create_widgets()
        self._layout_widgets()
        self._bind_events()

    def _create_widgets(self):
        """Crear todos los widgets que usará la GUI."""

        # Frame de entrada

        self.input_frame = ttk.Frame(self)
        self.lbl_info = ttk.Label(self.input_frame, text="Información:")
        self.entry_info = ttk.Entry(self.input_frame)
        self.btn_add = ttk.Button(self.input_frame, text="Agregar", command=self.add_item)
        self.btn_clear = ttk.Button(self.input_frame, text="Limpiar", command=self.clear_action)

        # Frame de la tabla

        self.table_frame = ttk.Frame(self)

        # Treeview como tabla con dos columnas: ID e Información

        self.tree = ttk.Treeview(
            self.table_frame,
            columns=("ID", "Información"),
            show="headings",
            selectmode="extended",
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Información", text="Información")
        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Información", anchor="w")

        # Scrollbar vertical para la tabla

        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Label de estado en el pie

        self.status = ttk.Label(self, text="Listo", anchor="w")

    def _layout_widgets(self):
        """Organizar widgets en la ventana (usamos grid para control fino)."""

        # Frame de entrada en la parte superior

        self.input_frame.grid(row=0, column=0, sticky="ew")
        self.input_frame.columnconfigure(1, weight=1)

        self.lbl_info.grid(row=0, column=0, padx=(0, 8), pady=4)
        self.entry_info.grid(row=0, column=1, sticky="ew", pady=4)
        self.btn_add.grid(row=0, column=2, padx=6)
        self.btn_clear.grid(row=0, column=3)

        # Frame de tabla en el medio

        self.table_frame.grid(row=1, column=0, sticky="nsew", pady=(8, 0))
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.table_frame.columnconfigure(0, weight=1)
        self.scrollbar.grid(row=0, column=1, sticky="ns", padx=(4, 0))

        # Label de estado al final

        self.status.grid(row=2, column=0, sticky="ew", pady=(8, 0))

    def _bind_events(self):
        """Vincular eventos de teclado y mouse a funciones."""
        # Enter en el entry agrega el elemento
        self.entry_info.bind("<Return>", lambda e: self.add_item())
        # Tecla Delete elimina los elementos seleccionados
        self.tree.bind("<Delete>", lambda e: self._delete_selected())
        # Doble clic en una fila permite editar su texto cargándolo en el entry
        self.tree.bind("<Double-1>", lambda e: self._on_double_click(e))

    def add_item(self):
        """Agregar el texto del campo entrada a la tabla con un ID incremental."""
        text = self.entry_info.get().strip()
        if not text:
            messagebox.showwarning("Entrada vacía", "Por favor ingresa algo antes de agregar.")
            return

        item_id = f"{self._next_id}"

        # Insertar como nuevo elemento en el Treeview

        self.tree.insert("", "end", iid=item_id, values=(self._next_id, text))
        self._next_id += 1

        # Limpiar campo y actualizar estado

        self.entry_info.delete(0, tk.END)
        self.status.config(text=f"Agregado ID {item_id}")

    def clear_action(self):
        """Si hay selección en la tabla, eliminar los elementos seleccionados.
        Si no hay selección, limpiar el campo de entrada.
        Esto satisface el requisito: el botón 'Limpiar' borra lo ingresado o lo seleccionado.
        """
        selected = self.tree.selection()
        if selected:
            for iid in selected:
                self.tree.delete(iid)
            self.status.config(text=f"Eliminado {len(selected)} elemento(s).")
        else:
            if self.entry_info.get():
                self.entry_info.delete(0, tk.END)
                self.status.config(text="Campo de entrada limpiado.")
            else:
                self.status.config(text="Nada que limpiar.")

    def _delete_selected(self):
        """Helper para enlazar la tecla Supr al borrado de selección."""
        self.clear_action()

    def _on_double_click(self, event):
        """Al hacer doble clic en una fila, cargamos su texto en el Entry para poder editarlo.
        Eliminamos la fila original; al presionar 'Agregar' se insertará como un registro "nuevo".
        Esto es una forma sencilla de permitir edición sin crear una UI de edición completa.
        """
        item = self.tree.identify_row(event.y)
        if not item:
            return
        values = self.tree.item(item, "values")
        if not values:
            return

        # Cargar en el campo de entrada

        self.entry_info.delete(0, tk.END)
        self.entry_info.insert(0, values[1])

        # Borrar la fila antigua para evitar duplicados al re-agregar

        self.tree.delete(item)
        self.status.config(text=f"Editando ID {values[0]} (agrega para guardar).")


if __name__ == "__main__":
    app = DataGUI()
    app.mainloop()
