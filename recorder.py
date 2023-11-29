import pyaudio
import wave

# Initialize PyAudio and Whisper
audio = pyaudio.PyAudio()

def record_and_transcribe():
    # Start recording from the microphone
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    print("Recording...")

    frames = []

    try:
        while True:
            data = stream.read(2048)
            #data = stream.read(2048, exception_on_overflow=False)
            frames.append(data)

            # Save the recorded data as a WAV file
            wf = wave.open("temp.wav", "wb")
            wf.setnchannels(1)
            wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(16000)
            wf.writeframes(b''.join(frames))
            wf.close()

    except KeyboardInterrupt:
        # Stop recording
        print("Stopped recording.")
        stream.stop_stream()
        stream.close()
        audio.terminate()

if __name__ == "__main__":
    record_and_transcribe()

