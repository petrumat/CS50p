# Quiz Game

#### Video Demo: [Final Project](https://youtu.be/I69H-EpEzJs)

#### Description:

My final project for this course is an interactive trivia quiz game. Tkinter was used to create the graphical user interface for this program. Gamers may choose the category, number of questions, and degree of difficulty while testing their knowledge on a range of subjects. Every trivia question is taken from the Open Trivia Database and formatted for ease of usage. To improve the experience, I decided to provide multiple-choice responses (instead of True/False) and graphic components.

### Execution

- **Run the project**: Call python interpreter cli: *python project.py*.
- **Run unit tests**: Call pytest in cli: **pytest test_project.py*. This will test functions including `fetch_questions()` that will fail and an error message will appear. This is normal a behavior of the quiz game (click *Ok* to continue testing).

### Features

- **Category Selection**: Numerous trivia categories, including Books, Films, Sports, Science, and more, are available for users to select from. Naturally, 'Computers' is the default.
- **Difficulty Levels**: The quiz offers three difficulty levels: easy, medium, and hard.
- **Number of Questions**: Users can specify the number of questions they want to answer in a single quiz session. Options vary from 2 to 20 questions per session.
- **Image Integration**: The application attempts to display relevant images based on the significant words in the questions. If a picture isn't available for that significant word, a question mark image appears.
- **Score Tracking**: The user’s score is calculated and displayed at the end of the quiz.

### Files and Functionality

- **`project.py`**: Contains the core functionality of the quiz game separated in many functions:
  - `main()`: Initializes the application by setting up the Tkinter window and starts the quiz by calling the `welcome_window()` function.
  - `welcome_window()`: Displays the initial screen for category and quiz settings selection. The questions appear after `Start Quiz` button is clicked.
  - `start_quiz()`: Starts the quiz with the user’s selected settings by loading fetched questions from Open Trivia DB API.
  - `fetch_questions()`: Fetches trivia questions based on user preferences.
  - `load_question()`: Loads and displays the current trivia question along with its options. This can highlight significant word. Also shows an image for that word (if exists) or a default question image. After the current question is checked than the player can continue to next question.
  - `get_significant_word()`: Extracts the most significant word from a trivia question. The word can be highlighted with "\*\*" symbols.
  - `next_question()`: Handles the transition to the next question, updating the score and UI. This function calls `load_question()` (and the cycle continues) or `show_final_score()` based on the index of that question.
  - `show_final_score()`: Displays the final score and exits the application.

- **`requirements.txt`**: Lists the Python libraries required for this project. Ensure you install the dependencies using `pip install -r requirements.txt`.

- **`test_project.py`**: Contains unit tests for the project using `pytest`. It includes tests for the core functions like `fetch_questions()`, `get_significant_word()`, `start_quiz()` and `show_final_score()`.

- **`images/`**: Folder containing images for the significant word in the question. A default 200x200 pixels *question.png* image is present. Players may add their own images in the same format for different words. 

### Design Choices

- **GUI Framework**: I choose Tkinter for its simplicity and integration with the Python standard library. It provides a straightforward way to create GUIs without additional dependencies.

- **Image Handling**: Since `Pillow` supports a wide range of image formats and guarantees compatibility with the Tkinter `Canvas` widget, it was an obvious option for image processing.

- **Testing**: I opted for `pytest` since it has powerful features and ease of use in writing and running tests. I verified the functionality of critical components and ensured a reliable experience with this tool.

### Goals and Milestones

- **Initial Setup**: Set up the basic GUI and integrate the Open Trivia Database API.
- **Feature Implementation**: Develop core features such as category selection, difficulty levels, and score tracking.
- **Image Integration**: Add functionality to handle and display images based on trivia questions.
- **Testing and Debugging**: Write and execute tests to ensure the application works as expected and fix any bugs.
- **Final Review**: Complete documentation and prepare for uploading.

I hope you enjoy using the Quiz Game and find it both entertaining and educational. Happy quizzing!
