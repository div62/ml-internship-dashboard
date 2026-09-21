import customtkinter as ctk
from models.predict import make_prediction
from models.load_model import load_model
from sklearn.datasets import load_iris
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from preprocessing.preprocess import split_data
from models.evaluate import evaluate_model
from backend.data_loader import load_iris_data
# APPEARANCE
ctk.set_appearance_mode("dark")
# COLORS
BACKGROUND = "#000000"
CARD = "#111111"
INPUT = "#1A1A1A"

ACCENT = "#00D4FF"
ACCENT_HOVER = "#00A8CC"

TEXT = "#FFFFFF"
SECONDARY_TEXT = "#A3A3A3"

SUCCESS = "#22C55E"
ERROR = "#EF4444"
BORDER = "#2A2A2A"

FONT_FAMILY = "Segoe UI"
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

    # TITLE
    title = ctk.CTkLabel(
        content_area,
        text="ML Dashboard",
        font=("Segoe UI", 30, "bold"),
        text_color=TEXT
    )

    title.pack(pady=(20, 3))

    subtitle = ctk.CTkLabel(
        content_area,
        text="Iris Flower Classification System",
        font=("Segoe UI", 14),
        text_color=SECONDARY_TEXT
    )

    subtitle.pack(pady=(0, 20))

    # STATISTICS CARDS
    cards_frame = ctk.CTkFrame(
        content_area,
        fg_color=BACKGROUND
    )

    cards_frame.pack(
        fill="x",
        padx=10,
        pady=5
    )

    def create_card(title_text, value_text, description):

        card = ctk.CTkFrame(
            cards_frame,
            fg_color=CARD,
            corner_radius=12,
            border_width=1,
            border_color=BORDER
        )

        card.pack(
            side="left",
            expand=True,
            fill="both",
            padx=6
        )

        title_label = ctk.CTkLabel(
            card,
            text=title_text.upper(),
            font=("Segoe UI", 11, "bold"),
            text_color=SECONDARY_TEXT
        )

        title_label.pack(
            pady=(18, 4)
        )

        value_label = ctk.CTkLabel(
            card,
            text=value_text,
            font=("Segoe UI", 24, "bold"),
            text_color=ACCENT
        )

        value_label.pack(
            pady=(0, 2)
        )

        description_label = ctk.CTkLabel(
            card,
            text=description,
            font=("Segoe UI", 11),
            text_color=SECONDARY_TEXT
        )

        description_label.pack(
            pady=(0, 15)
        )

    create_card(
        "Model Accuracy",
        "90%",
        "Test set performance"
    )

    create_card(
        "Dataset",
        "Iris",
        "150 samples"
    )

    create_card(
        "Algorithm",
        "Random Forest",
        "100 decision trees"
    )

    # MAIN OVERVIEW CARD
    overview_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=12,
        border_width=1,
        border_color=BORDER
    )

    overview_card.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=(18, 10)
    )

    overview_title = ctk.CTkLabel(
        overview_card,
        text="Welcome to the ML Dashboard",
        font=("Segoe UI", 22, "bold"),
        text_color=TEXT
    )

    overview_title.pack(
        pady=(25, 8)
    )

    overview_text = ctk.CTkLabel(
        overview_card,
        text=(
            "An interactive machine learning application "
            "for Iris flower classification.\n\n"
            "Explore the trained model, make predictions, "
            "and analyze model performance."
        ),
        font=("Segoe UI", 14),
        text_color=SECONDARY_TEXT,
        justify="center",
        wraplength=700
    )

    overview_text.pack(
        pady=10
    )

    # QUICK ACTION
    action_label = ctk.CTkLabel(
        overview_card,
        text="Ready to make a prediction?",
        font=("Segoe UI", 13, "bold"),
        text_color=TEXT
    )

    action_label.pack(
        pady=(18, 8)
    )

    prediction_button = ctk.CTkButton(
        overview_card,
        text="Start Prediction  →",
        width=220,
        height=42,
        corner_radius=8,
        font=("Segoe UI", 14, "bold"),
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        text_color=BACKGROUND,
        command=show_prediction
    )

    prediction_button.pack(
        pady=(0, 25)
    )


