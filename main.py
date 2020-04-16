import tkinter as tk
coords = []

def ready():
    global TEMP
    with open('govno.py', 'w') as f:
        f.write('\n'.join(TEMP))

def get_coords(event):
    global coords, edges_count, hex_input, width_input, canv, TEMP
    coords.append([event.x, event.y])
    if len(coords) == int(edges_count.get()):
        if len(coords) == 2:
            canv.create_line(coords, fill=hex_input.get(), width=width_input.get())
            TEMP.insert(3, 'canv.create_line({}, {}, {})'.format(coords, 'fill=' +"'"+hex_input.get()+"'",
                                                                 'width='+"'"+width_input.get()+"'"))
        else:
            canv.create_polygon(coords, fill=hex_input.get())
            TEMP.insert(3, 'canv.create_polygon({}, {})'.format(coords, 'fill=' +"'"+ hex_input.get()+"'"))
        coords = []
        print(TEMP)

TEMP = [
    'import tkinter as tk',
    'root = tk.Tk()',
    'canv = tk.Canvas(width=400, height=600)',

    'canv.pack()',
    'root.mainloop()',
]


root = tk.Tk()
canv = tk.Canvas(width=400, height=600)
width_input = tk.Entry(root, width=10)
hex_input = tk.Entry(root, width=10)
edges_count = tk.Entry(root, width=10)
width_label = tk.Label(root, text='width')
hex_label = tk.Label(root, text='hex color')
edges_label = tk.Label(text='edges')
ready_button = tk.Button(text='ready', command=ready)
canv.bind('<Button-1>', get_coords)

width_label.pack()
width_input.pack()
hex_label.pack()
hex_input.pack()
edges_label.pack()
edges_count.pack()
canv.pack()
ready_button.pack()
root.mainloop()
