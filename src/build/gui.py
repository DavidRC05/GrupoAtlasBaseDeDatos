#Imports
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#Para rutas relativas
OUTPUT_PATH = Path(__file__).parent

#Esta ruta hay que cambiarla por cada compu
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Arturo\Desktop\GeneratedCode\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Creacion de la ventana
window = Tk()
window.geometry("960x600")
window.configure(bg = "#F9F9F9")

#Canvas para juntarle imagenes
canvas = Canvas(
    window,
    bg = "#F9F9F9",
    height = 600,
    width = 960,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

window.resizable(False, False)
window.mainloop()
