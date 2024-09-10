import os
import shutil
import ollama
import google.generativeai as genai

model = "qwen2:1.5b"
genai.configure(api_key="")

def get_structure(folders, file):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f'I have these folders called {folders}. And I have these file(s) called {files}. Can you sort these files into the folders I have given? Please tell me in one sentence.')
    print(f"Response from Gemini: {response.text}")

    return response.text

def get_folder_for_file(file, folders, gemini_response):
    response_content = ollama.generate(model=model, prompt=f'`Based on this data"{gemini_response}"`. Where does {file} go?')

    print(f"Response from Gwen: {file} = {response_content["response"]}")
    
    for folder in folders:
        if folder in response_content["response"]:
            return folder

directory = os.getcwd()

folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f)) and f != 'qwen1']

files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != 'main.py']

print(f"Folders: {folders}")
print(f"Files: {files}")

response = get_structure(folders, files)

for file in files:
    target_folder = get_folder_for_file(file, folders, response)
    if target_folder:
        source_path = os.path.join(directory, file)
        target_path = os.path.join(directory, target_folder, file)
        
        shutil.move(source_path, target_path)
        print(f"Moved {file} to {target_folder}")
    
