from dotenv import load_dotenv
load_dotenv()

def mock_twitch_event():
    return {"user": "demo_user", "text": "hello world"}

def generate_reply(text: str) -> str:
    return text.upper()

if __name__ == "__main__":
    ev = mock_twitch_event()
    reply = generate_reply(ev["text"])
    print(f"[DEMO] user={ev['user']} text={ev['text']} -> reply={reply}")
