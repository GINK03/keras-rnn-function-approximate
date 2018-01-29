# RNNなどで関数を近似します

## Function Approximateの方法はいくつかあって、RNNで表現できるケース

RNNはn-1からn-mまでの情報を特徴量にnの系列でのデータを予想することができます。  
この時、単調増加のような形態を伴っていないことが望ましく、一定の再帰性があると収束しやすいです。(発散する関数は予想が発散領域に近づくにつれ、難しくなります)

<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35493641-4c4df17e-04f8-11e8-9a2c-3cb79a1245e6.png">
</p>
<div align="center"> 図1. アステロイド（うまくいく） </div>

<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35493714-b94d6750-04f8-11e8-90f7-bbc5cf321afd.png">
</p>
<div align="center"> 図2. 二次関数（うまくいかない）</div>

## 数式で表現する
最近解析学の本を読んでいて、圏論より実用性が高く、とても役に立つと思いました  

ディープラーニングのRNNで定式化すると、系列情報としてみなすことができるので、このようなことができます。 
<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/35493888-eedf8082-04f9-11e8-8d61-c02ea2047458.png">
</p>

ディープラーニングで適切なFを決定することで、次の系列のX,Yが予想可能になります  

## ネットワークで表現する
ディープラーニングのネットワークではこのように表せるように思います
<p align="center">
  <img width="650px" src="https://user-images.githubusercontent.com/4949982/35494326-35866728-04fd-11e8-9cdc-400c5e11d63b.png">
</p>
<div align="center"> 図3. 作成したネットワーク(RNNのAutoEncoderモデルを参考に作成)</div>

このネットワークは特に媒介変数がないと表現できないようなネットワークについて高い力を発揮しそうだと考えました。

## 実験

## サイクロイド
サイクロイドはこのような図形になます
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35494551-a23e20a8-04fe-11e8-915d-77395a8f2f9f.png">
</p>
<div align="center"> 図4. サイクロイド</div>
媒介変数をもちいた表現はこのようになります
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35494665-75d8936c-04ff-11e8-85b0-55b396437d52.png">
</p>

**学習**

```console
$ python3 20-train-cicloid.py --train
```
**評価** 

trainで使用しなかったデータを使用して予想
```console
$ python3 20-train-cicloid.py --predict
```
<p align="center">
  <img width="350px" src="https://user-images.githubusercontent.com/4949982/35494768-36a95716-0500-11e8-9da5-58bb5a1dee6f.png">
</p>
<div align="center"> 図5. 予想したサイクロイド</div>

## アステロイド
アステロイドはこのように表現され、一定の大きさよりは大きくなりません
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35493641-4c4df17e-04f8-11e8-9a2c-3cb79a1245e6.png">
</p>
<div align="center"> 図6. アステロイド </div>
媒介変数をもちいた表現はこのようになります
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35494859-dc3faa68-0500-11e8-8df9-1d8d6b8c7565.png">
</p>

**学習**

```console
$ python3 20-train-asteroid.py --train
```

**評価** 

trainで使用しなかったデータを使用して予想します

```console
$ python3 20-train-asteroid.py --predict
```
<p align="center">
  <img width="350px" src="https://user-images.githubusercontent.com/4949982/35494923-589bdeba-0501-11e8-8bd4-2e0cb56cacbf.png">
</p>
<div align="center"> 図7. 予想したアステロイド(たまにドロップする)</div>

## 対数らせん
対数らせんはこのように表現されます。無限に大きくなるので、媒介変数thetaを一定の大きさでストップします
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35495016-f27ef12a-0501-11e8-885c-7b89344ceb5e.png">
</p>
<div align="center"> 図8. 対数らせん</div>

媒介変数を用いた表現はこのようになります
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35495436-409791da-0504-11e8-926d-51bd03791d90.png">
</p>

**対数らせんの図** 

<p align="center">
  <img width="350px" src="https://user-images.githubusercontent.com/4949982/35495762-cbd8ee78-0505-11e8-859e-54b1dc345c08.png">
</p>
<div align="center"> 図9. 予想すした対数らせん（微妙に歪んでいる）</div>

## まとめ
- いろいろな媒介変数でないと表現が難しい関数をy = f(x)でない、系列予想の問題設定とすることで予想することができそうだとわかりました
- とにかく時系列でもなんでも連続した事象でパラメタライズできるのであれば、予想が可能そうです
- 応用範囲は関数近似が既存のタスクでむずかしかった領域全体に広がり、有益そうです
