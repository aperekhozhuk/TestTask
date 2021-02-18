# Running locally:

#### (*Requirements:* linux, git, python3 installed)

1) Clone repository:
```
git clone https://github.com/aperekhozhuk/TestTask && cd TestTask
```
2) Export project settings to ENV (also you can change some of them if you need):
```
source ./set_env.sh
```
3) Create virtual environment, install libs, migrate and create superuser:
```
source ./install.sh
```
4) Run:
```
source ./run.sh
```


# Endpoints:
1) Signup:
```
POST http://127.0.0.1:8000/api/signup/ username=User_example password=Password_axample
```
2) Obtain access and refresh tokens:
```
POST http://127.0.0.1:8000/api/token/ username=User_example password=Password_axample
```
3) Refresh access token:
```
POST http://127.0.0.1:8000/api/token/refresh/ refresh=${refresh_token}
```
4) Create new Post:
```
POST 127.0.0.1:8000/api/posts/ title="Post 1" text="Text 1" "Authorization: Bearer ${access_token}"
```
5) Get list of Posts:
```
GET 127.0.0.1:8000/api/posts/
```
6) Get Post by id:
```
GET 127.0.0.1:8000/api/posts/1/
```
7) Get User's profile by user_id:
```
GET 127.0.0.1:8000/api/users/1/
```
8) Put like for Post:
```
POST 127.0.0.1:8000/api/posts/1/like/ "Authorization: Bearer ${access_token}"
```
9) Remove like from Post:
```
DELETE 127.0.0.1:8000/api/posts/1/like/ "Authorization: Bearer ${access_token}"
```
10) Get analytics of likes count by dates (you can pass optional query parameters for filtering):
```
GET "127.0.0.1:8000/api/analytics/?date_from=2021-01-01&date_to=2022-01-01"
```
