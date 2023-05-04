# Custom chatgpt chat bot for organisational use
ChatGPT chatbots with customised knowledge is the need of the hour. I have created this repo python code base to train the chatgpt with custom data so that the user can train the chatgpt with the dataset which is in the data folder

How to use
==========

Step 1 - Initially spin up an aws ec2 instance , preferably a ubuntu machine

Step 2 - Run the following commands:

        1  sudo apt update
        2  sudo apt install build-essential libssl-dev libffi-dev zlib1g-dev
        3  wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tgz
        4  tar xzf Python-3.9.4.tgz
        5  cd Python-3.9.4
        6  ./configure --enable-optimizations
        7  make -j $(nproc)
        8  sudo make altinstall
        9  python3.9 --version

Step 3 - Then create virtual environment:

     python3 -m venv my_env

     Then :

     source my_env/bin/activate

Step 4 - Then do the following installations:

     pip install langchain==0.0.118

     pip install gpt_index==0.4.24



Step 5 - edit api key and  put your own api key there. Register an account at openai.com if you don't have one.

Step 6 - Create a data folder in the current working directory

Step 7 - Place the file that you intent to train the chatgpt in the data folder

Step 8 - From the command line use 'python chatbot.py' to run the training and the bot and ask with end up in USER: prompt and the user can ask question based on the trained data.

Step 9 (optional) - If you want to enable PDF support, install PyPDF2. 
