import os
from google import genai
from google.genai import types



def generate(user_input):
  client = genai.Client(
      api_key=os.environ.get("GEMINI_API_KEY"),
  )

  model = "gemini-2.0-flash"
  contents = [
      types.Content(
          role="user",
          parts=[
              types.Part.from_text(
                  text=user_input
              ),
          ],
      ),
  ]
  generate_content_config = types.GenerateContentConfig(
      temperature=1,
      top_p=0.95,
      top_k=40,
      max_output_tokens=8192,
      response_mime_type="text/plain",
      system_instruction=[
          types.Part.from_text(
              text="""give res on unit conversion question other wise tell them ask only unit conversion quserion in correct sentence"""
          ),
      ],
  )

  for chunk in client.models.generate_content_stream(
      model=model,
      contents=contents,
      config=generate_content_config,
  ):
    print(chunk.text, end="")


generate()