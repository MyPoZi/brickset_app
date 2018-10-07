# brickset_app

### Django 2.1.1 使用

### 追加した機能
- ページング機能
- アカウント登録機能
- ログイン、ログアウト機能
- 一般ユーザーの場合、編集や削除を行わせないための処理

様々なバグ(仕様)が発生したが、修正することができた。URLを直接入力することによりアクセスできてしまう仕様も修正済み。ログインの有無や、管理者がログインしている場合など、条件分岐が難しかった。

`$ git clone https://github.com/MyPoZi/brickset_app`  
`$ cd brickset_app/brickset_app`  
`$ python3 manage.py runserver`  
then access to http://127.0.0.1:8000/

#### The user information  
##### admin  
id: MyPoZi  
pass: mypozi  

##### generalUser  
id: generaluser  
pass: test0987  