import sys
import os
import PyPDF2
from langchain import OpenAI
from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
        
os.environ["OPENAI_API_KEY"] = "Your-Openai-Key"

def index_creation(dir_path):
  maximum_input_size = 4096
  num_outputs = 256
  maximum_chunk_overlap = 20
  chunk_size_limit = 600
  prompt_helper = PromptHelper(maximum_input_size, num_outputs, maximum_chunk_overlap, chunk_size_limit=chunk_size_limit)
  
  predictor_llm = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))
  documents = SimpleDirectoryReader(dir_path).load_data()
  index = GPTSimpleVectorIndex(documents, llm_predictor=predictor_llm, prompt_helper=prompt_helper)
  index.save_to_disk('index.json')
  return index
  
def chat_bot(input_index = 'index.json'):
  index = GPTSimpleVectorIndex.load_from_disk(input_index)
  while True:
    query = input('User: \n')
    response = index.query(query, response_mode="compact")
    print ("\nJJ: " + response.response + "\n")

if __name__ == '__main__':
    index = index_creation("data/")
    chat_bot('index.json')

