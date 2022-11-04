import tkinter
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk


root_tk = tkinter.Tk()
root_tk.geometry(f"{600}x{400}")
root_tk.title("map_view_simple_example.py")

# create map widget
map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# google normal tile server
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

map_widget.set_position(13.014493, 77.634619)
map_widget.set_zoom(15)
map_widget.set_address("Kamanahalli, Bangalore", marker=True)

pothole1 = ImageTk.PhotoImage(Image.open('pothole1.jpg').resize((320, 200)))
marker_1 = map_widget.set_marker(13.014605, 77.634809, text="pothole", image=pothole1)
marker_1.image_zoom_visibility=(18, 22)
marker_1.hide_image(False)

pothole2 = ImageTk.PhotoImage(Image.open('pothole2.jpg').resize((320, 200)))
marker_2 = map_widget.set_marker(13.017214, 77.636273, text="pothole", image=pothole2)
marker_2.image_zoom_visibility=(18, 22)
marker_2.hide_image(False)

root_tk.mainloop()