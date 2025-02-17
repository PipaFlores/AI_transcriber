#%%
import base64
import os
import argparse
import APIcred
from openai import OpenAI

#%% OpenAI API Key & Prompt
## Replace with your own key
api_key = APIcred.api_key
Prompt = "Transcribe the written content in this image"
client = OpenAI(api_key=api_key)

# Use in command line as python ./Transcribenotes.py <path_to_image> --transcription_path <path_to_transcriptionfile>

#%% functions
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def transcribe_image (image_path, transcription_path = None):
    
    if transcription_path == None:
       transcription_path = os.path.splitext(image_path)[0] + "_transcribe.txt"

    base64_image = encode_image(image_path)


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": Prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )

    print(response.choices[0].message.content)

    transcription = response.choices[0].message.content

    with open(transcription_path, 'w') as file:
        file.write(transcription)
    print ("-----" + "\n" + f"Transcript successfully saved at {transcription_path}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Transcribe Image")
    parser.add_argument("--image_path", default=r'C:\LocalData\pabflore\OpenAI-testi\Testis\Vision\testimage.jpg',type=str, help="Path to the image file")
    parser.add_argument("--transcription_path", type=str, help="Optional path for the output transcription text file")
    args = parser.parse_args()
    return args


#%%
if __name__ == "__main__":
    args = parse_arguments()
    image_path = args.image_path
    transcription_path = args.transcription_path if args.transcription_path else os.path.splitext(image_path)[0] + "_transcribe.txt"
    transcribe_image(image_path, transcription_path)



