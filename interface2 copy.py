import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time
from kafka import KafkaConsumer
import json
import threading
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time
from kafka import KafkaConsumer
import json
import threading
from PIL import Image, ImageTk

class KafkaGraphConsumer(threading.Thread):
    def __init__(self, topic):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.data = {}
        self.topic = topic
        
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')), 
            consumer_timeout_ms=1000
        )

    def run(self):
        while not self.stop_event.is_set():
            try:
                for message in self.consumer:
                    if self.stop_event.is_set():
                        break
                    value_dict = message.value
                    current_time = time.time()
                    
                    print("Received data:", value_dict)  # Print the received dictionary
                    
                    for key, value in value_dict.items():
                        if key not in self.data:
                            self.data[key] = {"x": [], "y": []}
                        self.data[key]["x"].append(current_time)
                        self.data[key]["y"].append(value)
                        
                        # Keep only last 50 points
                        self.data[key]["x"] = self.data[key]["x"][-50:]
                        self.data[key]["y"] = self.data[key]["y"][-50:]
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
    def stop(self):
        self.stop_event.set()





class StylishKafkaRealtimeGraphs:
    def __init__(self, root):
        self.root = root
        self.root.title("Kafka Real-time Graphs")
        self.root.geometry("1400x800")
        self.root.configure(bg='#F0F2F5')  # Light gray background

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#FFFFFF')
        
        self.topic = 'my-topic'
        self.kafka_consumer = KafkaGraphConsumer(self.topic)
        self.kafka_consumer.start()

        self.current_page = "descriptors"
        self.graphs = {}
        self.graph_frames = {}

        self.create_sidebar()
        self.create_main_area()
        self.create_graphs()
        self.show_page("descriptors")
        
        self.update_graphs()

    def create_sidebar(self):
        sidebar = ttk.Frame(self.root, style='TFrame', padding="10")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        title_label = ttk.Label(sidebar, text="Navigation", font=("Helvetica", 16), foreground="#ECF0F1", background="#34495E")
        title_label.pack(pady=10)

        btn_page1 = ttk.Button(sidebar, text="Page 1", command=lambda: self.show_page(0))
        btn_page1.pack(fill=tk.X, pady=5)

        btn_page2 = ttk.Button(sidebar, text="Page 2", command=lambda: self.show_page(1))
        btn_page2.pack(fill=tk.X, pady=5)

    def create_main_area(self):
        self.main_area = ttk.Frame(self.root, style='TFrame', padding="20")
        self.main_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_graphs(self):
        metrics = ['alt', 'TRA', 'T2', 'T24']
        colors = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12']  # Red, Blue, Green, Orange

        for page in ["descriptors", "malaks", "pressure", "ratio air"]:
            page_frame = ttk.Frame(self.main_area)
            self.graph_frames[page] = page_frame
            
            for i, (metric, color) in enumerate(zip(metrics, colors)):
                figure = Figure(figsize=(5, 3), dpi=100, facecolor='#FFFFFF')
                ax = figure.add_subplot(111)
                ax.set_facecolor('#FFFFFF')
                line, = ax.plot([], [], color=color, linewidth=2)
                ax.set_title(f"{metric}", color='#333333', fontsize=12)
                ax.tick_params(colors='#333333')
                for spine in ax.spines.values():
                    spine.set_edgecolor('#333333')

                canvas = FigureCanvasTkAgg(figure, master=page_frame)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")

                self.graphs.setdefault(page, []).append({
                    "figure": figure,
                    "ax": ax,
                    "line": line,
                    "metric": metric,
                    "canvas": canvas
                })

            for i in range(2):
                page_frame.grid_columnconfigure(i, weight=1)
            for i in range(2):
                page_frame.grid_rowconfigure(i, weight=1)

    def show_live_image(self):
        # Clear the main area
        for widget in self.main_area.winfo_children():
            widget.pack_forget()

        # Load and display the image
        image_path = "cmapps.PNG"  # Replace with your image path
        try:
            image = Image.open(image_path)
            
            # Resize the image to fit the main area while maintaining aspect ratio
            main_area_width = self.main_area.winfo_width()
            main_area_height = self.main_area.winfo_height()
            image.thumbnail((main_area_width, main_area_height), Image.LANCZOS)
            
            photo = ImageTk.PhotoImage(image)
            
            label = ttk.Label(self.main_area, image=photo, background='#FFFFFF')
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(expand=True, fill=tk.BOTH)
            
            # Center the image in the main area
            label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            
        except Exception as e:
            error_label = ttk.Label(self.main_area, text=f"Error loading image: {str(e)}", background='#FFFFFF')
            error_label.pack(expand=True)

    def show_page(self, page):
        self.current_page = page
        for widget in self.main_area.winfo_children():
            widget.pack_forget()

        if page == "live":
            self.show_live_image()
        else:
            self.graph_frames[page].pack(expand=True, fill=tk.BOTH)

    def update_graphs(self):
        for page, graphs in self.graphs.items():
            for graph in graphs:
                metric = graph["metric"]
                if metric in self.kafka_consumer.data:
                    data = self.kafka_consumer.data[metric]
                    
                    graph["line"].set_data(data["x"], data["y"])
                    graph["ax"].relim()
                    graph["ax"].autoscale_view()
                    graph["figure"].tight_layout()
                    graph["canvas"].draw_idle()

        self.root.after(1000, self.update_graphs)

    def on_closing(self):
        self.kafka_consumer.stop()
        self.root.quit()



if __name__ == "__main__":
    root = tk.Tk()
    app = StylishKafkaRealtimeGraphs(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
