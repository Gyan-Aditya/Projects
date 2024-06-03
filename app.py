# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 02:24:59 2024

@author: KIIT
"""
import openai
import os
import zipfile

openai.api_key = 'sk-proj-TQrgbgVdaYQutibCVcLuT3BlbkFJM9DRTvZltLcdSBR1P36F'

def generate_response(prompt, max_tokens=150):
    try:
        res = openai.Completion.create(
            engine="text-davinci-003",  # This is engine can handle most of the prompt
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.6
        )
        return res.choices[1].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def create_file_structure(user_input):
    prompt = f"Generate a file structure for a project based on the following requirements: {user_input}"
    file= generate_response(prompt)
    return file

def create_files(file, user_input):
    file_contents = {}
    lines = file.split("\n")
    for line in lines:
        if line.strip():
            filename = line.strip()
            content_prompt = f"Generate the content for {filename} in a project with the following requirements: {user_input}"
            file_contents[filename] = generate_response(content_prompt, max_tokens=500)
    return file_contents

def save_files(file_contents):
    os.makedirs("project", exist_ok=True)
    for filename, content in file_contents.items():
        file_path = os.path.join("project", filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            file.write(content)

def zip_files(directory):
    zip_file = f"{directory}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))
    return zip_file

if __name__ == "__main__":
    user_input = input("Enter a brief description of the application you want to build: ")

    print("Generating file structure...")
    file = create_file_structure(user_input)
    print("File structure generated:")
    print(file)

    print("Generating files...")
    file_contents = create_files(file, user_input)

    print("Saving files...")
    save_files(file_contents)

    print("Creating zip archive...")
    zip_filename = zip_files("generated_project")

    print(f"Project files have been zipped into {zip_filename}")
