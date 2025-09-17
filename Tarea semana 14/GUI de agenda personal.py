# agenda de eventso personal
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import uuid

# Intentamos importar DateEntry desde tkcalendar. Si no está instalado, se avisará al usuario.

try:
    from tkcalendar import DateEntry
except Exception as e:
    DateEntry = None


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x450")
        self.root.resizable(False, False)

        # Lista interna de eventos (diccionario con id -> evento)

        self.events = {}

        # Frames para organizar la interfaz

        # Frame superior: lista de eventos

        self.frame_list = ttk.Frame(self.root, padding=(10, 8))
        self.frame_list.pack(fill=tk.BOTH, expand=True)

        # Frame inferior: entradas y botones

        self.frame_inputs = ttk.Frame(self.root, padding=(10, 8))
        self.frame_inputs.pack(fill=tk.X)

        # Subframes dentro de frame_inputs para separar entradas y botones

        self.frame_fields = ttk.Frame(self.frame_inputs)
        self.frame_fields.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.frame_actions = ttk.Frame(self.frame_inputs)
        self.frame_actions.pack(side=tk.RIGHT)

        # Treeview para mostrar eventos

        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(self.frame_list, columns=columns, show="headings", height=12)
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=120, anchor=tk.CENTER)
        self.tree.column("hora", width=80, anchor=tk.CENTER)
        self.tree.column("descripcion", width=420, anchor=tk.W)

        # Scrollbar vertical

        vsb = ttk.Scrollbar(self.frame_list, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        # Configure grid weight

        self.frame_list.columnconfigure(0, weight=1)
        self.frame_list.rowconfigure(0, weight=1)

        #  Campos de entrada

        # Fecha: si tkcalendar está disponible usamos DateEntry, si no usamos Entry simple con formato YYYY-MM-DD

        lbl_fecha = ttk.Label(self.frame_fields, text="Fecha (YYYY-MM-DD):")
        lbl_fecha.grid(row=0, column=0, padx=5, pady=4, sticky=tk.W)

        if DateEntry is not None:
            self.entry_fecha = DateEntry(self.frame_fields, date_pattern='yyyy-mm-dd')
        else:
            self.entry_fecha = ttk.Entry(self.frame_fields)
            self.entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.entry_fecha.grid(row=0, column=1, padx=5, pady=4, sticky=tk.W)

        lbl_hora = ttk.Label(self.frame_fields, text="Hora (HH:MM):")
        lbl_hora.grid(row=1, column=0, padx=5, pady=4, sticky=tk.W)
        self.entry_hora = ttk.Entry(self.frame_fields)
        self.entry_hora.insert(0, "09:00")
        self.entry_hora.grid(row=1, column=1, padx=5, pady=4, sticky=tk.W)

        lbl_desc = ttk.Label(self.frame_fields, text="Descripción:")
        lbl_desc.grid(row=2, column=0, padx=5, pady=4, sticky=tk.NW)
        self.txt_desc = tk.Text(self.frame_fields, width=40, height=4)
        self.txt_desc.grid(row=2, column=1, padx=5, pady=4, sticky=tk.W)

        # Botones de acción

        self.btn_add = ttk.Button(self.frame_actions, text="Agregar Evento", command=self.add_event)
        self.btn_add.pack(fill=tk.X, pady=(8, 4))

        self.btn_delete = ttk.Button(self.frame_actions, text="Eliminar Evento Seleccionado", command=self.delete_selected)
        self.btn_delete.pack(fill=tk.X, pady=4)

        self.btn_exit = ttk.Button(self.frame_actions, text="Salir", command=self.root.quit)
        self.btn_exit.pack(fill=tk.X, pady=4)

        # Bind doble click en Treeview para ver detalles (opcional)

        self.tree.bind('<Double-1>', self.on_tree_double_click)

    def add_event(self):
        """Agregar un evento a la lista: validar entradas, crear un id único, actualizar Treeview y estructura interna."""
        fecha_str = self.entry_fecha.get().strip()
        hora_str = self.entry_hora.get().strip()
        descripcion = self.txt_desc.get("1.0", tk.END).strip()

        # Validaciones básicas

        if not fecha_str:
            messagebox.showwarning("Entrada inválida", "Por favor ingrese una fecha.")
            return
        if not hora_str:
            messagebox.showwarning("Entrada inválida", "Por favor ingrese una hora.")
            return
        if not descripcion:
            messagebox.showwarning("Entrada inválida", "Por favor ingrese una descripción.")
            return

        # Validar formato de fecha y hora

        try:
            # Fecha en formato YYYY-MM-DD

            fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Formato de fecha inválido", "La fecha debe estar en formato YYYY-MM-DD.")
            return

        try:
            hora_obj = datetime.strptime(hora_str, "%H:%M")
        except ValueError:
            messagebox.showerror("Formato de hora inválido", "La hora debe estar en formato HH:MM (24 horas).")
            return

        # Crear ID único para el evento

        event_id = str(uuid.uuid4())

        # Guardar en estructura interna

        self.events[event_id] = {
            "fecha": fecha_obj.strftime("%Y-%m-%d"),
            "hora": hora_obj.strftime("%H:%M"),
            "descripcion": descripcion
        }

        # Insertar en Treeview (usamos el event_id como iid para facilitar eliminacion)

        self.tree.insert("", tk.END, iid=event_id, values=(self.events[event_id]["fecha"],
                                                           self.events[event_id]["hora"],
                                                           self.events[event_id]["descripcion"]))

        # Limpiar entradas

        if DateEntry is None:
            # si usamos Entry para la fecha dejamos la fecha actual
            self.entry_fecha.delete(0, tk.END)
            self.entry_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_hora.delete(0, tk.END)
        self.entry_hora.insert(0, "09:00")
        self.txt_desc.delete("1.0", tk.END)

    def delete_selected(self):
        """Eliminar el evento seleccionado en el Treeview, con confirmación"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("Eliminar evento", "No hay ningún evento seleccionado.")
            return

        # Preguntar confirmación (si se seleccionaron varios, preguntar para todos)

        if len(selected) == 1:
            msg = "¿Eliminar el evento seleccionado?"
        else:
            msg = f"¿Eliminar los {len(selected)} eventos seleccionados?"

        if not messagebox.askyesno("Confirmar eliminación", msg):
            return

        for iid in selected:

            # Quitar de estructura interna si existe

            if iid in self.events:
                del self.events[iid]

            # Quitar del Treeview

            try:
                self.tree.delete(iid)
            except Exception:
                pass

    def on_tree_double_click(self, event):
        """Mostrar un diálogo con los detalles del evento al hacer doble clic"""
        item = self.tree.identify_row(event.y)
        if not item:
            return
        ev = self.events.get(item)
        if not ev:
            return
        detalle = f"Fecha: {ev['fecha']}\nHora: {ev['hora']}\n\n{ev['descripcion']}"
        messagebox.showinfo("Detalle del evento", detalle)


if __name__ == '__main__':
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
