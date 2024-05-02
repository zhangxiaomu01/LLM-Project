Prompt Logs
===========
*** A list of logs tested ***


# 2024-05-02
*** Updates the log with the actual device tag defined in the emulator project. ***
-----------------------------------------------------------------------------------
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
        "[\
            {"action" ":" "Navigate", "objectList : [de_01]"},\
            {"action" ":" "grabObject", "objectList : [de_01]"},\
            {"action" ":" "Navigate", "objectList : [de_04]"},\
            {"action" ":" "openObject", "objectList : [de_04]"},\
            {"action" ":" "pickupObjectWith", "objectList : [de_14, sa_01]"},\
        ]"\
        
        Example2: \
        Task description: Pre-warm ECM in the 37 degree water bath.\
        High level Plan: \
        "[\
            {"action" ":" "Navigate", "objectList : [sa_01]"},\
            {"action" ":" "grabObject", "objectList : [sa_01]"},\
            {"action" ":" "Navigate", "objectList : [de_13]"},\
            {"action" ":" "putObjectInto", "objectList : [sa_01, de_13]"},\
            {"action" ":" "waitForCondition", "objectList : [sa_01]", "conditionList : [37 degree]"},\
        ]"\
        
        Example3: \
        Task description: Thaw extracellular matrix (ECM; Matrigel or Cultrex) compounds in a 4°C cooling bench in the refrigerator.\
        High level Plan: \
        "[\
            {"action" ":" "Navigate", "objectList : [sa_01]"},\
            {"action" ":" "grabObject", "objectList : [sa_01]"},\
            {"action" ":" "Navigate", "objectList : [de_08]"},\
            {"action" ":" "openObject", "objectList : [de_08]"},\
            {"action" ":" "putObjectInto", "objectList : [sa_01, de_08]"},\
            {"action" ":" "waitForCondition", "objectList : [sa_01]", "conditionList : [4 degree]"},\
        ]"\
        ```\
    Task description: Pre-warm a 12-well plate in a 37°C CO2 incubator. \
    Next plan:
    """
------------------------------------------------------------------------------------------------------
Result
------------------------------------------------------------------------------------------------------
'''
{
    "action": "Navigate",
    "objectList": ["de_01"]
},
{
    "action": "grabObject",
    "objectList": ["de_01"]
},
{
    "action": "Navigate",
    "objectList": ["de_05"]
},
{
    "action": "openObject",
    "objectList": ["de_05"]
},
{
    "action": "putObjectInto",
    "objectList": ["de_01", "de_05"]
},
{
    "action": "waitForCondition",
    "objectList": ["de_01"],
    "condition": "37 degree"
}
'''

# 2024-03-24
------------------------------------------------------------------------------------------------------
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
------------------------------------------------------------------------------------------------------
Result
------------------------------------------------------------------------------------------------------
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