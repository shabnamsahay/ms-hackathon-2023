import openai
import requests

# Set up the OpenAI API client
openai.api_key = "YOUR_API_KEY"

# Set up the model and prompt
model_engine = "gpt-4-0613"

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

function_descriptions = [
    {
        "name": "get_resource_creation_url",
        "descriptionn": "Returns the type of HTTP call (GET, POST, PUT, DELETE, etc.) and the ",
        "parameters": {
            "type": "object",
            "properties": {
                "http_call": {
                    "type": "string",
                    "description": "The HTTP call to be made.",
                    "enum": ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "TRACE", "CONNECT"],
                },
                "resource_url": {
                    "type": "string",
                    "description": "The URL of the resource to be created, updated, or deleted.",
                }
            }
            "required": ["http_call", "resource_url"]
        }
    }
]

query2 = "Get the REST API url to" + query1

response2 = openai.chatcompletions.create(
    model = "gpt-4-0613",
    message =[{"role" : "user", "content" : query2}],
    functions = function_descriptions,
)

message = response2.choices[0].["message"]
http_request_type = message['function_call']['arguments'].get("http_call")
resource_url = message['function_call']['arguments'].get("resource_url")

# Make the HTTP call
if(http_request_type == "GET"):
    response3 = requests.get(resource_url);
elif(http_request_type == "POST"):
    response3 = requests.post(resource_url, data=data);
elif(http_request_type == "PUT"):
    response3 = requests.put(resource_url, data=data);
elif(http_request_type == "DELETE"):
    response3 = requests.delete(resource_url);
elif(http_request_type == "PATCH"):
    response3 = requests.patch(resource_url, data=data);
elif(http_request_type == "HEAD"):
    response3 = requests.head(resource_url);
elif(http_request_type == "OPTIONS"):
    response3 = requests.options(resource_url);
elif(http_request_type == "TRACE"):
    response3 = requests.trace(resource_url);
elif(http_request_type == "CONNECT"):
    response3 = requests.connect(resource_url);

print(response3)
