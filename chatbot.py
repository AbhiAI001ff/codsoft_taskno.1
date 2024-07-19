data = {

 "hi": "Hllo there! I'm a friendly chatbot here to help you.",

 "hello": "Hello! How can I help to you?",

 "what is your name": "they call me chatbot",

 "where are you from": "i am from ai assistence, i am always ready to chat! ",

 "how are you": "I'm fine,How can I assist you today?",

}



def get_response(user_input):

 for pattern, response in data.items():

  if pattern in user_input.lower():

   return response

 return "Could you please rephrase your sentence?"



print("Chatbot: Hi there! I'm a simple chatbot. I'm here to assist you!")

while True:

 user_input = input("You: ")

 if user_input.lower() == 'bye':

  print("Chatbot: Goodbye! Have a nice day! ")

  break

 else:

  response = get_response(user_input)

  print("Chatbot:", response)
