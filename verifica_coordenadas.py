import tkinter as tk
import pyautogui

def atualizar_coordenadas():
    x, y = pyautogui.position()
    label.config(text=f"X: {x}, Y: {y}")
    root.after(10, atualizar_coordenadas)  # Atualiza a cada 10ms

# Criar a janela
root = tk.Tk()
root.title("Monitor de Coordenadas")
root.geometry("200x100")
root.resizable(False, False)

# Criar o rótulo para mostrar as coordenadas
label = tk.Label(root, text="X: 0, Y: 0", font=("Arial", 14))
label.pack(expand=True)

# Iniciar a atualização das coordenadas
atualizar_coordenadas()

# Executar a aplicação
root.mainloop()