import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests, random, html, os


# Configuration flags
FIXED_GEOMETRY = False  # If True, the window size will not change
HIGHLIGHT_SIGNIFICANT_WORD = False  # If True, the most significant word in the question will be highlighted

# Category ID mapping for trivia questions
CATEGORIES = {
    "Books": 10,
    "Films & Movies": 11,
    "Video Games": 15,
    "Cartoon & Animations": 32,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Art": 25,
    "Animals": 27,
    "Vehicles": 28,
    "Science & Nature": 17,
    "Mathematics": 19,
    "Computers": 18,
    "Gadgets": 30
}

# List to keep references to images to prevent garbage collection
image_references = []


def main() -> None:
    """
    Main function to initialize and run the quiz app.

    Returns:
        None
    """
    root = tk.Tk()
    root.title("Quiz Game")
    welcome_window(root)  # Show the category selection window
    root.mainloop()


def fetch_questions(amount: int = 5, category_id: int = 9, difficulty: str = 'medium') -> list[dict] | None:
    """
    Fetch trivia questions from the Open Trivia Database.

    Args:
        amount (int): Number of questions to fetch.
        category_id (int): Category ID for the questions.
        difficulty (str): Difficulty level ('easy', 'medium', 'hard').

    Returns:
        list[dict]: List of questions in dictionary format if successful.
        None: If the request fails.
    """
    url = f"https://opentdb.com/api.php?amount={amount}&category={category_id}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        messagebox.showerror("Error", "Failed to fetch questions")
        return None


def get_significant_word(text: str, highlighted: bool = False) -> str | None:
    """
    Extract the most significant word in the question.

    Args:
        text (str): The text of the question.
        highlight (bool): Whether to highlight the significant word.

    Returns:
        str | None: The most significant word, optionally highlighted if enabled.
    """
    words = text.split()
    if not words:
        return None
    
    # Find the most significant word (longest word)
    significant_word = max(words, key=len)

    # Highlight the significant word if the flag is set
    if highlighted:
        return f"**{significant_word}**"
    else:
        return significant_word


def welcome_window(root: tk.Tk) -> tk.StringVar:
    """
    Display the category selection screen.

    Args:
        root (tk.Tk): The root window.

    Returns:
        tk.StringVar: The selected category as a Tkinter string variable.
    """
    if FIXED_GEOMETRY:
        root.geometry("300x600")  # Set fixed window size if the flag is set

    # Clear previous widgets from the window
    for widget in root.winfo_children():
        widget.destroy()

    # Title for the first page
    title_label = tk.Label(root, text="Welcome to Quiz Game", font=("Arial", 18, "bold"))
    title_label.pack(padx=10, pady=10)

    # Variables to store user selections
    num_questions_value = tk.IntVar(value=10)  # Default number of questions
    difficulty_value = tk.StringVar(value="medium")  # Default difficulty
    category_value = tk.StringVar(value="Computers")  # Default category
    
    # Number of questions selection
    num_questions_label = tk.Label(root, text="Number of Questions", font=("Arial", 14))
    num_questions_label.pack(pady=5)
    num_questions_spinbox = tk.Spinbox(root, from_=2, to=20, textvariable=num_questions_value, width=5)
    num_questions_spinbox.pack(pady=5)

    # Difficulty selection
    difficulty_label = tk.Label(root, text="Select Difficulty", font=("Arial", 14))
    difficulty_label.pack(pady=10)
    for difficulty in ["easy", "medium", "hard"]:
        radio_btn = tk.Radiobutton(root, text=difficulty.capitalize(), variable=difficulty_value, value=difficulty, padx=50)
        radio_btn.pack(anchor='w')

    # Category selection
    category_label = tk.Label(root, text="Select a Category", font=("Arial", 14))
    category_label.pack(pady=10)

    for category in CATEGORIES.keys():
        radio_btn = tk.Radiobutton(root, text=category, variable=category_value, value=category, padx=50)
        radio_btn.pack(anchor='w') 

    # Start button to initiate the quiz
    start_button = tk.Button(root, text="Start Quiz", command=lambda: start_quiz(root, category_value.get(), difficulty_value.get(), num_questions_value.get()))
    start_button.pack(pady=20)

    return category_value


def start_quiz(root: tk.Tk, selected_category: str, difficulty: str, num_questions: int) -> None:
    """
    Start the quiz with the selected category, difficulty, and number of questions.

    Args:
        root (tk.Tk): The root window.
        selected_category (str): The selected quiz category.
        difficulty (str): The selected difficulty level.
        num_questions (int): The number of questions to ask.

    Returns:
        None
    """
    if not selected_category:
        messagebox.showwarning("Warning", "Please select a category")
        return

    category_id = CATEGORIES[selected_category]
    questions = fetch_questions(amount=num_questions, category_id=category_id, difficulty=difficulty)
    
    if not questions:
        return
    if FIXED_GEOMETRY:
        root.geometry("300x400")  # Adjust window size for quiz if the flag is set

    load_question(root, questions, 0, 0, HIGHLIGHT_SIGNIFICANT_WORD)  # Load the first question


