import tkinter as tk
from tkinter import messagebox

class TareaApp:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Gestor de Tareas")
        self.ventana.geometry("400x400")

        # Campo de entrada para añadir nuevas tareas
        self.entrada_tarea = tk.Entry(ventana, width=40)
        self.entrada_tarea.pack(pady=10)
        self.entrada_tarea.focus()  # Coloca el cursor automáticamente en el campo

        # Botón para añadir tareas (también funciona con tecla Enter)
        self.boton_añadir = tk.Button(ventana, text="Añadir Tarea (Enter)", command=self.añadir_tarea)
        self.boton_añadir.pack(pady=5)

        # Lista visual para mostrar las tareas
        self.lista_tareas = tk.Listbox(ventana, selectmode=tk.SINGLE, width=50)
        self.lista_tareas.pack(pady=10)

        # Botón para marcar como completada (también funciona con tecla C)
        self.boton_completar = tk.Button(ventana, text="Marcar como Completada (C)", command=self.marcar_completada)
        self.boton_completar.pack(pady=5)

        # Botón para eliminar tarea (también funciona con tecla D)
        self.boton_eliminar = tk.Button(ventana, text="Eliminar Tarea (D)", command=self.eliminar_tarea)
        self.boton_eliminar.pack(pady=5)

        # Lista interna para almacenar las tareas con su estado (completada o no)
        self.tareas = []

        # Asignación de atajos de teclado
        self.ventana.bind('<Return>', lambda evento: self.añadir_tarea())      # Enter: añadir tarea
        self.ventana.bind('<c>', lambda evento: self.marcar_completada())      # C: marcar como completada
        self.ventana.bind('<d>', lambda evento: self.eliminar_tarea())         # D: eliminar tarea
        self.ventana.bind('<Escape>', lambda evento: self.ventana.quit())      # Escape: cerrar aplicación

    # Función para añadir una tarea a la lista
    def añadir_tarea(self):
        texto_tarea = self.entrada_tarea.get().strip()  # Elimina espacios al inicio/final
        if texto_tarea:  # Verifica que no esté vacía
            self.tareas.append({"texto": texto_tarea, "completada": False})  # Agrega a la lista
            self.actualizar_lista_tareas()
            self.entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    # Función para marcar/desmarcar como completada la tarea seleccionada
    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            # Cambia el estado de completada a su opuesto (toggle)
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para marcar como completada.")

    # Función para eliminar la tarea seleccionada
    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]  # Elimina la tarea de la lista
            self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")

    # Función para actualizar la lista visual de tareas en la interfaz
    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)  # Limpia la lista visual
        for tarea in self.tareas:
            texto_mostrar = tarea["texto"]
            if tarea["completada"]:
                texto_mostrar = "✔️ " + texto_mostrar  # Añade ícono si está completada
            self.lista_tareas.insert(tk.END, texto_mostrar)

# Bloque principal para crear la ventana y ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = TareaApp(ventana)
    ventana.mainloop()
