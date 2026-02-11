import streamlit as st
from random import randint

def random_number():
    return randint(1, 10**6)

def guessing_game():
    st.title("🎯 Number Guessing Game")
    st.write("Guess a number between **1 and 1,000,000**")

    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random_number()
        st.session_state.attempts = 0
        st.session_state.game_over = False

    guess = st.number_input("Enter your guess:", min_value=1, max_value=1000000, step=1)

    if st.button("Guess!"):
        st.session_state.attempts += 1

        if guess == st.session_state.number_to_guess:
            st.success(f"🎉 CONGRATULATIONS! You got it in {st.session_state.attempts} tries!")
            st.balloons()
            st.session_state.game_over = True
        elif guess < st.session_state.number_to_guess:
            st.warning("📈 Number to guess is HIGHER")
        else:
            st.warning("📉 Number to guess is LOWER")

    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.number_to_guess = random_number()
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.rerun()

st.set_page_config(page_title="Number Guessing Game", page_icon="🎯")
guessing_game()
