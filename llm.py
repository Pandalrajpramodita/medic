import google.generativeai as genai

genai.configure(api_key="AIzaSyCkuEAV9pk8iujerwMCo1-vP0iHdqX_KPs")

model=genai.GenerativeModel(model_name="gemini-2.0-flash")

chat=model.start_chat(history=[])
while True:
  prmt=input()
  if(prmt=="exit"):
   break


res=chat.send_message(prmt)
print(res.text)