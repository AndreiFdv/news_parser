# Software engineering project

I'm too lazy to add something here

## Installation

Clone this repository into your working directory with following command. 

```shell
$ git clone https://github.com/AndreiFdv/SE_Project.git
```

If you are using **Pipenv** use this command.

```shell
$ cd SE_Project && pipenv install
```

For **virtualenv** use this.

```shell
$ virtualenv venv $$ source venv/bin/activate && cd SE_Project %% pip install -r requirements.txt
```

### Important 

This project will not work without **.env** file, so download this file and put it into project folder.

#### Finally 

**Make sure that virtualenv was activated and use this command.**

```shell
$ python manage.py runserver
```

If everything is working then that's great, if not then not great. In any case **GLHF**