def load_question(root: tk.Tk, questions: list[dict], current_index: int, score: int, highlight: bool = False) -> None:
    """
    Load and display the current question.

    Args:
        root (tk.Tk): The root window.
        questions (list[dict]): The list of questions.
        current_index (int): The index of the current question being displayed.
        score (int): The current score of the player.
        highlight (bool): Whether to highlight the significant word.

    Returns:
        None
    """
    question_data = questions[current_index]

    # Clear previous widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Decode HTML entities and get the significant word
    question_text = html.unescape(question_data['question'])
    significant_word = get_significant_word(question_text, False)

    # Highlight the significant word if required
    if highlight and significant_word:
        question_text = question_text.replace(significant_word.strip("**"), significant_word)

    # Display the question text
    question_label = tk.Label(root, text=f"{current_index + 1}. {question_text}", wraplength=250, padx=10, font=("Arial", 12))
    question_label.pack(pady=20)

    radio_value = tk.StringVar(value="")
    option_buttons = []

    # Prepare and shuffle options
    options = question_data['incorrect_answers']
    options.append(question_data['correct_answer'])
    random.shuffle(options)

    for option in options:
        option = html.unescape(option)
        radio_btn = tk.Radiobutton(root, text=option, variable=radio_value, value=option, padx=30)
        radio_btn.pack(anchor='w')
        option_buttons.append(radio_btn)

    # Check if an image corresponding to the significant word exists
    image_filename = f"images/{significant_word.lower()}.png" if significant_word else "images/question.png"
    if not os.path.exists(image_filename):
        image_filename = "images/question.png"

    # Load and display the image if it exists
    try:
        image = Image.open(image_filename)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)

        image_references.append(photo)  # Keep a reference to prevent garbage collection
        # Use Canvas to display the image
        canvas = tk.Canvas(root, width=200, height=200)
        canvas.pack(pady=10)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    except Exception as e:
        print(f"Error loading image: {e}")
        messagebox.showerror("Error", "Failed to load the image.")

    # Initially, the continue button is disabled until an option is selected
    continue_button = tk.Button(root, text="Check", state=tk.DISABLED, command=lambda: next_question(root, questions, current_index, score, radio_value.get(), option_buttons, question_data['correct_answer']))
    continue_button.pack(pady=20)

    # Enable the continue button once an option is selected
    def on_option_selected(*args):
        continue_button.config(state=tk.NORMAL)

    radio_value.trace_add("write", on_option_selected)


def next_question(root: tk.Tk, questions: list[dict], current_index: int, score: int, selected_answer: str, option_buttons: list[tk.Radiobutton], correct_answer: str) -> None:
    """
    Handle the logic for the next question, including updating the score and moving to the next question.

    Args:
        root (tk.Tk): The root window.
        questions (list[dict]): The list of questions.
        current_index (int): The index of the current question being displayed.
        score (int): The current score of the player.
        selected_answer (str): The answer selected by the player.
        option_buttons (list[tk.Radiobutton]): List of option buttons for the current question.
        correct_answer (str): The correct answer for the current question.

    Returns:
        None
    """
    # Highlight correct and incorrect answers
    for btn in option_buttons:
        if btn['text'] == html.unescape(correct_answer):
            btn.config(bg='#00FF7F')  # Green for correct answer
        elif btn['text'] == selected_answer:
            if selected_answer != html.unescape(correct_answer):
                btn.config(bg='#F08080')  # Red for incorrect answer

    # Update score if the selected answer is correct
    if selected_answer == html.unescape(correct_answer):
        score += 1

    # Disable all option buttons after selection
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)

    # Replace the continue button to load the next question
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()

    current_index += 1
    if current_index < len(questions):
        continue_button = tk.Button(root, text="Continue", command=lambda: load_question(root, questions, current_index, score, HIGHLIGHT_SIGNIFICANT_WORD))
        continue_button.pack(pady=20)
    else:
        show_final_score(root, score, len(questions))


def show_final_score(root: tk.Tk, score: int, total: int) -> None:
    """
    Display the final score to the player and quit the application.

    Args:
        root (tk.Tk): The root window.
        score (int): The final score of the player.
        total (int): The total number of questions.

    Returns:
        None
    """
    messagebox.showinfo("Quiz Completed", f"Your final score is: {score}/{total}")
    root.quit()


if __name__ == "__main__":
    main()
