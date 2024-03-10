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


text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""

prompt = f"""Create a high-level plan for completing a household task \
      using the allowed actions and visible objects. You can find an example \
      delimited by triple backticks. \
    Allowed actions: OpenObject, CloseObject, PickupObject, PutObject, ToggleObjectOn,
    ToggleObjectOff, SliceObject, Navigation \
    
    ```Example:
        Task description: Put a heated egg in the sink.
        Completed plan: Navigation fridge, OpenObject fridge, \
        PickupObject egg, CloseObject fridge\
        Visible objects are sink, egg, microwave\
        High level Plan: Navigation microwave, OpenObject microwave, PutObject egg microwave,\
        CloseObject microwave, ToggleObjectOn microwave, ToggleObjectOff microwave,\
        OpenObject microwave, PickupObject egg, CloseObject microwave, Navigation\
        sinkbasin, PutObject egg sinkbasin```\
        
    Task description: Cook a potato and put it into the recycle bin. \
    Completed plan: Navigation fridge, OpenObject fridge, PickupObject potato, \
    CloseObject fridge, Navigation microwave, OpenObject microwave, PutObject potato \
    microwave, CloseObject microwave, ToggleObjectOn microwave, ToggleObjectOff \
    microwave, OpenObject microwave, PickupObject potato, CloseObject microwave \
    Visible objects are microwave, fridge, potato, garbagecan \
    Next plan:
    """

prompt = f"""Create a high-level plan for completing a lab task \
      using the allowed actions and usable objects. You can find an example \
      delimited by triple backticks. Please format the result the same as the example.\
    Allowed actions: OpenObject, CloseObject, PickupObject, PickupObjectWith, PutObject, ToggleObjectOn,
    ToggleObjectOff, SliceObject, Navigation \
    
    ```Example:
        Task description: Put the tweezers into the container, then grab the sample with the tweezers.\
        Usable objects are tweezers, container, sample\
        High level Plan: Navigation tweezers, PickupObject tweezers, Navigation container,
        PickupObjectWith tweezers sample```\
        
    Task description: Take a potato and put it into the recycle bin. \
    Usable objects are potato, recycle bin
    Next plan:
    """

response = get_completion(prompt) 
'''
High level Plan: 
   Navigation potato, PickupObject potato, Navigation recycle bin, PutObject potato

High level Plan: 
Navigation potato, PickupObject potato, Navigation recycle bin, PutObject potato into recycle bin
'''
print(response)
