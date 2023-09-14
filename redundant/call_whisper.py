import openai
# add your API key here
openai.api_key = "YOUR_API_KEY"

# transcript using openai module
audio_file = open("./sample_audio_1.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# save the below to a txt file (instead of printing) 
# so that it can be read in by call_chatgpt.py
print(transcript['text'])