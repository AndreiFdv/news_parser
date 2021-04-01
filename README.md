# Software engineering project

I'm too lazy to add something here

## Installation

Clone this repository into your working directory with following command.

```shell
$ git clone https://github.com/AndreiFdv/SE_Project.git
```

In case you use **Pipenv** type this command.

```shell
$ cd SE_Project && pipenv install
```

For **virtualenv** use this.

```shell
$ virtualenv venv && source venv/bin/activate && cd SE_Project && pip install -r requirements.txt
```

### Important

This project will not work without **.env** file, so download this file and put it into project folder.

#### Finally

**Make sure that virtualenv was activated and use this command.**

```shell
$ python manage.py migrate && python manage.py runserver
```

If everything is working then that's great, if not then not great. In any case **Good Luck**

### PyCharm Settings

Before you commit something, check following settings inside commit window:

1. Reformat code
2. Optimize imports
3. Perform code analytics

It will be much easier to understand the code with **these settings enabled**.