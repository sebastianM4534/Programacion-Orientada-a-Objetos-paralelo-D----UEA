
#GUI de lista de Tareas

import tkinter as tk
from tkinter import messagebox


class TodoApp:
    #Clase principal de la aplicación.

    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Gestor de Tareas - Tkinter")
        root.geometry("420x480")
        root.resizable(False, False)

        # Estado de la aplicación: lista de tareas
        self.tasks = []

        # Zona de entrada (Entry) y boton "Añadir"
        entry_frame = tk.Frame(root)
        entry_frame.pack(padx=12, pady=12, fill='x')

        self.entry = tk.Entry(entry_frame, font=("Helvetica", 12))
        self.entry.pack(side='left', fill='x', expand=True)

        # Permitir añadir tarea pulsando Enter
        self.entry.bind('<Return>', self.on_enter_pressed)

        add_btn = tk.Button(entry_frame, text="Añadir Tarea", command=self.add_task)
        add_btn.pack(side='left', padx=(8, 0))

        # Listbox para mostrar tareas con scrollbar
        list_frame = tk.Frame(root)
        list_frame.pack(padx=12, pady=(0, 12), fill='both', expand=True)

        self.listbox = tk.Listbox(
            list_frame,
            font=("Helvetica", 12),
            activestyle='none',
            selectmode=tk.SINGLE,
            exportselection=False,
        )
        self.listbox.pack(side='left', fill='both', expand=True)

        # Doble clic en un elemento alterna su estado (completado/no completado)
        self.listbox.bind('<Double-Button-1>', self.on_double_click)

        # Pulsar Supr (Delete) borra la tarea seleccionada
        self.listbox.bind('<Delete>', lambda e: self.delete_task())

        scrollbar = tk.Scrollbar(list_frame, orient='vertical', command=self.listbox.yview)
        scrollbar.pack(side='right', fill='y')
        self.listbox.config(yscrollcommand=scrollbar.set)

        #Botones inferiores: Marcar / Eliminar
        btn_frame = tk.Frame(root)
        btn_frame.pack(padx=12, pady=(0, 12), fill='x')

        mark_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.toggle_completed)
        mark_btn.pack(side='left', expand=True, fill='x', padx=(0, 6))

        del_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        del_btn.pack(side='left', expand=True, fill='x', padx=(6, 0))

        # Atajos de teclado útiles
        root.bind('<Control-n>', lambda e: self.entry.focus_set())
        root.bind('<Control-d>', lambda e: self.delete_task())


    #Manejo de eventos
    def on_enter_pressed(self, event):
        self.add_task()
    def on_double_click(self, event):

        # Llamamos al toggle_completed que usa el índice seleccionado
        self.toggle_completed()

    def add_task(self, text: str = None):

        if text is None:
            text = self.entry.get().strip()
        else:
            text = text.strip()

        if not text:
            messagebox.showwarning('Entrada vacía', 'Escribe una tarea antes de añadirla.')
            return

        self.tasks.append({'text': text, 'completed': False})
        self.entry.delete(0, tk.END)
        self.refresh_listbox()

        # Seleccionar y hacer scroll hasta la última tarea añadida
        last_index = len(self.tasks) - 1
        if last_index >= 0:
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(last_index)
            self.listbox.see(last_index)

    def refresh_listbox(self):

        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            display = task['text']
            if task['completed']:
                display = '✓ ' + display
            self.listbox.insert(tk.END, display)

        # Intento de estilizar (gris) las tareas completadas
        for i, task in enumerate(self.tasks):
            if task['completed']:
                try:
                    self.listbox.itemconfig(i, fg='gray')
                except Exception:
                    # Si la plataforma no soporta itemconfig para Listbox, ignoramos.
                    pass

    def get_selected_index(self):
        sel = self.listbox.curselection()
        if not sel:
            return None
        return sel[0]

    def toggle_completed(self):
        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo('Sin selección', 'Selecciona una tarea para marcarla/desmarcarla.')
            return

        # Alternar y actualizar vista
        self.tasks[idx]['completed'] = not self.tasks[idx]['completed']
        self.refresh_listbox()

        # Mantener la selección en el mismo índice (si existe)
        if idx < len(self.tasks):
            self.listbox.selection_set(idx)

    def delete_task(self):

        idx = self.get_selected_index()
        if idx is None:
            messagebox.showinfo('Sin selección', 'Selecciona una tarea para eliminar.')
            return

        task_text = self.tasks[idx]['text']
        if not messagebox.askyesno('Confirmar eliminación', f"¿Eliminar la tarea?\n\n{task_text}"):
            return

        del self.tasks[idx]
        self.refresh_listbox()


# Punto de entrada
if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
