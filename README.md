# 環境

python: 3.6^  
django: 2.2.5  
djangorestframework: 3.10.3  
djangorestframework-jwt: 1.11.0

# 準備

pipenv install

pipenv run python manage.py migrate

# 実行

pipenv run python manage.py runserver

## 使い方

### ユーザーの作成 or ログイン

curl http://localhost:8000/signin/ -d "uuid=uuid"

### 食材の追加

curl -X POST -H 'Content-Type:application/json' -d '{"name":"豚肉", "food_type": "meat", "rate":100}' http://localhost:8000/randomFood/config/ -H 'Authorization: JWT '

curl -X POST -H 'Content-Type:application/json' -d '{"name":"白菜", "food_type": "vegetable", "rate":0}' http://localhost:8000/randomFood/config/ -H 'Authorization: JWT '

### 食材の一括追加

curl -X POST -H 'Content-Type:application/json' -d '[{"name":"鶏肉", "food_type": "meat", "rate":100}, {"name":"牛肉", "food_type": "meat", "rate":100}]' http://localhost:8000/randomFood/config/ -H 'Authorization: JWT '

### 選ばれている中からランダムに選出

curl http://localhost:8000/randomFood/ -H 'Authorization: JWT '

### 食材一覧表示

curl http://localhost:8000/randomFood/config/ -H 'Authorization: JWT '

### ユーザごとの食材一覧表示

curl http://localhost:8000/randomFood/user/config/ -H 'Authorization: JWT '

### 食材の選択状態の一括変更

curl -X PUT -H 'Content-Type:application/json' -d '{"data": [{"rate": 30, "name": "牛肉"}, {"rate": 30, "name": "イワシ"}]}' http://localhost:8000/randomFood/user/config/ -H 'Authorization: JWT '
