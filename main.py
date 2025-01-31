# %%
# !pip install roboflow
# !pip install inference_sdk
# !pip install python-dotenv

# %%
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
from inference_sdk import InferenceHTTPClient

# %%
# Load .env file
load_dotenv()

# %%
class Conversation:
    def __init__(self, history, default_history=True):

        # Initialize the model
        self.model = "gpt-4o-mini"

        # Initialize history and create the conversation
        if (default_history):
          self.history = [
              {"role": "developer", "content": "You are a helpful chatbot assistant."}
          ]
        else:
          self.history = history

        self.client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    def get_conversation(self):

        # Obtain the entire conversation
        return "\n".join([f"{role}: {text}" for role, text in self.history])

    def get_response(self, question):

        # Append question to history
        self.history.append({"role": "user", "content": question})

        # Obtain response from model
        response = self.client.chat.completions.create(
            messages=self.history,
            model="gpt-4o-mini",
        )

        # Append response to history
        self.history.append({"role": "assistant", "content": response.choices[0].message.content})

        # Print user query and response
        print(f"you: {question}\nassistant: {response.choices[0].message.content}")


# %%
def main_process():
  
  # Create an introductory initial prompt
  initial_prompt = """Hello! I am a smart assistant designed to analyze images and detect whether they contain cigarettes. If I find one, I'll also provide insights into the health risks of smoking.

To get started, follow these steps:
1️⃣ When you're ready to upload an image, type 'UPLOAD IMAGE' and press Enter.
2️⃣ Upload the file to the project directory.
3️⃣ Then, type the file name along with its extension (e.g., image.jpg) to begin analysis.

If you ever want to end our session, simply type 'STOP'.

Let's begin!"""

  print(initial_prompt)

  # Provide developer command to the chatbot and initialize the conversation object
  initial_history = [
      {"role": "developer", "content": "You are a smart assistant designed to analyze images and detect whether they contain cigarettes. If you find one, you will also provide insights into the health risks of smoking."},
      {"role": "assistant", "content": initial_prompt}
      ]
  conversation = Conversation(initial_history, False)

  # Start the main loop
  while(True):

    user_input = input()

    # Handle image upload
    if (user_input == "UPLOAD IMAGE"):
      image = access_image(conversation)
      detect_cigarette(image, conversation)

    # End conversation for particular input
    elif (user_input == "STOP"):
      print("Nice conversation :)")
      break

    # Any other input
    else:
      conversation.get_response(user_input)


# %%
def access_image(conversation):
  
  # Upload instructions
  upload_prompt = "Upload the image in the test_images folder in the project directory.\nThen type the name of the file along with extension."
  print(upload_prompt)

  image = input()

  # Update conversation
  conversation.history.extend([
      {"role": "assistant", "content": upload_prompt},
      {"role": "user", "content": image},
  ])

  return "test_images/" + image


# %%
def detect_cigarette(image, conversation):
  
  # Initialize the Roboflow inference client with API authentication
  CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=os.getenv("ROBOFLOW_API_KEY")
  )

  # Send image to roboflow's API and obtain a prediction using a publicly available smoking detection computer vision model
  result = CLIENT.infer(image, model_id="smoking-detection-yzewv/1")

  if (True in list(map(lambda prediction: prediction["confidence"] > 0.5, result["predictions"]))): # Set confidence threshold to 0.5
    detection_result = "This image contains a cigarette.\nSmoking poses serious health risks, including lung cancer, heart disease, and respiratory issues. It can also lead to addiction due to nicotine. Quitting smoking can significantly improve overall health and increase life expectancy."
    print(detection_result)
    conversation.history.append({"role": "assistant", "content": detection_result})

  else:
    detection_result = "There are no cigarettes in this image."
    print(detection_result)
    conversation.history.append({"role": "assistant", "content": detection_result})

  return

# %%
main_process()

