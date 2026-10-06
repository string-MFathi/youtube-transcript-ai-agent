# 🎥 YouTube Transcript AI Agent

An intelligent, terminal-based AI agent that extracts and analyzes YouTube video transcripts in real-time. Built using Python and the **OpenAI Agents SDK**.

## 🧠 Core Architecture
This project implements the **ReAct (Reasoning and Acting)** logic pattern. Instead of a simple chatbot, this agent operates with autonomy:
1. **Tool Calling:** Equipped with a custom Python tool to scrape YouTube transcripts using `youtube-transcript-api`.
2. **Context Memory:** Maintains conversation history to answer follow-up questions and translate extracted data without losing context.
3. **Decision Making:** The LLM autonomously decides *when* to trigger the extraction tool based on the user's prompt.

## 🚀 Why I Built This
As my first foundational project in **AI Agent Development**, my goal was to master the underlying mechanics of how LLMs interact with external APIs. Instead of relying on heavy, abstracted frameworks, I focused on understanding native tool calling, asynchronous execution, and managing dependency environments in Python.

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/youtube-transcript-ai-agent.git](https://github.com/YourUsername/youtube-transcript-ai-agent.git)
