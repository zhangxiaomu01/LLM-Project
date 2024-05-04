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
    print(response)
    print("\n")
    return response.choices[0].message.content

prompt = """Create a high-level plan for completing a lab task \
      using the allowed actions and usable object dictionary. Please format the result in a list of json object which 
      has three keys: action, objectList, condition, and replace the object\
          name with object id in the object dictionary. You can find examples delimited by triple backticks. \
    Allowed actions: Navigate, openObject, grabObject, putObject, disinfect, centrifuge, putObjectInto, \
        pickupObjectWith, extractObject, transferObejct, changeObject, mixObject, waitForCondition \
    Usable Object dictionary: ```{{"12 well tissue culture plates", "de_01"},\
	{"15ml tube", "de_02"},\
	{"9ml DMEM", "de_03"}, \
	{"Bench", "de_04"},\
	{"CO2 incubator", "de_05"},\
	{"Dewar", "de_06"},\
	{"Multi-application centrifuge", "de_07"},\
	{"Refrigerator", "de_08"},\
	{"Sample holder", "de_09"},\
	{"Bio-safety cabinet", "de_10"},\
	{"1.5 mL microcentrifuge tube", "de_11"},\
	{"Vial", "de_12"},\
	{"Water bath", "de_13"},\
    {"Tweezers", "de_14"},\
    {"Extracellular matrix compounds (ECM)", "sa_01"},\
	{"WERN 3D base proliferation medium for spheroid culture", "sa_02"},\
	{"3D organoids", "sa_03"},\
	{"Advanced DMEM/F-12", "sa_04"}\
    }```
    
    ```Example1:
        Task description: Put the tissue culture plates onto the bench, then grab the Extracellular matrix compounds with the tweezers.\
        High level Plan: \
        [\
            {"action" : "Navigate", "objectList" : ["de_01"]},\
            {"action" : "grabObject", "objectList" : ["de_01"]},\
            {"action" : "Navigate", "objectList" : ["de_04"]},\
            {"action" : "openObject", "objectList" : ["de_04"]},\
            {"action" : "pickupObjectWith", "objectList" : ["de_14", "sa_01"]},\
        ]\
        
        Example2: \
        Task description: Pre-warm ECM in the 37 degree water bath.\
        High level Plan: \
        [\
            {"action" : "Navigate", "objectList" : ["sa_01"]},\
            {"action" : "grabObject", "objectList" : ["sa_01"]},\
            {"action" : "Navigate", "objectList" : ["de_13"]},\
            {"action" : "putObjectInto", "objectList" : ["sa_01", "de_13"]},\
            {"action" : "waitForCondition", "objectList" : ["sa_01"], "conditionList" : ["37 degree"]},\
        ]\
        
        Example3: \
        Task description: Thaw extracellular matrix (ECM; Matrigel or Cultrex) compounds in a 4°C cooling bench in the refrigerator.\
        High level Plan: \
        [\
            {"action" : "Navigate", "objectList" : ["sa_01"]},\
            {"action" : "grabObject", "objectList" : ["sa_01"]},\
            {"action" : "Navigate", "objectList" : ["de_08"]},\
            {"action" : "openObject", "objectList" : ["de_08"]},\
            {"action" : "putObjectInto", "objectList" : ["sa_01", "de_08"]},\
            {"action" : "waitForCondition", "objectList" : ["sa_01"], "conditionList" : ["4 degree"]},\
        ]\
        ```\
    Task description: Pre-warm a 12-well plate in a 37°C CO2 incubator. \
    Next plan:
    """

'''
[
    {"action" : "Navigate", "objectList" : ["de_01"]},
    {"action" : "grabObject", "objectList" : ["de_01"]},
    {"action" : "Navigate", "objectList" : ["de_05"]},
    {"action" : "openObject", "objectList" : ["de_05"]},
    {"action" : "putObjectInto", "objectList" : ["de_01", "de_05"]},
    {"action" : "waitForCondition", "objectList" : ["de_01"], "conditionList" : ["37 degree"]},
]
'''
'''
ChatCompletion(id='chatcmpl-9KLDJEF9Bus4cwjCVNcyOZGPONYf6', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='[\n    {"action" : "Navigate", "objectList" : ["de_01"]},\n    {"action" : "grabObject", "objectList" : ["de_01"]},\n    {"action" : "Navigate", "objectList" : ["de_05"]},\n    {"action" : "openObject", "objectList" : ["de_05"]},\n    {"action" : "putObjectInto", "objectList" : ["de_01", "de_05"]},\n    {"action" : "waitForCondition", "objectList" : ["de_01"], "conditionList" : ["37 degree"]},\n]', role='assistant', function_call=None, tool_calls=None))], created=1714635133, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='', usage=CompletionUsage(completion_tokens=142, prompt_tokens=858, total_tokens=1000))

'''

'''
UE LOG for testing:
{"id":"chatcmpl-9L2m6xOXkj7u64lqAON5XKvB3AyjR","object":"chat.completion","created":1714802582,"model":"gpt-3.5-turbo-0125","choices":[{"index":0,"message":{"role":"assistant","content":"```json\n[\n    {\"action\" : \"Navigate\", \"objectList\" : [\"de_01\"]},\n    {\"action\" : \"grabObject\", \"objectList\" : [\"de_01\"]},\n    {\"action\" : \"Navigate\", \"objectList\" : [\"de_05\"]},\n    {\"action\" : \"openObject\", \"objectList\" : [\"de_05\"]},\n    {\"action\" : \"putObjectInto\", \"objectList\" : [\"de_01\", \"de_05\"]},\n    {\"action\" : \"waitForCondition\", \"objectList\" : [\"d
e_01\"], \"conditionList\" : [\"37 degree\"]},\n]\n```"},"finish_reason":"stop"}],"usage":{"prompt_tokens":902,"completion_tokens":146,"total_tokens":1048},"system_fingerprint":""} 

[
    {"action" : "Navigate", "objectList" : ["de_01"]},
    {"action" : "grabObject", "objectList" : ["de_01"]},
    {"action" : "Navigate", "objectList" : ["de_05"]},
    {"action" : "openObject", "objectList" : ["de_05"]},
    {"action" : "putObjectInto", "objectList" : ["de_01", "de_05"]},
    {"action" : "waitForCondition", "objectList" : ["de_01"], "conditionList" : ["37 degree"]},
]
'''

response = get_completion(prompt) 
print(response)
