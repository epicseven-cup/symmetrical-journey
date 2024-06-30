from llama_cpp import Llama
import llama_cpp
import os
import google.generativeai as genai


class DungonMaster:
	def __init__(self):
		pass

	# This will associate the characters and the discord names together
	def asscoicate_characters(self):
		pass

	# This will be used to generate the next scene of the game
	def generate_scenes(self):
		pass
	# This will keep track of what is going on in the stroy so far
	def story(self):
		pass
	# This will be done to talk to users when in case of inacitvily
	def explore(self):
		pass
	# Save the current game state into a file that the model can read into it later, should tell the user a id name that can be used to reference the game
	def save_state(self):
		pass
	# loads a state base on given ids
	def load_state(self):
		pass


class Gemini(DungonMaster):
	def __init__(self):
		genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
		self.model = genai.GenerativeModel("gemini-1.5-flash")
		# Start to save chat history
		self.chat = self.model.start_chat(history=[])
		starter_prompt = open("prompt/starter.txt").read()
		self.chat.send_message(starter_prompt)
		return

	def asscoicate_characters(self, character_summaries):
		result = self.chat.send_message(character_summaries)
		return result.text

	def generate_scenes(self, authorName, message):
		chat_message = f"{authorName} say {message} \n"
		result = self.chat.send_message(chat_message)
		return result.text

	def story(self):
		content = open("prompt/story.txt").read()
		result = self.chat.send_message(content)
		return result



class LocalModel:
	def __init__(self):
		path = os.getenv("MODEL_PATH") 
		self.llm = Llama(
		model_path= path,
		# n_gpu_layers=-1, # Uncomment to use GPU acceleration
		# seed=1337, # Uncomment to set a specific seed
		# n_ctx=2048, # Uncomment to increase the context window
		)
		# self.llm.set_cache(llama_cpp.LlamaCache)
		self.messages = [
			{"role": "system", "content": "You are a Dragon Master for a DND game."},
			{"role": "system", "content": open("prompt/starter.txt").read()}
		]
	# Generate the next scene for the group
	def generate_scenes(self, user:str, message: str):
		self.messages.append({"role": "user", "content": message})
		respond = self.llm.create_chat_completion(self.messages)["choices"][0]["message"]["content"]
		self.messages.append({"role": "system", "content": respond})
		print(self.messages)
		return respond
