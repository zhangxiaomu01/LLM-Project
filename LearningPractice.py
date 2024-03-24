### Prompt tuning practice
import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(
    # 输入转发API Key
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url="https://api.chatkore.com/v1/"
)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

prompt = f"""Create a high-level plan for completing a lab task \
      using the allowed actions and usable objects. You can find examples \
      delimited by triple backticks. Please format the result the same as the example.\
    Allowed actions: Navigate, openObject, grabObject, putObject, disinfect, centrifuge, putObjectInto, \
        pickupObjectWith, extractObject, transferObejct, changeObject, mixObject, waitForCondition \
    
    ```Example1:
        Task description: Put the tweezers into the container, then grab the sample with the tweezers.\
        High level Plan: Navigate tweezers, grabObject tweezers, Navigate container, openObject container, \
        pickupObjectWith tweezers sample.\
        
        Example2: \
        Task description: Pre-warm sample in the 37 degree water bath.\
        High level Plan: Navigate water bath, putObjectInto sample water bath, waitForCondition sample 37 degree\
        
        Example3: \
        Task description: Thaw extracellular matrix (ECM; Matrigel or Cultrex) compounds in a 4°C cooling rack in the refrigerator.\
        High level Plan: grabObject extracellular matrix (ECM; Matrigel or Cultrex) compounds, Navigate refrigerator, \
        openObject refrigerator, putObjectInto extracellular matrix (ECM; Matrigel or Cultrex) compounds cooling rack, 
        waitForCondition extracellular matrix (ECM; Matrigel or Cultrex) compounds 4 degree\
        ```\
        
    Task description: Pre-warm a 24-well plate in a 37°C CO2 incubator. \
    Next plan:
    """

response = get_completion(prompt) 
print(response)
