# Log Manager
- [Log Manager](#log-manager)
  - [Brief Summary](#brief-summary)
  - [Sample Demonstration of Features](#sample-demonstration-of-features)
      - [Adding a new log](#adding-a-new-log)
      - [Adding a follow up on a log and sorting logs by date](#adding-a-follow-up-on-a-log-and-sorting-logs-by-date)
      - [Filtering or isolating all-time logs using any search combination](#filtering-or-isolating-all-time-logs-using-any-search-combination)
  - [Steps to Run](#steps-to-run)
  - [Comments and Observations](#comments-and-observations)
## Brief Summary
Log Manager is a web board that can be used by a start up company to manage and visualize "logs". A "log" is a time-stamped documentation of events related to work operations

## Sample Demonstration of Features
#### Adding a new log
![1_create_log](https://github.com/maksim-petrushin/Maintenance-Operations-Board/assets/136845116/c84d5cae-eed4-415f-acc1-1bc96233e0c3)

#### Adding a follow up on a log and sorting logs by date
![2_followup_sort](https://github.com/maksim-petrushin/Maintenance-Operations-Board/assets/136845116/0c4f4ee3-41bb-4250-9e4d-20979b148198)

#### Filtering or isolating all-time logs using any search combination
![3_filter_history_report](https://github.com/maksim-petrushin/Maintenance-Operations-Board/assets/136845116/cee719bd-5107-46a5-bff7-cc2fd2835d2f)

## Steps to Run
- ### Clone this repository into your local directory
- ### Configure the Database
    - #### Option 1: Use the default local SQLite database
      - In your settings.py file,
        put this code:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }   
        
        ```
        Instead of this code:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'YOUR_DATA_BASE_NAME_WITHIN_PGADMIN_SERVER',
                'USER': 'YOUR_PG_ADMIN_USERNAME',
                'PASSWORD': 'YOUR_PG_ADMIN_PASSWORD',
                'HOST':'AWS_RDS_ENDPOINT',
                'PORT': 'PORT_NAME_WITHIN_YOUR_LOCAL_HOST_(MOST_LIKELY_5432)'
            }
        }
        
        ```
    - #### Option 2: Set up your AWS Account and use RDS and Postgres Database
      - This is option that is set by default in my repository because this is actually what I did in my implementation. I have put my database on AWS RSD
      - Prior to that I have created an AWS account and used documentation below to set up RDS
      - [RDS Setup Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)
      - You will have to fill the following blocks in your settings.py file with your AWS account keys and your RDS keys. (Keep this private)
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'YOUR_DATA_BASE_NAME_WITHIN_PGADMIN_SERVER',
                'USER': 'YOUR_PG_ADMIN_USERNAME',
                'PASSWORD': 'YOUR_PG_ADMIN_PASSWORD',
                'HOST':'AWS_RDS_ENDPOINT',
                'PORT': 'PORT_NAME_WITHIN_YOUR_LOCAL_HOST_(MOST_LIKELY_5432)'
            }
        }
        ```
        ```python
        #aws user
        AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACESS_KEY'
        AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_AWS_ACCESS_KEY'
        AWS_STORAGE_BUCKET_NAME = 'YOUR_AWS_BUCKET_NAME'
        ```
- #### Open your terminal, go to this project repositoty and type:
  ```
  python3 manage.py runserver
  ```
  If nothing went wrong, the output of this command will be the local link of your website, go to that website and enjoy and test the funtionality 🔭
 ## Comments and Observations
- I initially created this django project under name "ticketing" application, but then I found the better term "Log" instead of a "Ticket" for this application. But all of the models, forms, and application name were left as "tickets" and only the HTML was adjusted to say "Logs" everywhere for user experience obviously. So, please note, the root Django app name is "ticketing", the model name for the logs is "Ticket" and the model name for follow-ups on logs is "FollowUp".
- For support, please feel free to contact me using my contacts in my github bio. There is probably no-one who understands my implementation better than me, so it will be easire for me to just take a look at your potential bugs.



