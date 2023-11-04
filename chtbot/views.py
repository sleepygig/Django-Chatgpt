from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse 
import openai


openai_api_key='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'
openai.api_key=openai_api_key
def ask_openai(message):
    response =openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=30,
        n=1,
        stop=None,
        temperature=0.7,   
    )
    #print(response)
    answer=response.choices[0].text.strip()
    return answer

def chtbot(request):
    if request.method=='POST':
    #gererally yh methos pe get req aati url se toh 
    #nrml rendering lekin jb post aye from FE
      message=request.POST.get('message')
      response=ask_openai(message)
      return JsonResponse({'message':message,'response':response}) 
    return render(request,'chatbot.html')
