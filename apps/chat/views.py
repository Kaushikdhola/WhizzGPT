
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from WhizzGPT import settings
import openai
from django.views.decorators.csrf import csrf_exempt

conversation_history = {}
openai.api_key = settings.OPENAI_API_KEY

def process_message(message):

    message="Provide information in the below concept/question/facts: "+message
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=100,
    )
    return response.choices[0].text.strip()

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'POST':
        incoming_message = request.POST.get('Body')
        
        response_text = process_message(incoming_message)

        response = MessagingResponse()

        response.message(response_text)

        return HttpResponse(str(response))
    else:
        return HttpResponse(status=405)
    
    