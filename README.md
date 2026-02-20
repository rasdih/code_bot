# 💻 NeuralCode Assistant

A powerful local AI-powered code assistant built with Streamlit and Ollama. Generate, analyze, debug, and optimize code using state-of-the-art language models running locally on your machine.

## Features

- 🤖 **Local AI Models**: Run language models locally using Ollama
- 💬 **Interactive Chat Interface**: Seamless conversation-based code generation
- 🔄 **Multiple AI Models**: Switch between different models (Qwen, Mistral, Neural Chat)
- 📝 **Code Generation**: Generate clean, well-formatted code with explanations
- 🔍 **Code Analysis**: Analyze and understand existing code
- 🐛 **Debugging**: Get help debugging your code
- ⚡ **Performance Optimization**: Optimize your code for better performance
- 💾 **Chat History**: Keep track of recent conversations
- ⚙️ **Customizable Settings**: Adjust temperature and token limits

## Requirements

- Python 3.8+
- Streamlit
- Ollama (for running local models)
- ollama Python library

## Installation

### 1. Install Ollama

Download and install Ollama from [ollama.ai](https://ollama.ai)

### 2. Pull Required Models

```bash
ollama pull qwen2.5-coder:3b
ollama pull mistral:7b
ollama pull neural-chat:7b
```

### 3. Install Python Dependencies

```bash
pip install streamlit ollama
```

### 4. Clone or Download This Repository

```bash
git clone <repository-url>
cd NeuralCode-Assistant
```

## Usage

### Start Ollama Service

Before running the app, make sure Ollama is running:

```bash
ollama serve
```

### Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

The app will open in your default web browser at `http://localhost:8501`

## How to Use

### Main Chat Interface
- Type your code requests in the chat input at the bottom
- The AI will generate responses in real-time
- Chat history is displayed in the main area

### Sidebar Features

**Search Programs**: Filter recent conversations by name

**Recent Programs**: Quick access to your recent chat sessions:
- 🧠 GPT-4 Analysis
- 💻 Code Assistant
- ✍️ Creative Writer
- 📊 Data Scientist
- 🌐 Language Tutor
- ∑ Math Solver

**Settings**:
- **Temperature**: Controls creativity (0.0 = focused, 1.0 = creative)
- **Max Tokens**: Maximum length of AI responses
- **Model Selection**: Choose between available models

**Action Buttons**:
- 🆕 **New Chat**: Start a fresh conversation
- 🧹 **Clear Chat**: Clear current conversation history

### Quick Actions

When starting a new chat, use quick action buttons:
- 🔍 **Analyze**: Request code analysis
- ✨ **Create**: Generate new code
- 🐛 **Debug**: Get debugging help
- 🚀 **Optimize**: Optimize existing code

## Configuration

### Temperature Settings
- **0.0 - 0.3**: Best for code generation (focused, deterministic)
- **0.4 - 0.7**: Balanced creativity and accuracy
- **0.8 - 1.0**: Most creative responses (less predictable)

### Model Recommendations
- **qwen2.5-coder:3b**: Fast, lightweight, excellent for coding
- **mistral:7b**: Balanced performance and quality
- **neural-chat:7b**: General-purpose, conversational

### Max Tokens
- **256**: Short responses
- **512**: Medium responses
- **1024**: Long responses (default)
- **2048**: Very detailed responses

## System Requirements

- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: At least 5GB for models
- **GPU** (optional): NVIDIA GPU with CUDA for faster inference

## Troubleshooting

### "Connection refused" Error
- Make sure Ollama is running with `ollama serve`
- Check that Ollama is accessible on `http://localhost:11434`

### Model Not Found
- Pull the model first: `ollama pull <model-name>`
- Verify models are installed: `ollama list`

### Slow Response Times
- Reduce max tokens
- Lower temperature slightly
- Use a faster model like `qwen2.5-coder:3b`
- Increase GPU allocation if using GPU

### Memory Issues
- Close other applications
- Reduce max tokens
- Use a smaller model

## File Structure

```
NeuralCode-Assistant/
├── streamlit_app.py       # Main application
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

## Dependencies

```
streamlit>=1.28.0
ollama>=0.0.1
```

## Project Structure

### Main Sections

1. **Page Configuration**: Streamlit settings
2. **Session State**: Chat history and program tracking
3. **Sidebar**: Navigation and settings
4. **Main Chat Area**: Message display and input
5. **Quick Actions**: Shortcut buttons for common tasks

## Tips & Tricks

### Best Practices
- Keep conversations focused for better results
- Use specific, detailed prompts
- Test responses before using in production
- Adjust temperature based on task type

### Example Prompts
```
"Write a Python function to sort a list of dictionaries"
"Debug this code: <paste code>"
"Optimize this SQL query for performance"
"Explain how this JavaScript function works"
```

## System Prompt

The assistant is configured as an expert software engineer that:
- Generates clean, correct, well-formatted code
- Returns code in proper markdown code blocks
- Explains only when explicitly asked
- Focuses on code quality and best practices

## Performance Tips

1. **Start with smaller models** for faster responses
2. **Adjust temperature** to find the right balance
3. **Use specific prompts** for better results
4. **Monitor resource usage** and adjust max tokens
5. **Keep chat history reasonable** to avoid slowdowns

## Limitations

- Responses are generated locally (no internet required)
- Quality depends on selected model
- Large code blocks may be slow on lower-end hardware
- No persistent storage of conversations (chat resets on restart)

## Future Enhancements

- [ ] Chat history persistence
- [ ] Custom model loading
- [ ] Code syntax highlighting improvements
- [ ] Export chat history
- [ ] Voice input support
- [ ] Multi-file code support

## Contributing

Contributions are welcome! Feel free to submit issues and enhancement requests.

## License

This project is open source and available under the MIT License.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify Ollama is installed and running
3. Ensure all models are properly pulled
4. Check system resources (RAM, disk space)

## Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Powered by [Ollama](https://ollama.ai)
- Models provided by open-source communities

## Version

- **Version**: 1.0
- **Last Updated**: 2024

---

Happy coding! 🚀
