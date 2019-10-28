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

### ユーザーの作成
curl http://localhost:8000/signup/ -d "uuid=yourname"

### ユーザーの認証
curl http://localhost:8000/signin/ -d "uuid=yourname"

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

### 食材の選択状態の変更
curl -X PUT -H 'Content-Type:application/json' -d '{"foodname": "鶏肉", "new_rate": 30}' http://localhost:8001/randomFood/user/config/ -H 'Authorization: JWT '

### 食材の選択状態の一括変更
PATCHかPUT


### 食材の削除
curl -X DELETE http://localhost:8000/randomFood/config/9/ -H 'Authorization: JWT '


curl -X GET http://localhost:8000/randomFood/config/2/ -H 'Authorization: JWT '