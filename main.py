from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import speech_recognition as sr

# # Step 1: Extract audio from video
# video = VideoFileClip("your_video.mp4")
# video.audio.write_audiofile("extracted_audio.wav")

# # Step 2: Convert audio to .wav format
# audio = AudioSegment.from_file("extracted_audio.wav")
# audio.export("converted_audio.wav", format="wav")

# Step 3: Transcribe the audio file
r = sr.Recognizer()
text = ''  # Define text before the try block
with sr.AudioFile('converted_audio.wav') as source:
    audio_text = r.listen(source)
    try:
        text = r.recognize_google(audio_text)
    except:
        print('Sorry.. run again...')

# Step 4: Write the transcription to a text file
with open('transcription.txt', 'w') as f:
    f.write(text)