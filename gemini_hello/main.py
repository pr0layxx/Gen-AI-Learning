from google import genai


client = genai.Client(
    api_key= "API-KEY"
)

interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)