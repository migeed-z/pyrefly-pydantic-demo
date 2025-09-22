# pyrefly-pydantic-demo
A demo of Pyrefly for Pydantic


### 1. Clone the repo

```bash
git clone https://github.com/migeed-z/pyrefly-pydantic-demo.git
```


### 2. Install the dependencies 

pip/venv

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

Conda

```bash
cd pyrefly-pydantic-demo
conda env create -f environment.yml
conda activate pyrefly-pydantic-demo
```

### 3. Run the examples 
```bash
cd examples
pyrefly check <example_file_name.py>
```

Install the IDE extension for hover and autocomplete: [https://pyrefly.org/en/docs/IDE/](https://pyrefly.org/en/docs/IDE/)

<img width="828" height="284" alt="Screenshot 2025-09-22 at 2 38 07 PM" src="https://github.com/user-attachments/assets/7792ebd0-4319-46c6-a38f-485624ec3935" />


### 4. Make sure you are using the right conda env in your IDE 
If you are using an IDE, make sure you set your conda environment to `pyrefly-pydantic-demo`. 
Instructions on how to do so in VSCode can be found [here](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment). 
