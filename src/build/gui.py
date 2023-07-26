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

def create_image(filename, x, y, canvas):
    image_image = PhotoImage(file=relative_to_assets(filename))
    photo_images.append(image_image)
    image = canvas.create_image(x, y, image=image_image)
    return image

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

photo_images = [] 

# ---------------IMAGENES---------------

# Main
BackGround = create_image("BackGround.png", 480.0, 300.0, canvas)
BtnBuscar = create_image("BtnBuscar.png", 267.0, 71.0, canvas) 
BtnBorrar = create_image("BtnBorrar.png", 814.0, 74.0, canvas) 
BtnAgregar = create_image("BtnAgregar.png", 104.0, 71.0, canvas) 
BtnActualizar = create_image("BtnActualizar.png", 651.0, 74.0, canvas) 

# Siempre en CRUD
PlaceholderTabla = create_image("PlaceholderTabla.png", 480.0, 416.0, canvas) 
PlaceHolderDropDownMenu = create_image("PlaceHolderDropDownMenu.png", 338.0,166.0, canvas) 

# Agregar
BtnAgregarTabla = create_image("BtnAgregarTabla.png", 587.0,170.0, canvas) 
TextosAgregarPaciente = create_image("TextoAgregar.png", 422.0,202.0, canvas) 

canvas.place(x = 0, y = 0)

window.resizable(False, False)
window.mainloop()
