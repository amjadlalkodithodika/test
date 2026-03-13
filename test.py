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
        # Use markdown with CSS-like styling to match button width
        button_placeholder.markdown(
            f"""
            <div style="
                display:inline-block;
                width:100%;
                text-align:center;
                padding:0.5em;
                border:1px solid #666;
                border-radius:4px;
                background-color:#222;
                color:#FFD700;
                font-weight:bold;">
                Next resend in: {mins:02d}:{secs:02d}
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.show_countdown = False
        st.rerun()
