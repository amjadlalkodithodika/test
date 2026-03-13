import streamlit as st
import time

# Initialize session state
if "show_countdown" not in st.session_state:
    st.session_state.show_countdown = False
if "cooldown_end" not in st.session_state:
    st.session_state.cooldown_end = 0

placeholder = st.empty()

if not st.session_state.show_countdown:
    if st.button("Resend Code"):
        st.success("✅ Code sent to your email!")
        # Set cooldown for 30 seconds (easy to test)
        st.session_state.cooldown_end = time.time() + 30
        st.session_state.show_countdown = True
        st.rerun()

if st.session_state.show_countdown:
    remaining = int(st.session_state.cooldown_end - time.time())
    if remaining > 0:
        # Render countdown in placeholder
        mins, secs = divmod(remaining, 60)
        placeholder.info(f"Next resend in: {mins:02d}:{secs:02d}")
        # Force rerun after 1 second
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.show_countdown = False
        st.rerun()
