# Test Repo for LLMS and stuff

The following repo has some test python scripts for llama and also whisper 

Whisper is used to interpret speach and llama is used as the LLM to talk back to the user

The prompt files are used to constantly prompt user for text to feed to llama

The whisper file records using pyaudio and then prints the text out that was transcribed by whisper 

## Setup

### Environment

Fist follow the steps to setup python env from this

https://github.com/abetlen/llama-cpp-python

Specifically that readme will link to this

https://llama-cpp-python.readthedocs.io/en/latest/install/macos/

Which will have you install and set up conda and activate a python env with 

```
conda create -n llama python=3.9.16
```

and then

```
conda activate llama
```

Now you can pip install according to the linked page then after run

```
pip install -r requirements.txt
```

to install the other dependencies


### LLAMA

Download a gguf file and place in `~/.cash/models/`

Read install instructions for llamma_cpp here https://github.com/abetlen/llama-cpp-python

### Whisper

Here to install

https://github.com/openai/whisper

**Note** Follow all install instructions including part about installing `ffmpeg`

### Pyaudio

In order to get audio we use pyaudio which records and saves to a wave file

Need this for pyaudio

```
brew install portaudio
```


