import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("500x400")

        # Entrada de texto para nuevas tareas
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=10)
        self.task_entry.focus()

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)

        complete_btn = tk.Button(btn_frame, text="Marcar Completada", command=self.complete_task)
        complete_btn.grid(row=0, column=1, padx=5)

        delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Diccionario para controlar estado de tareas
        self.tasks = {}

        # Asignar atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<C>", lambda event: self.complete_task())  # Por si se usa Shift
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            index = self.task_listbox.size()
            self.task_listbox.insert(tk.END, task_text)
            self.tasks[index] = {"text": task_text, "completed": False}
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            if not self.tasks[index]["completed"]:
                self.tasks[index]["completed"] = True
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✔ {self.tasks[index]['text']}")
                self.task_listbox.itemconfig(index, fg="gray", selectforeground="black")
            else:
                messagebox.showinfo("Info", "La tarea ya está completada.")
        else:
            messagebox.showwarning("Atención", "Selecciona una tarea para completar.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_listbox.delete(index)
            del self.tasks[index]

            # Reorganizar índices del diccionario
            self.tasks = {i: v for i, v in enumerate(self.tasks.values())}
        else:
            messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
