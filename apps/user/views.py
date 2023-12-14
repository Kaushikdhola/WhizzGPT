
from twilio.rest import Client
from django.conf import settings

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
twilio_phone_number = settings.TWILIO_PHONE_NUMBER

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body="Hello from Twilio!",
    from_=twilio_phone_number,
    to="17828826892"
)

print(f"Message sent with SID: {message.sid}")

# from django.http import HttpResponse
# from twilio.twiml.messaging_response import MessagingResponse
# from django.conf import settings
# import openai

# def process_message(message):
#     # Send the user message to ChatGPT
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=message,
#         max_tokens=100,
#         api_key=settings.OPENAI_API_KEY,
#     )
#     return response.choices[0].text.strip()

# def whatsapp_webhook(request):
#     # Handle incoming WhatsApp messages
#     incoming_message = request.POST.get('Body', '')
#     response_text = process_message(incoming_message)

#     # Send the response back to the user via WhatsApp
#     response = MessagingResponse()
#     response.message(response_text)

#     return HttpResponse(str(response))
