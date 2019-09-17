## 練習課題A/ユーザ認証あり
  肉・魚・野菜（でる100per・でない0per）を登録できる
  「でる」が選ばれている中からどれか一つを返す

## 使い方

### ユーザーの作成
curl http://localhost:8000/signup/ -d "uuid=yourname"

### ユーザーの認証
curl http://localhost:8000/signin/ -d "uuid=yourname"

### 食材の追加
curl -X POST -H 'Content-Type:application/json' -d '{"name":"肉", "percent":100}' http://localhost:8000/randomMeal/config/ -H 'Authorization: JWT '

curl -X POST -H 'Content-Type:application/json' -d '{"name":"野菜", "percent":0}' http://localhost:8000/randomMeal/config/ -H 'Authorization: JWT '

### 選ばれている中からランダムに選出
curl http://localhost:8000/randomMeal/ -H 'Authorization: JWT '

### 食材一覧表示
curl http://localhost:8000/randomMeal/config/ -H 'Authorization: JWT '

### 食材の選択状態の変更
curl -X PUT -H 'Content-Type:application/json' -d '{"percent":0}' http://localhost:8000/randomMeal/config/1/ -H 'Authorization: JWT '

### 食材の削除
curl -X DELETE http://localhost:8000/randomMeal/config/3/ -H 'Authorization: JWT '

