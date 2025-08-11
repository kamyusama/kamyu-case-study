from dotenv import load_dotenv
load_dotenv()

def send_one_caption(text="HELLO FROM DEMO"):
    print(f"[DEMO] would send caption once to OBS: {text}")

if __name__ == "__main__":
    send_one_caption()
