# Image Transcription Tool

A Python script that uses OpenAI's GPT-4 Vision API to transcribe text from images.

## Prerequisites

- Python 3.x
- OpenAI API key
- Required Python packages:
  ```bash
  pip install openai
  ```

## Setup

1. Create a file named `APIcred.py` in the same directory with your OpenAI API key:
   ```python
   api_key = "your-api-key-here"
   ```

2. Ensure the script `Transcribenotes.py` is in your working directory.

## Usage

### Command Line

```bash
python Transcribenotes.py <path_to_image> --transcription_path <path_to_transcriptionfile>
```

#### Arguments:
- `--image_path`: Path to the image you want to transcribe (required)
- `--transcription_path`: Path where you want to save the transcription (optional)
  - If not specified, the transcription will be saved next to the image with "_transcribe.txt" suffix

### Example

```bash
python Transcribenotes.py --image_path "testimage.jpg"
```

This will transcribe the text from "testimage.jpg" and save the transcription to "testimage_transcribe.txt" in the same directory.

## Output

- The transcribed text will be printed to the console
- A text file containing the transcription will be saved at the specified location
- A confirmation message will show where the transcript was saved

## Note

Make sure your image is in a supported format (JPEG, PNG, etc.) and is clearly readable for best results.