# PREDICTION PAGE
# PREDICTION PAGE

def show_prediction():

    clear_page()
    set_active_nav(prediction_nav)

    try:
        model = load_model()

    except FileNotFoundError as error:

        error_label = ctk.CTkLabel(
            content_area,
            text=str(error),
            font=("Segoe UI", 16),
            text_color=ERROR
        )

        error_label.pack(pady=50)

        return

    iris = load_iris()

    title = ctk.CTkLabel(
        content_area,
        text="Iris Flower Prediction",
        font=("Segoe UI", 28, "bold"),
        text_color=TEXT
    )

    title.pack(pady=(15, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="Enter flower measurements to classify the Iris species.",
        font=("Segoe UI", 14),
        text_color=SECONDARY_TEXT
    )

    subtitle.pack(pady=(0, 15))

    # INPUT CARD

    input_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15,
        border_width=1,
        border_color=BORDER
    )

    input_card.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    input_title = ctk.CTkLabel(
        input_card,
        text="Flower Measurements",
        font=("Segoe UI", 18, "bold"),
        text_color=TEXT
    )

    input_title.pack(
        pady=(15, 2)
    )

    input_subtitle = ctk.CTkLabel(
        input_card,
        text="Enter the measurements in centimeters.",
        font=("Segoe UI", 12),
        text_color=SECONDARY_TEXT
    )

    input_subtitle.pack(
        pady=(0, 10)
    )

    # INPUT CREATOR

    def create_input(parent, label_text, range_text):

        frame = ctk.CTkFrame(
            parent,
            fg_color=INPUT,
            corner_radius=10
        )

        label = ctk.CTkLabel(
            frame,
            text=label_text,
            font=("Segoe UI", 13, "bold"),
            text_color=TEXT
        )

        label.pack(
            anchor="w",
            padx=12,
            pady=(10, 2)
        )

        range_label = ctk.CTkLabel(
            frame,
            text=range_text,
            font=("Segoe UI", 10),
            text_color=SECONDARY_TEXT
        )

        range_label.pack(
            anchor="w",
            padx=12
        )

        entry = ctk.CTkEntry(
            frame,
            height=35,
            fg_color=BACKGROUND,
            border_color=BORDER,
            text_color=TEXT,
            font=("Segoe UI", 13)
        )

        entry.pack(
            fill="x",
            padx=12,
            pady=(5, 10)
        )

        return frame, entry

    # INPUTS

    inputs_frame = ctk.CTkFrame(
        input_card,
        fg_color=BACKGROUND
    )

    inputs_frame.pack(
        fill="x",
        padx=15,
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

    sepal_length_frame, sepal_length_entry = create_input(
        row_one,
        "Sepal Length",
        "4.0–8.0 cm"
    )

    sepal_length_frame.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5
    )

    sepal_width_frame, sepal_width_entry = create_input(
        row_one,
        "Sepal Width",
        "2.0–4.5 cm"
    )

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
        "Petal Length",
        "1.0–7.0 cm"
    )

    petal_length_frame.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5
    )

    petal_width_frame, petal_width_entry = create_input(
        row_two,
        "Petal Width",
        "0.1–2.5 cm"
    )

    petal_width_frame.pack(
        side="left",
        expand=True,
        fill="x",
        padx=5
    )

    # RESULT

    result_label = ctk.CTkLabel(
        input_card,
        text="Prediction will appear here",
        font=("Segoe UI", 18, "bold"),
        text_color=SECONDARY_TEXT
    )

    result_label.pack(
        pady=(15, 5)
    )

    # PREDICTION FUNCTION

    def predict_flower():

        try:

            sepal_length = float(
                sepal_length_entry.get()
            )

            sepal_width = float(
                sepal_width_entry.get()
            )

            petal_length = float(
                petal_length_entry.get()
            )

            petal_width = float(
                petal_width_entry.get()
            )

        except ValueError:

            result_label.configure(
                text="Please enter valid numbers.",
                text_color=ERROR
            )

            return

        if not (
            4.0 <= sepal_length <= 8.0
            and 2.0 <= sepal_width <= 4.5
            and 1.0 <= petal_length <= 7.0
            and 0.1 <= petal_width <= 2.5
        ):

            result_label.configure(
                text="Please enter values within the given ranges.",
                text_color=ERROR
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

    # PREDICT BUTTON

    predict_button = ctk.CTkButton(
        input_card,
        text="Predict Iris Species  →",
        width=300,
        height=45,
        fg_color=ACCENT,
        hover_color=ACCENT_HOVER,
        text_color=BACKGROUND,
        font=("Segoe UI", 15, "bold"),
        corner_radius=8,
        command=predict_flower
    )

    predict_button.pack(
        pady=(10, 20)
    )

# ANALYTICS PAGE
def show_analytics():

    clear_page()
    set_active_nav(analytics_nav)

    title = ctk.CTkLabel(
        content_area,
        text="Model Analytics",
        font=("Segoe UI", 28, "bold"),
        text_color=TEXT
    )

    title.pack(pady=(15, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="Explore the Iris dataset and model performance.",
        font=("Segoe UI", 14),
        text_color=SECONDARY_TEXT
    )

    subtitle.pack(pady=(0, 10))

    # LOAD MODEL AND CALCULATE ACCURACY

    df = load_iris_data()

    X_train, X_test, y_train, y_test = split_data(df)

    model = load_model()

    accuracy, confusion  = evaluate_model(
        model,
        X_test,
        y_test
    )

    # ACCURACY CARD

    accuracy_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15,
        height=90
    )

    accuracy_card.pack(
        fill="x",
        padx=10,
        pady=(0, 10)
    )

    accuracy_card.pack_propagate(False)

    accuracy_title = ctk.CTkLabel(
        accuracy_card,
        text="Model Accuracy",
        font=("Segoe UI", 14, "bold"),
        text_color=SECONDARY_TEXT
    )

    accuracy_title.pack(
        pady=(12, 2)
    )

    accuracy_value = ctk.CTkLabel(
        accuracy_card,
        text=f"{accuracy:.0%}",
        font=("Segoe UI", 24, "bold"),
        text_color=ACCENT
    )

    accuracy_value.pack()
        # CONFUSION MATRIX

    confusion_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15,
        height=180
    )

    confusion_card.pack(
        fill="x",
        padx=10,
        pady=(0, 10)
    )

    confusion_card.pack_propagate(False)

    confusion_title = ctk.CTkLabel(
        confusion_card,
        text="Confusion Matrix",
        font=("Segoe UI", 14, "bold"),
        text_color=SECONDARY_TEXT
    )

    confusion_title.pack(
        pady=(8, 2)
    )

    matrix_figure = Figure(
        figsize=(6, 2.5),
        dpi=80
    )

    matrix_axis = matrix_figure.add_subplot(111)

    matrix_axis.imshow(
    confusion,
    aspect="auto"
)
    matrix_axis.set_xlim(-0.5, 2.5)
    matrix_axis.set_ylim(2.5, -0.5)
    matrix_axis.set_title(
        "Model Predictions vs Actual"
    )

    matrix_axis.set_xlabel(
        "Predicted"
    )

    matrix_axis.set_ylabel(
        "Actual"
    )

    matrix_axis.set_xticks([0, 1, 2])
    matrix_axis.set_yticks([0, 1, 2])

    matrix_axis.set_xticklabels(
        ["Setosa", "Versicolor", "Virginica"]
    )

    matrix_axis.set_yticklabels(
        ["Setosa", "Versicolor", "Virginica"]
    )

    for i in range(3):
        for j in range(3):
            matrix_axis.text(
                j,
                i,
                confusion[i, j],
                ha="center",
                va="center"
            )

    matrix_figure.tight_layout()

    matrix_canvas = FigureCanvasTkAgg(
        matrix_figure,
        master=confusion_card
    )

    matrix_canvas.draw()

    matrix_canvas.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 5)
)
    # ANALYTICS CHART CARD

    analytics_card = ctk.CTkFrame(
        content_area,
        fg_color=CARD,
        corner_radius=15,
        height=250
    )

    analytics_card.pack(
        fill="x",
        padx=10,
        pady=10
    )

    analytics_card.pack_propagate(False)

    iris = load_iris()

    # LEFT CHART

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

    species_names = [
        "Setosa",
        "Versicolor",
        "Virginica"
    ]

    figure = Figure(
        figsize=(5, 3.5),
        dpi=80
    )

    axis = figure.add_subplot(111)

    axis.bar(
        species_names,
        species_counts
    )

    axis.set_title(
        "Iris Species Distribution"
    )

    axis.set_xlabel(
        "Species"
    )

    axis.set_ylabel(
        "Number of Samples"
    )

    canvas = FigureCanvasTkAgg(
        figure,
        master=left_chart
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )

    # RIGHT CHART

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

    figure_two = Figure(
        figsize=(5, 3.5),
        dpi=80
    )

    axis_two = figure_two.add_subplot(111)

    for class_index, class_name in enumerate(
        iris.target_names
    ):

        class_data = iris.data[
            iris.target == class_index
        ]

        axis_two.scatter(
            class_data[:, 2],
            class_data[:, 3],
            label=class_name
        )

    axis_two.set_title(
        "Petal Length vs Petal Width"
    )

    axis_two.set_xlabel(
        "Petal Length (cm)"
    )

    axis_two.set_ylabel(
        "Petal Width (cm)"
    )

    axis_two.legend()

    canvas_two = FigureCanvasTkAgg(
        figure_two,
        master=right_chart
    )

    canvas_two.draw()

    canvas_two.get_tk_widget().pack(
        fill="both",
        expand=True
    )
