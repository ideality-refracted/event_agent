from google import genai


def _get_genai_client() -> genai.Client:
  """Returns a client for Gemini inference."""
  return genai.Client(
      vertexai=False,
      api_key=os.environ['GOOGLE_API_KEY'],
  )


def genai_model_inference(contents) -> str:
  client = _get_genai_client()

  response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
  )
  return response.text
