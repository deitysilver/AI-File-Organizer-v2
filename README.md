To use this project, first clone the repository.

# Install Ollama

Then create an environment (google how to create python environment for your operating system (Linux, Mac, Windows etc) if you don't know how) and then run the following command:

pip install ollama

After that, go to this website and download ollama for the respective OS you're on:

https://ollama.com/download/windows

Once you've downloaded ollama, go to the terminal and install the AI model you wish to use, in this case, we're using "qwen2:1.5b".

ollama run qwen2:1.5b

Exit the model using `ctrl+d` once you've tested it out a little.

# Get Gemini API key

Create/Retrieve your API key from: https://makersuite.google.com/app/apikey

Then replace the "YOUR_API_KEY" string with your actual API key.

You can now just simply run the python file with the following command:

python main.py

Just sit back and watch the magic unfold.

Now just move your main.py script to whatever messy folder you have and move on with your day.

If you find your results to be less than mediocre, you can go through other models and select the one that best fits your VRAM. Then change the model name in the code, and voila.
