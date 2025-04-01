import os
import cv2
import base64
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key="sk-627a7f6f36e84ae5a90e69c96c130af4",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


# Function to convert local image to base64
def image_to_base64(image_path):
    image = cv2.imread(image_path)
    _, buffer = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    return f"data:image/jpeg;base64,{image_base64}"


# Function to split AI response into parts and extract the pose name
def split_response(response):
    parts = response.split('\n\n')  # Split by double newlines
    if len(parts) >= 3:
        # Remove the bolded labels and extract pose name from "Correct posture"
        correct_posture = parts[0].replace("**Correct posture:** ", "")
        users_posture = parts[1].replace("**User's posture:** ", "")
        adjustment_suggestions = parts[2].replace("**Adjustment suggestions:** ", "")

        # Extract pose name (assuming it's mentioned in "Correct posture" like "Navasana (Boat Pose)")
        pose_name = "Unknown"
        if "known as" in correct_posture:
            start_idx = correct_posture.index("known as") + len("known as ")
            end_idx = correct_posture.index(")", start_idx) if ")" in correct_posture[start_idx:] else len(
                correct_posture)
            pose_name = correct_posture[start_idx:end_idx + 1].strip()

        return {
            "Pose name": pose_name,
            "Correct posture": correct_posture,
            "User's posture": users_posture,
            "Adjustment suggestions": adjustment_suggestions
        }
    else:
        return {
            "Pose name": "N/A",
            "Correct posture": "N/A",
            "User's posture": "N/A",
            "Adjustment suggestions": "N/A"
        }


# Path to your local yoga image
image_path = "image_test/File1.jpeg"

# Prepare the messages with the local image and modified prompt
messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are a yoga instructor assistant."}],
    },
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": image_to_base64(image_path)
                },
            },
            {
                "type": "text",
                "text": "Analyze the yoga pose in the image and provide feedback in three parts: "
                        "'Correct posture', 'User's posture', and 'Adjustment suggestions'. "
                        "Include the name of the yoga pose in the 'Correct posture' section, "
                        "formatted as 'known as [Sanskrit name]'. "
                        "Use English for the response and clearly label each section as '**Correct posture:** ', "
                        "'**User's posture:** ', and '**Adjustment suggestions:** ' followed by the description."
            },
        ],
    },
]

# Create the completion request
completion = client.chat.completions.create(
    model="qwen-omni-turbo",
    messages=messages,
    modalities=["text"],
    stream=True,
    stream_options={"include_usage": True}
)

# Combine the streaming output into a complete response
full_response = ""
for chunk in completion:
    if chunk.choices and chunk.choices[0].delta.content is not None:
        full_response += chunk.choices[0].delta.content
    elif chunk.usage:
        print(f"Usage: {chunk.usage}")

# Print the full response
print("Full AI Response:")
print(full_response)

# Split and display the response with the pose name
response_parts = split_response(full_response)
print("\nSplit Response:")
print("Pose name:", response_parts["Pose name"])
print("Correct posture:", response_parts["Correct posture"])
print("User's posture:", response_parts["User's posture"])
print("Adjustment suggestions:", response_parts["Adjustment suggestions"])