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

prompt = """Create a high-level plan for completing a lab task \
      using the allowed actions and usable object dictionary. Please format the result in a list of json object which 
      has three keys: action, objectList, condition, and replace the object\
          name with object id in the object dictionary. You can find examples delimited by triple backticks. \
    Allowed actions: Navigate, openObject, grabObject, putObject, disinfect, centrifuge, putObjectInto, \
        pickupObjectWith, extractObject, transferObejct, changeObject, mixObject, waitForCondition \
    Usable Object dictionary: ```{"tweezers : t_01", "container : c_01",
                                  "sample : s_01", "extracellular matrix (ECM; Matrigel or Cultrex) compounds : s_02",\
                                "water bath : e_01", "refrigerator : e_02", "cooling rack : e_03", "24-well plate : e_04",\
                                    "CO2 incubator : e_05"}```
    
    ```Example1:
        Task description: Put the tweezers into the container, then grab the sample with the tweezers.\
        High level Plan: \
        "[\
            {"action" ":" "Navigate", "objectList : [t_01]"},\
            {"action" ":" "grabObject", "objectList : [t_01]"},\
            {"action" ":" "Navigate", "objectList : [c_01]"},\
            {"action" ":" "openObject", "objectList : [c_01]"},\
            {"action" ":" "pickupObjectWith", "objectList : [t_01, c_01]"},\
        ]"\
        
        Example2: \
        Task description: Pre-warm sample in the 37 degree water bath.\
        High level Plan: \
        "[\
            {"action" ":" "Navigate", "objectList : [s_01]"},\
            {"action" ":" "grabObject", "objectList : [s_01]"},\
            {"action" ":" "Navigate", "objectList : [e_01]"},\
            {"action" ":" "putObjectInto", "objectList : [s_01, e_01]"},\
            {"action" ":" "waitForCondition", "objectList : [s_01]", "conditionList : [37 degree]"},\
        ]"\
        
        Example3: \
        Task description: Thaw extracellular matrix (ECM; Matrigel or Cultrex) compounds in a 4°C cooling rack in the refrigerator.\
        High level Plan: \
        "[\
            {"action" ":" "Navigate", "objectList : [s_02]"},\
            {"action" ":" "grabObject", "objectList : [s_02]"},\
            {"action" ":" "Navigate", "objectList : [e_02]"},\
            {"action" ":" "openObject", "objectList : [e_02]"},\
            {"action" ":" "putObjectInto", "objectList : [s_02, e_03]"},\
            {"action" ":" "waitForCondition", "objectList : [s_02]", "conditionList : [4 degree]"},\
        ]"\
        ```\
    Task description: Pre-warm a 24-well plate in a 37°C CO2 incubator. \
    Next plan:
    """

'''
[
    {"action": "Navigate", "objectList": ["e_04"]},
    {"action": "grabObject", "objectList": ["e_04"]},
    {"action": "Navigate", "objectList": ["e_05"]},
    {"action": "openObject", "objectList": ["e_05"]},
    {"action": "putObjectInto", "objectList": ["e_04", "e_05"]},
    {"action": "waitForCondition", "objectList": ["e_04"], "condition": ["37 degree"]}
]
'''

response = get_completion(prompt) 
print(response)
