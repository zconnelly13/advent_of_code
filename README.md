Advent Of Code Solutions
========================

Solutions to the problems found here http://adventofcode.com/

### Setup

Install virtualenv

```
pip install virtualenv
```

Create a new virtualenv, activate it, and install requirements

```
virtualenv venv
source venv/bin/activate
pip install -r setup/requirements.txt
```

### Running the Code

To "solve" a problem run

```
python problems/problem_*.py
```

Where * is the number of the problem

### Tests

To test that all of the problem.py files still work, run

```
nosetests
```
