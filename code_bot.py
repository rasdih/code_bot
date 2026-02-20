import streamlit as st
import ollama
from datetime import datetime, timedelta
import json

# ====================
# PAGE CONFIGURATION
# ====================
st.set_page_config(
    page_title="💻 NeuralCode Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================
# INITIALIZE SESSION STATE
# ====================

# Chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are an expert software engineer. "
                "Generate clean, correct, and well-formatted code. "
                "Return code inside proper markdown code blocks. "
                "Explain only if explicitly asked."
            )
        }
    ]

# Recent programs
if "recent_programs" not in st.session_state:
    st.session_state.recent_programs = [
        {"name": "GPT-4 Analysis", "icon": "🧠", "time": "2 hours ago", "date": datetime.now() - timedelta(hours=2)},
        {"name": "Code Assistant", "icon": "💻", "time": "30 min ago", "date": datetime.now() - timedelta(minutes=30)},
        {"name": "Creative Writer", "icon": "✍️", "time": "1 hour ago", "date": datetime.now() - timedelta(hours=1)},
        {"name": "Data Scientist", "icon": "📊", "time": "5 hours ago", "date": datetime.now() - timedelta(hours=5)},
        {"name": "Language Tutor", "icon": "🌐", "time": "1 day ago", "date": datetime.now() - timedelta(days=1)},
        {"name": "Math Solver", "icon": "∑", "time": "2 days ago", "date": datetime.now() - timedelta(days=2)},
    ]

# Current program
if "current_program" not in st.session_state:
    st.session_state.current_program = "NeuralCode Assistant"

# ====================
# SIDEBAR
# ====================
with st.sidebar:
    st.title("NeuralChat")
    
    # Search box
    search_query = st.text_input(
        "🔍 Search programs",
        placeholder="Search...",
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Recent Programs Section
    st.subheader("Recent Programs")
    
    filtered_programs = st.session_state.recent_programs
    if search_query:
        filtered_programs = [p for p in filtered_programs if search_query.lower() in p["name"].lower()]
    
    for idx, program in enumerate(filtered_programs[:6]):
        if st.button(
            f"{program['icon']} {program['name']}",
            key=f"program_{idx}",
            use_container_width=True,
            help=f"Load {program['name']}"
        ):
            st.session_state.current_program = program['name']
            st.session_state.messages = st.session_state.messages[:1]  # Reset to system prompt
            st.rerun()
    
    st.divider()
    
    # Settings Section
    st.subheader("⚙️ Settings")
    
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.1,
        help="Lower = more focused, Higher = more creative"
    )
    
    max_tokens = st.slider(
        "Max Tokens",
        min_value=256,
        max_value=2048,
        value=1024,
        step=256,
        help="Maximum length of response"
    )
    
    model_choice = st.selectbox(
        "Model",
        ["qwen2.5-coder:3b", "mistral:7b", "neural-chat:7b"],
        help="Select the AI model to use"
    )
    
    st.divider()
    
    # Action Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🆕 New Chat", use_container_width=True):
            st.session_state.messages = st.session_state.messages[:1]
            st.session_state.current_program = "NeuralCode Assistant"
            st.rerun()
    
    with col2:
        if st.button("🧹 Clear Chat", use_container_width=True):
            st.session_state.messages = st.session_state.messages[:1]
            st.rerun()
    
    # Info Section
    st.divider()
    st.info("🤖 **NeuralCode** - Powered by Ollama Local Models")

# ====================
# MAIN CHAT AREA
# ====================

# Header
st.title(f"💻 {st.session_state.current_program}")

# Display Chat History
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Chat Input
user_input = st.chat_input(
    "Ask for code...",
    key="chat_input"
)

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Add to history
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    
    # Trim history
    MAX_HISTORY = 10
    trimmed_messages = [st.session_state.messages[0]] + st.session_state.messages[-MAX_HISTORY:]
    
    # Call Ollama with streaming
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_reply = ""
        
        try:
            stream = ollama.chat(
                model=model_choice,
                messages=trimmed_messages,
                stream=True,
                options={
                    "temperature": temperature,
                    "num_predict": max_tokens
                }
            )
            
            for chunk in stream:
                token = chunk["message"]["content"]
                full_reply += token
                placeholder.markdown(full_reply + "▌")
            
            placeholder.markdown(full_reply)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            full_reply = f"Error: {str(e)}"
    
    # Add assistant response to history
    st.session_state.messages.append(
        {"role": "assistant", "content": full_reply}
    )
    
    # Update recent programs
    current_time = datetime.now()
    program = next(
        (p for p in st.session_state.recent_programs if p["name"] == st.session_state.current_program),
        None
    )
    if program:
        program["date"] = current_time
        program["time"] = "Just now"
        st.session_state.recent_programs.sort(key=lambda x: x["date"], reverse=True)
    
    st.rerun()

# ====================
# QUICK ACTIONS SECTION
# ====================
if len(st.session_state.messages) == 1:  # Only show if no messages
    st.divider()
    st.subheader("Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🔍 Analyze", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Analyze: "})
            st.rerun()
    
    with col2:
        if st.button("✨ Create", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Create: "})
            st.rerun()
    
    with col3:
        if st.button("🐛 Debug", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Debug: "})
            st.rerun()
    
    with col4:
        if st.button("🚀 Optimize", use_container_width=True):
            st.session_state.messages.append({"role": "user", "content": "Optimize: "})
            st.rerun()