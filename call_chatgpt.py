import openai

# Set up the OpenAI API client
openai.api_key = "YOUR_API_KEY"

# Set up the model and prompt
model_engine = "text-davinci-003"

# Change this to take the output from whisper as input
# with appropriate details added, e.g. 'give output as json' etc.
prompt = "Hello, how are you today?"

# prompt = stuff read in from the whisper-generated txt file
# plus clarifications like convert this to json format
# which can be read in by azure resources api

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text

# save this to next txt? for passing to azure resources api
print(response)