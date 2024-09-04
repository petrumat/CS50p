import pytest
from unittest.mock import patch, Mock, MagicMock
from tkinter import Tk
from project import fetch_questions, get_significant_word, start_quiz, show_final_score, CATEGORIES


# Sample questions for testing
SAMPLE_QUESTIONS = [
    {
        'question': 'What is the capital of France?',
        'correct_answer': 'Paris',
        'incorrect_answers': ['London', 'Berlin', 'Madrid']
    },
    {
        'question': 'What is the largest planet in our Solar System?',
        'correct_answer': 'Jupiter',
        'incorrect_answers': ['Earth', 'Mars', 'Saturn']
    }
]


def test_fetch_questions_success():
    """ Test the fetch_questions function with a successful API call. """
    with patch('requests.get') as mock_get:
        # Setup the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'results': SAMPLE_QUESTIONS}
        mock_get.return_value = mock_response
        
        questions = fetch_questions(amount=2, category_id=CATEGORIES['Geography'], difficulty='medium')
        
        assert questions is not None
        assert len(questions) == 2
        assert questions[0]['question'] == 'What is the capital of France?'


def test_fetch_questions_failure():
    """ Test the fetch_questions function with a failed API call. """
    with patch('requests.get') as mock_get:
        # Setup the mock response for failure
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        questions = fetch_questions(amount=2, category_id=CATEGORIES['Geography'], difficulty='medium')
        
        assert questions is None


def test_get_significant_word():
    """ Test the get_significant_word function. """
    text = "Which planet is known for its rings?"
    
    # Test without highlighting
    significant_word = get_significant_word(text, False)
    assert significant_word == f"planet"

    # Test with highlighting enabled
    significant_word = get_significant_word(text, True)
    assert significant_word == f"**planet**"


def test_get_significant_word_empty():
    """ Test the get_significant_word function with empty text. """
    text = ""
    significant_word = get_significant_word(text)
    
    assert significant_word is None


@patch('project.fetch_questions')
@patch('project.load_question')
def test_start_quiz(mock_load_question, mock_fetch_questions):
    """ Test the start_quiz function to ensure it calls fetch_questions and load_question. """
    root = MagicMock(Tk)
    mock_fetch_questions.return_value = SAMPLE_QUESTIONS
    mock_load_question.return_value = None
    
    start_quiz(root, 'Geography', 'medium', 2)
    
    # Verify fetch_questions is called with correct parameters
    mock_fetch_questions.assert_called_once_with(amount=2, category_id=CATEGORIES['Geography'], difficulty='medium')
    
    # Verify load_question is called with initial parameters
    mock_load_question.assert_called_once_with(root, SAMPLE_QUESTIONS, 0, 0, False)


@patch('project.tk.messagebox.showinfo')
def test_show_final_score(mock_showinfo):
    """ Test the show_final_score function to ensure the final score is displayed. """
    root = MagicMock(Tk)
    
    show_final_score(root, 5, 10)
    
    # Check that showinfo is called with the correct message
    mock_showinfo.assert_called_once_with("Quiz Completed", "Your final score is: 5/10")


if __name__ == "__main__":
    pytest.main()
