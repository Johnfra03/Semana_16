import tkinter as tk
from tkinter import messagebox

class TareaApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de Tareas")
        self.ventana.geometry("400x400")

        self.entrada_tarea = tk.Entry(ventana, width=40)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.focus()

        self.boton_añadir = tk.Button(ventana, text="Añadir Tarea", command=self.añadir_tarea)
        self.boton_añadir.pack(pady=5)

        self.lista_tareas = tk.Listbox(ventana, selectmode=tk.SINGLE, width=50)
        self.lista_tareas.pack(pady=10)

        self.boton_completar = tk.Button(ventana, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        self.boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Lista para almacenar tareas y su estado
        self.tareas = []

        # Asignar atajos de teclado
        self.ventana.bind('<Return>', lambda evento: self.añadir_tarea())
        self.ventana.bind('<c>', lambda evento: self.marcar_completada())
        self.ventana.bind('<C>', lambda evento: self.marcar_completada())
        self.ventana.bind('<d>', lambda evento: self.eliminar_tarea())
        self.ventana.bind('<D>', lambda evento: self.eliminar_tarea())
        self.ventana.bind('<Escape>', lambda evento: self.ventana.quit())

    def añadir_tarea(self):
        texto_tarea = self.entrada_tarea.get().strip()
        if texto_tarea:
            self.tareas.append({"texto": texto_tarea, "completada": False})
            self.actualizar_lista_tareas()
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto_mostrar = tarea["texto"]
            if tarea["completada"]:
                texto_mostrar = "✔️ " + texto_mostrar
            self.lista_tareas.insert(tk.END, texto_mostrar)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = TareaApp(ventana)
    ventana.mainloop()
