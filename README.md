# Send html mail using Python 🐍
***

&nbsp;

### Instalation
***

* [Python 3.10.2](https://www.python.org/downloads/release/python-3102/)
    * Install jinja2
      ```bash
          pip install jinja2  # I used 3.0.3
      ```
    * Install python-dotenv
      ```bash
          pip install python-dotenv  # I used 0.19.2
      ```
      
&nbsp;

### Preparation
***

* Download this repository
  * If you use GIT:
    ```git
        git clone https://github.com/Ja-Pan-Krzysztof/instaling.git
    ```
* Create `.env` file and enter that data :
    ```dotenv
        _USERNAME=<your gmail>
        _PASSWORD=<your password>
   ```
  
&nbsp;

### Use
***

* Run code
  * Windows :
    ```bash
        py main.py
    ```
  * Linux / MacOS
    ```bash
        python3 main.py
    ```
    
&nbsp;

* Parameters in `main.py`
  ```python
        mailer.send_mail(
            recipent_email='recipent@gmail.com',  # Enter recipent email
            subject='<Your subject>',  # Enter subject
            content=mess.render(),  #  Render `HTML` to the mail
            file='C:\\Users\\Ja\\Desktop\\prezentacja_brodacz_QUnit.odp'  # The file to be send | May be empty
        )
   ```
  
&nbsp;
  
* `HTML` file you can change in `templates/` and `message.py` :
  ```python
        TEMPLATE_FILE = './templates/wow.html'
   ```
  
&nbsp;

### Thanks for use this 🐍
