import customtkinter as ctk
from models.predict import make_prediction
from models.load_model import load_model
from sklearn.datasets import load_iris
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# APPEARANCE
ctk.set_appearance_mode("dark")
# COLORS

BACKGROUND = "#101820"
CARD = "#1B2631"
INPUT = "#263746"
ACCENT = "#00BFA6"
ACCENT_HOVER = "#009688"
TEXT = "#FFFFFF"
SECONDARY_TEXT = "#AAB7B8"
# MAIN WINDOW
app = ctk.CTk()

app.title("ML Internship Dashboard")
app.geometry("1100x700")
app.minsize(900, 600)

app.configure(fg_color=BACKGROUND)
# CONTENT AREA

content_area = ctk.CTkFrame(
    app,
    fg_color=BACKGROUND,
    corner_radius=0
)

content_area.pack(
    side="top",
    fill="both",
    expand=True,
    padx=40,
    pady=(25, 10)
)
# CLEAR PAGE
def clear_page():
    for widget in content_area.winfo_children():
        widget.destroy()
def set_active_nav(active_button):
    nav_buttons = [
        dashboard_nav,
        prediction_nav,
        analytics_nav,
        model_nav,
        about_nav
    ]

    for button in nav_buttons:
        button.configure(
            fg_color=ACCENT if button == active_button else "transparent",
            text_color=BACKGROUND if button == active_button else TEXT
        )        
# DASHBOARD PAGE
def show_dashboard():

    clear_page()
    set_active_nav(dashboard_nav)

    # Title
    title = ctk.CTkLabel(
        content_area,
        text="Iris Flower Classification System",
        font=("Arial", 32, "bold"),
        text_color=TEXT
    )
    title.pack(pady=(20, 5))

    # Information cards
    cards_frame = ctk.CTkFrame(
        content_area,
        fg_color=BACKGROUND
    )

    cards_frame.pack(
        fill="x",
        pady=10
    )

    def create_card(heading, value):

        card = ctk.CTkFrame(
            cards_frame,
            fg_color=CARD,
            corner_radius=15
        )

        card.pack(
            side="left",
            expand=True,
            fill="both",
            padx=10
        )

        heading_label = ctk.CTkLabel(
            card,
            text=heading,
            font=("Arial", 14),
            text_color=SECONDARY_TEXT
        )

        heading_label.pack(pady=(20, 5))

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 22, "bold"),
            text_color=ACCENT
        )

        value_label.pack(pady=(0, 20))

    create_card("Model Accuracy", "90%")
    create_card("Dataset", "Iris🌸")
    create_card("Algorithm", "Random Forest")

    # Welcome section
    welcome_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15
    )

    welcome_card.pack(
        fill="both",
        expand=True,
        pady=(30, 10),
        padx=10
    )

    welcome_title = ctk.CTkLabel(
        welcome_card,
        text="HII!!",
        font=("Arial", 24, "bold"),
        text_color=TEXT
    )

    welcome_title.pack(pady=(35, 10))

    welcome_text = ctk.CTkLabel(
        welcome_card,
        text=(
            "Explore the Iris classification model\n"
            "Make predictions, and view model information."
        ),
        font=("Arial", 15),
        text_color=SECONDARY_TEXT,
        justify="center"
    )

    welcome_text.pack(pady=10)

    prediction_button = ctk.CTkButton(
        welcome_card,
        text="Go to Prediction",
        width=200,
        height=45,
        font=("Arial", 15, "bold"),
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        text_color=BACKGROUND,
        command=show_prediction
    )

    prediction_button.pack(pady=25)
# PREDICTION PAGE

