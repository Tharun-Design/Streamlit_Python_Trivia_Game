import streamlit as st
import random

# Dictionary to store questions and answers
questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}

def python_trivia_game():
    """
    Main function to run the Streamlit trivia game.
    It uses st.session_state to manage the game flow.
    """
    st.title("Python Trivia Game 🎮")

    # Initialize or reset session state variables
    # This prevents the game from resetting on every interaction
    if "questions_list" not in st.session_state:
        st.session_state.questions_list = random.sample(list(questions.keys()), 5)
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.show_result = False

    # Check if there are still questions to ask
    if st.session_state.question_index < len(st.session_state.questions_list):
        current_question = st.session_state.questions_list[st.session_state.question_index]
        correct_answer = questions[current_question].lower().strip()

        st.header(f"Question {st.session_state.question_index + 1} of 5")
        st.subheader(current_question)

        # Use a unique key for the text input to prevent bugs
        user_answer = st.text_input("Your answer:", key=f"answer_input_{st.session_state.question_index}")

        # Button to submit the answer
        if st.button("Submit"):
            # Check the user's answer
            if user_answer.lower().strip() == correct_answer:
                st.success("Correct! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Wrong. The correct answer is: **{questions[current_question]}**.")
            
            # Move to the next question and show result
            st.session_state.question_index += 1
            st.session_state.show_result = True
            
            # Rerun the app to show the next question
            st.rerun()

    # Game over screen
    else:
        st.balloons()
        st.header("Game Over! 🥳")
        st.subheader(f"Your final score is: **{st.session_state.score}/5**")
        
        # Option to play again
        if st.button("Play Again?"):
            st.session_state.clear()  # Clear all session state variables
            st.rerun()  # Rerun the app to restart the game

# Standard entry point for the script
if __name__ == "__main__":
    python_trivia_game()
