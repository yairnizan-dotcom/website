import streamlit as st
import random

# 1. Initialize Game State (so score doesn't reset)
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'target_emoji' not in st.session_state:
    st.session_state.target_emoji = random.choice(["🍎", "🚀", "🎸", "🎮", "🦄"])

st.header("🎮 Emoji Scramble")
st.success(f"Current Score: {st.session_state.score}")

# 2. Get User Input (Your Syntax!)
name = st.text_input("Enter ur player name:")

if name:
    st.write(f"Okay {name}, find the **{st.session_state.target_emoji}**!")
    
    # 3. Create interactive buttons for the game
    options = ["🍎", "🚀", "🎸", "🎮", "🦄"]
    random.shuffle(options)
    
    cols = st.columns(5)
    for i, emoji in enumerate(options):
        with cols[i]:
            if st.button(emoji):
                if emoji == st.session_state.target_emoji:
                    st.session_state.score += 1
                    st.session_state.target_emoji = random.choice(options)
                    st.balloons()
                    st.rerun() # Refresh to show new emoji
                else:
                    st.error("Wrong one! Try again.")

    if st.button("Reset Game"):
        st.session_state.score = 0
        st.rerun()
