import sounddevice as sd
from scipy.io.wavfile import write
import assemblyai as aai

fs = 44100  # Sample rate
#dynamic recording, start for loop that increments by 1 before recording starts and have user input number to stop
seconds = 3  # Duration of recording




aai.settings.api_key = "get ur own api key!!!"
transcriber = aai.Transcriber()

#create menu to record audio before recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 


transcript = transcriber.transcribe("output.wav")
print(transcript.text)