# ABOUT PAGE

def show_about():
    clear_page()
    set_active_nav(about_nav)

    title = ctk.CTkLabel(
        content_area,
        text="About",
        font=("Segoe UI", 28, "bold"),
        text_color=TEXT
    )
    title.pack(pady=(20, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="About the ML Internship Dashboard",
        font=("Segoe UI", 14),
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

    about_text = about_text = (
    "ML Internship Dashboard\n\n"
    "An interactive machine learning dashboard "
    "Built using Python and CustomTkinter.\n\n"
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
        font=("Segoe UI", 18),
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
        font=("Segoe UI", 28, "bold"),
        text_color=TEXT
    )

    title.pack(pady=(20, 5))

    subtitle = ctk.CTkLabel(
        content_area,
        text="Information about the trained machine learning model.",
        font=("Segoe UI", 14),
        text_color=SECONDARY_TEXT
    )

    subtitle.pack(pady=(0, 30))

    # LOAD MODEL AND DATA

    model = load_model()
    df = load_iris_data()

    X_train, X_test, y_train, y_test = split_data(df)

    accuracy, _ = evaluate_model(
        model,
        X_test,
        y_test
    )

    iris = load_iris()

    # MODEL INFORMATION

    model_name = type(model).__name__
    number_of_trees = model.n_estimators
    number_of_features = X_test.shape[1]
    number_of_classes = len(iris.target_names)

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
        font=("Segoe UI", 24, "bold"),
        text_color=ACCENT
    )

    info_title.pack(
        pady=(25, 20)
    )

    model_details = [
        ("Dataset", "Iris Dataset"),
        ("Algorithm", model_name),
        ("Number of Trees", str(number_of_trees)),
        ("Train / Test Split", "80% / 20%"),
        ("Number of Features", str(number_of_features)),
        ("Number of Classes", str(number_of_classes)),
        ("Test Accuracy", f"{accuracy:.0%}")
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
            font=("Segoe UI", 14, "bold"),
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
            font=("Segoe UI", 14),
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
    font=("Segoe UI", 14),
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
    font=("Segoe UI", 14),
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
    font=("Segoe UI", 14),
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
    font=("Segoe UI", 14),
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