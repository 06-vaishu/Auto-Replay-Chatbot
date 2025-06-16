from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

command = '''
[8:52 PM, 2/1/2025] Sanika_♥️: Avrlya mazee man zaly aata
[8:53 PM, 2/1/2025] Vaishnavi Handal✨❤️: Tu, ky man
[8:56 PM, 2/1/2025] Sanika_♥️: Ag udya jaychee g
[8:57 PM, 2/1/2025] Sanika_♥️: Tu ganpati la geli hoti photo nhi ka kadhle deva cha g
[9:06 PM, 2/1/2025] Vaishnavi Handal✨❤️: Ag baherun ghetl darshan
[9:19 PM, 2/1/2025] Sanika_♥️: Achha
[9:19 PM, 2/1/2025] Sanika_♥️: Udya jayche madam
[9:20 PM, 2/1/2025] Vaishnavi Handal✨❤️: Mala tr vatt hot thambava
[9:20 PM, 2/1/2025] Vaishnavi Handal✨❤️: Bt jau jaudet
'''
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are openaiwho speak hind as well as englishhe is from indias and coder"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)