def show_prediction():
    model = load_model()
    iris = load_iris()
    clear_page()
    set_active_nav(prediction_nav)

    title = ctk.CTkLabel(
        content_area,
        text="Iris Flower Prediction",
        font=("brush script", 28, "bold"),
        text_color=TEXT
    )
    title.pack(pady=(15, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="Enter flower measurements to classify the Iris species.",
        font=("brush script", 14),
        text_color=SECONDARY_TEXT
    )
    subtitle.pack(pady=(0, 20))

    input_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15
    )
    input_card.pack(
        fill="x",
        padx=80,
        pady=10
    )

    def create_input(parent, label_text):
        frame = ctk.CTkFrame(
            parent,
            fg_color=CARD,
            corner_radius=15
        )

        label = ctk.CTkLabel(
            frame,
            text=label_text,
            font=("brush script", 14, "bold"),
            text_color=TEXT
        )
        label.pack(
            anchor="w",
            padx=15,
            pady=(12, 5)
        )

        entry = ctk.CTkEntry(
            frame,
            height=35,
            font=("brush script", 15, "bold"),
            border_width=0,
            fg_color=INPUT,
            text_color=TEXT
        )
        entry.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        return frame, entry

    inputs_frame = ctk.CTkFrame(
        input_card,
        fg_color=BACKGROUND
    )
    inputs_frame.pack(
        fill="x",
        pady=5
    )

    row_one = ctk.CTkFrame(
        inputs_frame,
        fg_color=BACKGROUND
    )
    row_one.pack(
        fill="x",
        pady=5
    )

    sepal_length_frame, sepal_length_entry = create_input(row_one, "Sepal Length")
    sepal_length_frame.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5
    )

    sepal_width_frame, sepal_width_entry = create_input(row_one, "Sepal Width")
    sepal_width_frame.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5
    )

    row_two = ctk.CTkFrame(
        inputs_frame,
        fg_color=BACKGROUND
    )

    row_two.pack(
        fill="x",
        pady=5
    )

    petal_length_frame, petal_length_entry = create_input(
        row_two,
        "Petal Length"
    )

    petal_length_frame.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5
    )

    petal_width_frame, petal_width_entry = create_input(
        row_two,
        "Petal Width"
    )

    petal_width_frame.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5
    )

    def predict_flower():

        try:
            sepal_length = float(sepal_length_entry.get())
            sepal_width = float(sepal_width_entry.get())
            petal_length = float(petal_length_entry.get())
            petal_width = float(petal_width_entry.get())

        except ValueError:

            result_label.configure(
                text="Please enter valid numbers.",
                text_color="#FF6B6B"
            )

            return

        features = [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]

        prediction = make_prediction(
            model,
            features,
            iris.target_names,
            iris.feature_names
        )

        result_label.configure(
            text=prediction.capitalize(),
            text_color=ACCENT
        )

    predict_button = ctk.CTkButton(
        input_card,
        text="Predict Iris Species",
        width=300,
        height=45,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        text_color=BACKGROUND,
        font=("Arial", 15, "bold"),
        corner_radius=10,
        command=predict_flower
    )

    predict_button.pack(
        pady=(15, 10)
    )

    result_label = ctk.CTkLabel(
        input_card,
        text="Prediction will appear here",
        font=("brush script", 18, "bold"),
        text_color=SECONDARY_TEXT
    )

    result_label.pack(
        pady=(0, 20)
    )
def predict_flower():
        try:
            sepal_length = float(sepal_length_entry.get())
            sepal_width = float(sepal_width_entry.get())
            petal_length = float(petal_length_entry.get())
            petal_width = float(petal_width_entry.get())
        except ValueError:
            result_label.configure(
                text="Please enter valid numbers.",
                text_color="#FF6B6B"
            )
            return

        features = [
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]

        prediction = make_prediction(
            model,
            features,
            iris.target_names,
            iris.feature_names
        )

        result_label.configure(
            text=prediction.capitalize(),
            text_color=ACCENT
        )
# ANALYTICS PAGE

def show_analytics():
    clear_page()
    set_active_nav(analytics_nav)

    title = ctk.CTkLabel(
        content_area,
        text="Model Analytics",
        font=("Arial", 28, "bold"),
        text_color=TEXT
    )
    title.pack(pady=(15, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="Explore the Iris dataset and model performance.",
        font=("Arial", 14),
        text_color=SECONDARY_TEXT
    )
    subtitle.pack(pady=(0, 10))

    analytics_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15,
        height=430
    )
    analytics_card.pack(
        fill="x",
        padx=10,
        pady=10
    )
    analytics_card.pack_propagate(False)

    iris = load_iris()

    left_chart = ctk.CTkFrame(
        analytics_card,
        fg_color=CARD
    )
    left_chart.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    species_counts = [
        list(iris.target).count(0),
        list(iris.target).count(1),
        list(iris.target).count(2)
    ]
    species_names = ["Setosa", "Versicolor", "Virginica"]

    figure = Figure(figsize=(5, 3.5), dpi=80)
    axis = figure.add_subplot(111)
    axis.bar(species_names, species_counts)
    axis.set_title("Iris Species Distribution")
    axis.set_xlabel("Species")
    axis.set_ylabel("Number of Samples")

    canvas = FigureCanvasTkAgg(figure, master=left_chart)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    right_chart = ctk.CTkFrame(
        analytics_card,
        fg_color=CARD
    )
    right_chart.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    figure_two = Figure(figsize=(5, 3.5), dpi=80)
    axis_two = figure_two.add_subplot(111)

    for class_index, class_name in enumerate(iris.target_names):
        class_data = iris.data[iris.target == class_index]
        axis_two.scatter(
            class_data[:, 2],
            class_data[:, 3],
            label=class_name
        )

    axis_two.set_title("Petal Length vs Petal Width")
    axis_two.set_xlabel("Petal Length (cm)")
    axis_two.set_ylabel("Petal Width (cm)")
    axis_two.legend()

    canvas_two = FigureCanvasTkAgg(figure_two, master=right_chart)
    canvas_two.draw()
    canvas_two.get_tk_widget().pack(fill="both", expand=True)

# ABOUT PAGE

