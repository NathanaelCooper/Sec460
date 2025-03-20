import streamlit as st
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

# Initialize session state for score tracking
if "player_score" not in st.session_state:
    st.session_state["player_score"] = 0
    st.session_state["computer_score"] = 0

# Streamlit UI
st.title("🪨📄✂️ Rock-Paper-Scissors Game!")
st.write("Choose your move and play against the computer!")

# User selection
player_choice = st.radio("Your Move:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    result = get_winner(player_choice, computer_choice)

    # Update scores
    if result == "You win!":
        st.session_state["player_score"] += 1
    elif result == "You lose!":
        st.session_state["computer_score"] += 1

    # Display results
    st.subheader(f"🤖 Computer chose: {computer_choice}")
    st.subheader(f"📢 {result}")

    # Show Scoreboard
    st.write("---")
    st.subheader(f"🏆 Scoreboard:")
    st.write(f"**You:** {st.session_state['player_score']} | **Computer:** {st.session_state['computer_score']}")

# Reset Score Button
if st.button("Reset Score"):
    st.session_state["player_score"] = 0
    st.session_state["computer_score"] = 0
    st.success("Score reset!")

