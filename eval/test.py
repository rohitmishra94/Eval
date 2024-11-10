import requests

# Define the URL for your FastAPI endpoint
url = "http://127.0.0.1:8000/api/openai/judge/pointwise"

# Define the payload with the necessary parameters
data = {
    "prompt": f"""# System_prompt
You are an AI assistant. You will be given a task. You must generate a detailed and long answer. # Question
Single/multi-select question: If "Two people are wearing a Chinese dragon costume in front of an ornate Chinese gazebo with red pillars and the gazebo has two large red lanterns hanging from the roof.", can we conclude "The people are celebrating Chinese New Year."?

 a). yes. b). it is not possible to tell. c). no.""",
    "response": f"""The most accurate answer is **b) it is not possible to tell.** Here's why:

**While the imagery strongly suggests Chinese New Year, we cannot definitively conclude that's the celebration without further context.** 

Here's a breakdown of why:

**Elements that suggest Chinese New Year:**

* **Chinese Dragon Costume:** Dragon dances are a very prominent tradition during Chinese New Year, symbolizing good luck and prosperity.
* **Ornate Chinese Gazebo:**  Gazebos are often seen in Chinese gardens and parks, places where New Year festivities might take place.
* **Red Lanterns:** Red is the color of luck and prosperity in Chinese culture and is heavily featured during Chinese New Year. Lanterns are also common decorations.

**Reasons why it might NOT be Chinese New Year:**

* **Other Chinese Festivals:**  Many other Chinese festivals and celebrations incorporate similar elements like dragon dances, red lanterns, and traditional attire.
* **Cultural Performances:** The scene could depict a cultural performance or parade unrelated to a specific holiday. 
* **Staged Event:** The scene could be part of a play, movie set, or photoshoot with no connection to an actual celebration.

**To definitively conclude it's Chinese New Year,""",
    "metric": "coherence",
    "history": []  # Adjust this based on your endpoint's requirements
}

# Send the POST request with the JSON payload and enable streaming
# response = requests.post(url, json=data, stream=True)

# # Check if the request was successful
# if response.status_code == 200:
#     print("Streaming Response:")
#     # Iterate over the response content as it streams
#     for line in response.iter_lines():
#         # Filter out keep-alive new lines
#         if line:
#             # Decode and print each line of the response
#             print(line.decode('utf-8'))
# else:
#     print("Failed to connect:", response.status_code, response.text)




url = "http://127.0.0.1:8000/api/openai/judge/pairwise"

data_pairwise = {
    'prompt':f"""# System_prompt
You are an AI assistant. You will be given a task. You must generate a detailed and long answer. # Question
Single/multi-select question: If "Two people are wearing a Chinese dragon costume in front of an ornate Chinese gazebo with red pillars and the gazebo has two large red lanterns hanging from the roof.", can we conclude "The people are celebrating Chinese New Year."?

 a). yes. b). it is not possible to tell. c). no.""",
    'response':f"""The answer is **(b) it is not possible to tell**. While the scene described evokes strong imagery associated with Chinese New Year, we cannot definitively conclude that the people are celebrating this specific holiday based solely on the provided information. Here's why:

**Alternative Explanations:**

* **Cultural Performance:** The individuals could be performers in a cultural exhibition, parade, or theatrical production. Chinese dragon costumes and ornate gazebos are common elements in various cultural performances that are not exclusive to Chinese New Year.
* **Festival or Event:**  Many Chinese festivals and events incorporate traditional elements like dragon costumes and gazebos. They could be celebrating a birthday, wedding, or another cultural festival.
* **Tourism or Photography:** The scene could depict tourists or models posing for photographs in a culturally significant location. The presence of the costume and gazebo doesn't automatically signify a celebration. 
* **Decorative Elements:** The gazebo and lanterns might be permanent fixtures in a public park or garden designed with Chinese architectural influences. The people in the dragon costume could be unrelated to any specific event.

**Lack of Contextual Information:**

To confidently conclude that the people are celebrating Chinese New Year, we would need additional contextual clues, such as:

* **Date and Time""",
    'metric':'fluency',
    'history':[],
    'baseline_model_response':f"""The answer is **(b) it is not possible to tell**. Here's why:

* **Chinese dragon costumes** are a common sight in Chinese culture, not just during Chinese New Year. They are used in various festivals, cultural performances, and even everyday celebrations. 
* **Ornate Chinese gazebos with red pillars and lanterns** are also prevalent in Chinese architecture and are not exclusive to Chinese New Year celebrations. They are often found in parks, gardens, and temples. 

While the scene you describe might *suggest* a Chinese New Year celebration, it doesn't definitively prove it.  There could be other reasons for these elements to be present:

* **A cultural performance or festival:** The people could be part of a dragon dance troupe performing at a non-New Year event.
* **A traditional wedding:**  Dragon dances are sometimes incorporated into Chinese weddings.
* **A cultural park or event:**  The gazebo could be part of a themed park or an event showcasing Chinese culture.

**To definitively conclude that the people are celebrating Chinese New Year, we would need additional information, such as:**

* **The presence of other New Year-specific decorations:** Red paper cutouts, banners with "Happy New Year" greetings, or traditional New Year foods.
* **People wearing traditional Chinese New Year clothing:**  Red attire, specific hairstyles, or accessories like hats with tassels.
* **Specific activities associated with Chinese New Year:**  Firecrackers, lion dances, or people giving lucky red envelopes (hongbao). 
"""
}

# Send the POST request with the JSON payload and enable streaming
response = requests.post(url, json=data_pairwise, stream=True)

# Check if the request was successful
if response.status_code == 200:
    print("Streaming Response:")
    # Iterate over the response content as it streams
    for line in response.iter_lines():
        # Filter out keep-alive new lines
        if line:
            # Decode and print each line of the response
            print(line.decode('utf-8'))
else:
    print("Failed to connect:", response.status_code, response.text)
