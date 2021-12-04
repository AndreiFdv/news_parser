# News parser project

I'm too lazy to add something here.

## Installation

Clone this repository into your working directory with the following command.

```shell
$ git clone https://github.com/AndreiFdv/news_parser.git
```

In case you use **Pipenv**, type this command.

```shell
$ cd news_parser && pipenv install
```

For **virtualenv** use this.

```shell
$ virtualenv venv && source venv/bin/activate && cd news_parser && pip install -r requirements.txt
```

### Important

This project will not work without the **.env** file, so download it and put it into the project folder.

#### Finally

**Make sure that virtualenv was activated and use this command.**

```shell
$ python manage.py migrate && python manage.py runserver
```

### PyCharm Settings

Before you commit something, check the following settings inside the commit window:

1. Reformat code
2. Optimize imports
3. Perform code analytics

Understanding the code with **these settings enabled** will be much easier.
