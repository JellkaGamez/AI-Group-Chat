from huggingface_hub import InferenceClient
import pygame, os

def warn(text):
    print("\033[33m[WARNING] " + text + "\033[0m")

def finput(text):
    return input("\033[34m[INPUT] " + text + "\033[0m")

def info(text):
    print("\033[32m[INFO] " + text + "\033[0m")

def err(text):
    print("\033[31m[ERROR] " + str(text) + "\033[0m")
    # raise Exception

try:
    with open("key.key", "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    err("key.key not found")
    exit()


if api_key == "YOUR API KEY HERE":
    err("API key not inputed. Please input your API key in the key.key file.")

client = InferenceClient(api_key=api_key)

pygame.init()

cont = finput('Continue existing chat? (y/n)')
if cont == "y":
    chat = finput("Please select a chat .chats/")
else:
    chat = finput("Please name your chat. ")

