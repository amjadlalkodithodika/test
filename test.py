import streamlit as st
import time

# Initialize session state
if "show_countdown" not in st.session_state:
    st.session_state.show_countdown = False
if "cooldown_end" not in st.session_state:
    st.session_state.cooldown_end = 0

# Create a placeholder for the button/countdown
button_placeholder = st.empty()

if not st.session_state.show_countdown:
    # Render the button inside the placeholder
    if button_placeholder.button("Resend Code"):
        st.success("✅ Code sent to your email!")
        # Set cooldown for 30 seconds (easy to test)
        st.session_state.cooldown_end = time.time() + 30
        st.session_state.show_countdown = True
        st.rerun()

if st.session_state.show_countdown:
    remaining = int(st.session_state.cooldown_end - time.time())
    if remaining > 0:
        mins, secs = divmod(remaining, 60)
        # Replace the button with countdown text in the same spot
        button_placeholder.info(f"Next resend in: {mins:02d}:{secs:02d}")
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.show_countdown = False
        st.rerun()