def show_about():
    clear_page()
    set_active_nav(about_nav)

    title = ctk.CTkLabel(
        content_area,
        text="About",
        font=("Arial", 28, "bold"),
        text_color=TEXT
    )
    title.pack(pady=(20, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="About the ML Internship Dashboard",
        font=("Arial", 14),
        text_color=SECONDARY_TEXT
    )
    subtitle.pack(pady=(0, 30))

    about_title = ctk.CTkLabel(
        content_area,
        text="About This Project",
        font=("Brush Script MT", 34, "bold"),
        text_color=ACCENT
    )
    about_title.pack(pady=(30, 15))

    about_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15
    )
    about_card.pack(
        fill="both",
        expand=True,
        padx=80,
        pady=20
    )

    about_text = (
                "ML Internship Dashboard\n\n"
                "An interactive machine learning dashboard "
                "built using Python and CustomTkinter.\n\n"
                "Dataset: Iris Dataset\n"
                "Algorithm: Random Forest Classifier\n"
                "Test Accuracy: 90%\n\n"
                "This project demonstrates data loading, preprocessing, "
                "model training, evaluation, prediction, visualization "
                "and model deployment through a graphical interface."
)

    message = ctk.CTkLabel(
        about_card,
        
        text=about_text,
        font=("Arial", 18),
        text_color=TEXT,
        justify="center",
        wraplength=700
    )
    message.pack(
        expand=True,
        padx=40,
        pady=40
    )

navigation = ctk.CTkFrame(
    app,
    fg_color=CARD,
    height=75,
    corner_radius=15
)

navigation.pack(
    side="bottom",
    fill="x",
    padx=40,
    pady=(5, 20)
)

navigation.pack_propagate(False)
# MODEL INFO PAGE
def show_model_info():

    clear_page()
    set_active_nav(model_nav)

    title = ctk.CTkLabel(
        content_area,
        text="Model Information",
        font=("Arial", 28, "bold"),
        text_color=TEXT
    )

    title.pack(pady=(20, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="Information about the trained machine learning model.",
        font=("Arial", 14),
        text_color=SECONDARY_TEXT
    )

    subtitle.pack(pady=(0, 30))

    info_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15
    )

    info_card.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    info_title = ctk.CTkLabel(
        info_card,
        text="Random Forest Classifier",
        font=("Arial", 24, "bold"),
        text_color=ACCENT
    )

    info_title.pack(pady=(25, 20))

    model_details = [
        ("Dataset", "Iris Dataset"),
        ("Algorithm", "Random Forest"),
        ("Number of Trees", "100"),
        ("Train / Test Split", "80% / 20%"),
        ("Number of Features", "4"),
        ("Number of Classes", "3"),
        ("Test Accuracy", "90%")
    ]

    for label_text, value_text in model_details:

        row = ctk.CTkFrame(
            info_card,
            fg_color=INPUT,
            corner_radius=10
        )

        row.pack(
            fill="x",
            padx=40,
            pady=5
        )

        label = ctk.CTkLabel(
            row,
            text=label_text,
            font=("Arial", 14, "bold"),
            text_color=TEXT
        )

        label.pack(
            side="left",
            padx=15,
            pady=10
        )

        value = ctk.CTkLabel(
            row,
            text=value_text,
            font=("Arial", 14),
            text_color=SECONDARY_TEXT
        )

        value.pack(
            side="right",
            padx=15,
            pady=10
        )

dashboard_nav = ctk.CTkButton(
    navigation,
    text="🏠  Dashboard",
    fg_color="transparent",
    hover_color="#263746",
    text_color=TEXT,
    font=("brush script", 14),
    command=show_dashboard
)

dashboard_nav.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=10
)


prediction_nav = ctk.CTkButton(
    navigation,
    text="🔮  Prediction",
    fg_color="transparent",
    hover_color="#263746",
    text_color=TEXT,
    font=("Arial", 14),
    command=show_prediction
)

prediction_nav.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=10
)


analytics_nav = ctk.CTkButton(
    navigation,
    text="📊  Analytics",
    fg_color="transparent",
    hover_color="#263746",
    text_color=TEXT,
    font=("Arial", 14),
    command=show_analytics
)

analytics_nav.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=10
)


model_nav = ctk.CTkButton(
    navigation,
    text="🔶  Model Info",
    fg_color="transparent",
    hover_color="#263746",
    text_color=TEXT,
    font=("Arial", 14),
    command=show_model_info
)

model_nav.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=10
)

about_nav = ctk.CTkButton(
    navigation,
    text="ℹ️  About",
    fg_color="transparent",
    hover_color="#263746",
    text_color=TEXT,
    font=("Arial", 14),
    command=show_about
)

about_nav.pack(
    side="left",
    expand=True,
    fill="both",
    padx=5,
    pady=10
)
# START WITH DASHBOARD
show_dashboard()
app.mainloop()