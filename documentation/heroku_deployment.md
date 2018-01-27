# Hosting telegram bot on Heroku 
**Deployment method:** Github <br>
**Language:** Python
<br><br>

### Obtain a token from botfather

### Create a repository on GitHub

### Clone the repository
```
$ git clone https://github.com/ruiwen905/kboxLyricsBot.git
```

### Write your code in python <br>
In the same directory as your cloned repository, create a python file named "main.py" (Can be any name)

### Create a Procfile
A file that describes how your application is going to run. <br>
To run a websever on Heroku, add this line to the file:
```
web: python main.py
```
It is similar to telling Heroku to run the command ```python main.py``` on the console <br>
*NOTE: Do **NOT** add any extension behind. The name of this file should exactly be "Procfile"

### Create a requirement text file
A file that contains a list of packages to install. <br>
You can do this by:
```
$ pip freeze > requirements.txt
```
You can add more packages to this file by directly editing it

### Deploy on Heroku
Sign up for Heroku <br>
Create an app on Heroku either by using the Heroku dashboard or by CLI
```
$ heroku apps:create <name of app>
```
From the dashboard, navigate to the "Deploy" tab <br>
Select GitHub as the deployment method <br>
Insert the URL to your GitHub repository <br>
Set Automatic Deploys <br>
Heroku will now deploy a new version of your app on every push to GitHub ```master```

### Config Vars
You may want to hide your bot token from the public <br>
Navigate to the "Settings" tab in the dashboard <br>
Insert it here <br>
<img src="images\config_vars.png"><br>
