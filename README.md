# pyquizAPI
QuizAPI.io wrapper for Python 3.8+

## Installation
You can install from the PyPI repository: [Package on PyPI](https://pypi.org/project/pyquizAPI/)

```powershell
pip install pyquizAPI
```

## How to Use
To get an API key go to [here](https://quizapi.io/) and create an account
```python
from pyquizAPI import QuizClient

# creates client object
client = QuizClient(api_key)

# get questions
questions = client.get_questions()

# returns list of question objects
# sample output
{'id': 197, 
'question': 'What is the prefix of WordPress tables by default?', 
'description': None, 
'answers': {
    'answer_a': 'wp_ default', 
    'answer_b': 'wp_', 
    'answer_c': 'wp_ in', 
    'answer_d': '_wp_', 
    'answer_e': None, 
    'answer_f': None
    }, 
'multiple_correct_answers': 'false', 
'correct_answers': {
    'answer_a_correct': 'false', 
    'answer_b_correct': 'true', 
    'answer_c_correct': 'false', 
    'answer_d_correct': 'false', 
    'answer_e_correct': 'false', 
    'answer_f_correct': 'false'
    }, 
'correct_answer': None, 
'explanation': None, 
'tip': None, 'tags': [{
    'name': 'WordPress'
    }], 
'category': 'CMS', 
'difficulty': 'Easy'}
```

### Arguments

| Argument | Type | Description |
| --- | --- | --- |
| category | string | Get the questions for a specific category only |
| difficulty | string | Get the questions for a specific difficulty only |
| tags | [string] | Specify a list of tags that you want the questions to belong to |
| limit | int | Limit the number of questions returned |

[Parameter Reference](https://quizapi.io/docs/1.0/parameters)

### Creating and using custom configuration

```python
client = QuizClient(api_key)

client.make_config(
    category='',
    difficulty='',
    tags=[''],
    limit=''
)

questions = client.get_questions(use_config=True)
```

