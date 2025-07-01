from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

#Доступ к hub с predtrained models
from huggingface_hub import login
login(token="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")

model_name = "mistralai/Mistral-Nemo-Instruct-2407"

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-Nemo-Instruct-2407")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-Nemo-Instruct-2407")

model.save_pretrained("C:/Users/max/Desktop/Sturdy/3_curs_2_sem/summer_work/models/Mistral-Nemo-Instruct-2407")

#Чтобы был локальный доступ к базовой модели, а не каждый раз скачивали с hugging_face
#Поменяв значение model_name, можем скачать любую другую доступную модель