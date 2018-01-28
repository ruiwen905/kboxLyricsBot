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
A file in the root directory that describes the command to start your app. <br>
To run on Heroku, add this line to the file:
```
worker: python main.py
```
It is similar to telling Heroku to run the command ```python main.py``` on the console <br>
*NOTE: Do **NOT** add any extension behind. The name of this file should exactly be "Procfile" <br>
*NOTE: If you use ```web: python main.py```, you may encounter the error ```Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch```

### Create a requirement text file
A file that contains a list of dependencies to install. <br>
When your app is deployed, Heroku will read this file and installs these Python dependencies. <br>
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
<img src="images\deployment_github.png"><br>
Heroku will now deploy a new version of your app on every push to GitHub ```master```

### Config Vars
You may want to hide your bot token from the public <br>
Navigate to the "Settings" tab in the dashboard <br>
Insert it here <br>
<img src="images\config_vars.png"><br>
To access these variables:
```python
import os
botToken = os.environ['BOT_TOKEN']
```

### Dyno Settings
To turn on the dynos, navigate to the "Resources" tab in the dashboard <br>
<img src="images\dyno_setting.png"><br>
You can also turn it on using the CLI <br>
```
$ heroku ps:scale worker=1
```
 