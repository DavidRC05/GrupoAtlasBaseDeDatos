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

canvas.place(x = 0, y = 0)

window.resizable(False, False)
window.mainloop()
