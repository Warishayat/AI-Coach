import streamlit as st

# Initialize session state variables if they do not exist
if 'call_active' not in st.session_state:
    st.session_state.call_active = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# UI Layout
st.title("Voice Chat with Local LLM")
st.text("Press 'Start Call' to begin talking and 'Stop Call' to end.")

# Start and Stop buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Start Call"):
        st.session_state.call_active = True
        # Add welcome message to chat history
        st.session_state.chat_history.append("AI Coach: Hello, I am AI Coach. How may I assist you today?")
        
with col2:
    if st.button("Stop Call"):
        st.session_state.call_active = False
        # Clear chat history
        st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    st.write(message)

# Voice input processing only when the call is active
if st.session_state.call_active:
    st.write("Listening... Please speak into the microphone.")
    
    # Simulate real-time voice input (no actual recording)
    # Here you can add functionality to simulate transcription (e.g., typing a message manually)
    transcription = st.text_input("Enter your message here (Simulating voice input):")
    
    if transcription:
        st.session_state.chat_history.append(f"You: {transcription}")
        
        # Simulating LLM response
        response = f"AI Coach: I received your message '{transcription}', let me assist you."
        st.session_state.chat_history.append(response)
        
        # Display updated chat history
        for message in st.session_state.chat_history:
            st.write(message)

