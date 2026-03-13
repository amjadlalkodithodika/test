import streamlit as st
import time

# Initialize session state
if "show_countdown" not in st.session_state:
    st.session_state.show_countdown = False
if "cooldown_end" not in st.session_state:
    st.session_state.cooldown_end = 0
if "mail_sent_time" not in st.session_state:
    st.session_state.mail_sent_time = 0

# Create placeholders
button_placeholder = st.empty()
message_placeholder = st.empty()

if not st.session_state.show_countdown:
    # Render the button inside the placeholder
    if button_placeholder.button("Resend Code"):
        # Simulate sending mail
        st.session_state.mail_sent_time = time.time()
        st.session_state.cooldown_end = time.time() + 30
        st.session_state.show_countdown = True
        st.rerun()

if st.session_state.show_countdown:
    remaining = int(st.session_state.cooldown_end - time.time())
    if remaining > 0:
        mins, secs = divmod(remaining, 60)
        # Replace the button with countdown text in the same spot
        button_placeholder.markdown(
            f"""
            <span style="
                display:inline-block;
                padding:0.5em 1em;
                border:1px solid #666;
                border-radius:4px;
                background-color:#222;
                color:#FFD700;
                font-weight:bold;
                text-align:center;">
                Next resend in: {mins:02d}:{secs:02d}
            </span>
            """,
            unsafe_allow_html=True
        )

        # Show mail sent message only for 3 seconds
        if time.time() - st.session_state.mail_sent_time < 3:
            message_placeholder.success("📧 Code was sent to your email!")

        time.sleep(1)
        st.rerun()
    else:
        st.session_state.show_countdown = False
        st.session_state.mail_sent_time = 0
        st.rerun()
