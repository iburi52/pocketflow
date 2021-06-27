# 「PocketFlow」
# ポートフォリオサイト概要
TensorFlowで画像認識「いぬ/ねこ判別機」  

テストユーザ：  
* emaill:pocketflow.test.user@gmail.com  
* password:Password1  

![pocketflow (1)](https://user-images.githubusercontent.com/59566529/99944959-1cc6fc80-2db7-11eb-873f-171367071c1d.png)

## 使用した技術一覧
* フロントエンド：angular(Mat Card, Flex-Layout)
* バックエンド  ：django(REST API)
* インフラ     ：AWS(EKS), docer(docker-compose), kubernetes(minikube, helm)

## 機能一覧
* ユーザ認証機能
* 画像ファイルのアップロード機能
* 機械学習Kerasモデル(.h5)実行機能
* 判定結果一覧表示機能

### minikube を使用してアプリケーション実行
minikube起動:
```bash
$ minikube start
$ minikube addons enable ingress
$ minikube dashboard
```
hostファイルの編集(Macの場合):
```bash
$ minikube ip
$ sudo nano /etc/hosts
  <MINIKUBE_IP> pocketflow
$ sudo killall -HUP mDNSResponder
```
すべてのhelmチャートをクラスターにインストール:
```bash
$ cd helmfile
$ helmfile sync
```
データベース作成:
```bash
$ kubectl get pods
$ kubectl exec -it <pocketflow-backend-PODS_NAME> bash 
  python manage.py makemigrations && python manage.py migrate
```
localサイトにアクセス:[http://pocketflow/](http://pocketflow/)  
  
リソース削除:
```bash
$ helmfile delete
$ minikube delete
```
