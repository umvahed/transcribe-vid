# transcribe-vid

## Step 1: Extract audio from video
```
video = VideoFileClip("your_video.mp4")
video.audio.write_audiofile("extracted_audio.wav")
```

## Step 2: Convert audio to .wav format
```
audio = AudioSegment.from_file("extracted_audio.wav")
audio.export("converted_audio.wav", format="wav")
```
## Step 3: Transcribe the audio file and output to folder

## Setup
Please make sure video and audio file naming conventions are maintained
