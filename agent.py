import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from agents import Agent, Runner, function_tool

# تحميل مفتاح الـ API من ملف .env
load_dotenv()

# تعريف الأداة (Tool) لسحب تفريغ الفيديو
@function_tool
def extract_transcript(url: str) -> str:
    """Extracts the transcript with timestamps from a YouTube video URL."""
    try:
        import re
        match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
        if not match:
            return "Error: Invalid YouTube URL"
        
        video_id = match.group(1)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        formatted_transcript = []
        for entry in transcript_list:
            minutes = int(entry['start']) // 60
            seconds = int(entry['start']) % 60
            formatted_transcript.append(f"[{minutes:02d}:{seconds:02d}] {entry['text']}")
            
        return "\n".join(formatted_transcript)
    except Exception as e:
        return f"Error extracting transcript: {str(e)}"

# بناء الوكيل (Agent) وإعطائه الأداة
youtube_agent = Agent(
    name="YouTube Transcript Agent",
    instructions="You are a helpful assistant. Use the extract_transcript tool to get video transcripts and answer questions about them accurately.",
    tools=[extract_transcript]
)

def main():
    print("\n🎥 YouTube Transcript Agent is ready!")
    print("Type 'exit' to end.\n")
    
    # حلقة المحادثة
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            break
        if not user_input.strip():
            continue
            
        print("Agent is thinking...", end="\r", flush=True)
        
        # تشغيل الـ Runner الخاص بمكتبة الـ Agents
        result = Runner.run_sync(youtube_agent, user_input)
        
        print(f"Agent: {result.final_output}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()