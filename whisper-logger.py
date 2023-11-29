import pyaudio
import wave
import whisper
import threading
import sys
import select

# Initialize PyAudio and Whisper
audio = pyaudio.PyAudio()
model = whisper.load_model("base")  # or another model size

def record_audio():
    # Start recording from the microphone
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    print("Recording... Press Enter to stop.")

    frames = []

    while True:
        data = stream.read(1024)
        frames.append(data)

        # Stop recording if Enter is pressed
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = input()
            break

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Save the recorded data as a WAV file
    wf = wave.open("temp.wav", "wb")
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Recording stopped. Transcribing...")

def transcribe_audio():
    try:
        result = model.transcribe("temp.wav")
        print("Transcription: " + result["text"])
    except KeyboardInterrupt:
        print("Transcription interrupted. Waiting for user input...")

def main():
    while True:
        command = input("Type 'r' to start recording, 's' to stop transcription, or 'q' to quit: ").strip().lower()
        
        if command == 'r':
            record_thread = threading.Thread(target=record_audio)
            record_thread.start()
            record_thread.join()
            transcribe_audio()
        elif command == 's':
            # Interrupt transcription if it's running
            if transcribe_thread.is_alive():
                transcribe_thread.interrupt()
        elif command == 'q':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()

