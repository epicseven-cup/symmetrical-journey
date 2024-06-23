from llama_cpp import Llama

class model:
	def __init__(self):
		self.llm = Llama(
		model_path= os.getenv("MODEL_PATH"),
		# n_gpu_layers=-1, # Uncomment to use GPU acceleration
		# seed=1337, # Uncomment to set a specific seed
		# n_ctx=2048, # Uncomment to increase the context window
		)
		self.llm.set_cache(llama_cpp.LlamaCache)
		self.messages = [
			{"role": "system", "content": "You are an assistant who perfectly describes images."},
			{"role": "user", "content": "Describe this image in detail please."}
		]
	# Generate the next scene for the group
	def generate_scenes(user:str, message: str):
		self.messages.append({"role": user, "content": messages})
		return self.llm.create_chat_completion(self.messages)
