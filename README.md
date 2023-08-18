Download the project from the github repository using the following command in the terminal:

```python
git clone https://github.com/VarshithaCVasireddy/medicine_uses_LLM
```

To run the project I am creating a virtual environment and installing the required packages in it, so that the project can run without any issues.

To create a virtual environment, run the following command in the terminal:

```python
pip install pipenv
```

To install the required packages, run the following command in the terminal:

```python
pipenv install -r requirement.txt
```

To run the project, run the following command in the terminal:

```python
uvicorn main:app --reload
```

The model used in this project is trained on medicine and it's uses, so when the medicine name is given the model gives the uses of it. The model is big and takes time to load.

Now open the browser and go to the following url displayed in the terminal then add /docs to the end of the url, this is where you can give the input for execution. Click the POST button and then click the Try it out button. Now you can give the input in the text box and click the Execute button to get the output.

Below is an example of how to give the input and get the output.
<img width="1392" alt="image" src="https://github.com/VarshithaCVasireddy/Sensitive_Information_Redactor/assets/96924488/e54ae8a4-44de-475b-aa07-5862fa121d08">


Output is displayed as below
<img width="1368" alt="image" src="https://github.com/VarshithaCVasireddy/Sensitive_Information_Redactor/assets/96924488/a6baecbb-749c-4942-a5c2-3a63e410d37b">

Few examples that can be given as input are
1. What is the use of metformin?
2. Why are steroids used?
3. Why is sedative used?