
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import os
import json
from load_dotenv import load_dotenv
import streamlit as st

load_dotenv()

from PIL import Image


choose_prompt = PromptTemplate.from_template(""" 
You are a sprite-sheet designer designing a character for this description {description}. 
But, you are already given a directory of assets called {parent_name}. This directory may contain   
other nested directories, or base sprite-sheet assets. Your task is to choose the best option
to take at this junction. 

Here are the contents of this directory. {contents}
Return a json dictionary in your answer. The JSON should have the following key-value pairs ONLY.

is_dir: a boolean representing whether you are choosing to select a directory (TRUE) or a file (FALSE)
name: the name of the file/directory you choose.

Good luck!

Do not choose any COMPLETE files! Do not choose .xcf files! You do not HAVE to choose something. If nothing is relevant, pass the empty string in [name]
If there are numbered files with no description, choose one at random!
""")

model = ChatOpenAI(model="gpt-4")
choose_chain = LLMChain(llm=model, prompt=choose_prompt)

def read_directory_into_dict(directory_path):
    """
    Recursively reads a directory and its subdirectories into a nested dictionary structure.

    :param directory_path: The path to the directory to be read.
    :return: A nested dictionary where each key is a directory or file, 
             with directories mapping to another dictionary of their contents,
             and files mapping to None.
    """
    dir_dict = {}
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            dir_dict[item] = read_directory_into_dict(item_path)
        else:
            dir_dict[item] = None  # Here, setting file value to None
    return dir_dict

def build_spritesheet(tree, path, selected=set(), description=""):
    if tree is None:    return
    contents = "\n".join([json.dumps({'name': key, 'is_dir': tree[key] is not None}) for key in list(tree.keys())])
    decision = json.loads(choose_chain.run(
        description=description,
        parent_name=path,
        contents=contents,
    ))
    assert('is_dir' in list(decision.keys()) and 'name' in list(decision.keys()))
    is_dir = decision.get('is_dir')
    fpath = decision.get('name')
    if is_dir:   build_spritesheet(tree[fpath], path+"/"+fpath, selected, description)
    else:       selected.add(path+"/"+fpath)


def img_create(description):
    d = read_directory_into_dict("./spritesheets")
    s = set()
    for k in list(d.keys()):
        build_spritesheet(d[k], os.getcwd()+"/spritesheets/"+k, s, description)
    s_lst = list(s)
    img_1 = s_lst[0]
    canvas_size = (832, 1344)
    base_image = Image.new('RGBA', canvas_size)

    for img in s_lst:
        if not ".png" in img:   continue
        new_img = Image.open(img)
        if new_img.mode != 'RGBA':  new_img = new_img.convert('RGBA')
        base_image.paste(new_img, (0, 0), new_img)

    st.image(base_image)


st.title("AI-Sprite Generator")

desc = st.text_input("Enter a description here")

submit = st.button("Submit")

if submit:
    img_create(description=desc)
    