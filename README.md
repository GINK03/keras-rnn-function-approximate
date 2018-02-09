# RNNで関数近似
DeepLearningの一種であるRNNで、任意の関数を学習させて、十分にある関数の挙動が観測できたとき、未知の任意の点で予想できることを示したいと思います。  

## 始める前に諸々調査したこと
ディープラーニングで任意の連続する関数を再現可能です。  

しかし、ディープラーニングは無限やかなり大きな値を扱うことは難しく、適切にフィットしない問題があります。無限大に発散しない（発散してもいいけど、目的とする値をなにか閉域に限定して変換する操作を行う）必要があります    

もっと有機的で人間的な特徴を学習と予想を行う問題として、[sketch-rnn](https://magenta.tensorflow.org/assets/sketch_rnn_demo/index.html)というrnnで最初の一部だけを描き、学習した内容で残りを予想するという問題設定もあって面白くユニークです

<p align="center">
  <img width="300px" src="https://user-images.githubusercontent.com/4949982/36018890-b4cb78f4-0dc0-11e8-9720-1f0cf7e00958.png">
</p>
<div align="center"> 図1. 関数近似もスケッチの特徴を学び学習するのも一緒な気がします </div>

耳だけ描くと、残りの部分が自動的に機械学習の予想結果により描かれます  

## 様々な関数をDeepLearingのRNNで近似する

RNNはn-1からn-mまでの情報を特徴量にnの系列でのデータを予想することができます。  
この時、連続であることが望ましく、無限小、無限大を取らないような、一定の再帰性があると収束しやすいです。(発散する関数は予想が大きくなるに近づくにつれ、難しくなります)

<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35493641-4c4df17e-04f8-11e8-9a2c-3cb79a1245e6.png">
</p>
<div align="center"> 図2. アステロイド（うまくいく） </div>

<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35493714-b94d6750-04f8-11e8-90f7-bbc5cf321afd.png">
</p>
<div align="center"> 図3. 二次関数（うまくいかない）</div>

## 数式で表現する
ディープラーニングのRNNのEncoder-Decoderの一つの機能の粒度を関数として表現すると、このように表現することができると思います。  

<p align="center">
  <img width="450px" src="https://user-images.githubusercontent.com/4949982/35493888-eedf8082-04f9-11e8-8d61-c02ea2047458.png">
</p>

ディープラーニングで適切なF1, F2, F3を決定することで、次の系列のX,Yが予想可能になります  

## ネットワークで表現する
ディープラーニングのネットワークではこのように表せるように思います
<p align="center">
  <img width="650px" src="https://user-images.githubusercontent.com/4949982/35494326-35866728-04fd-11e8-9cdc-400c5e11d63b.png">
</p>
<div align="center"> 図4. 作成したネットワーク(RNNのAutoEncoderモデルを参考に作成)</div>

このネットワークは特に媒介変数がないと表現できないようなネットワークについて高い力を発揮しそうだと考えました。

## 実験

## サイクロイド
サイクロイドはこのような図形になます
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35494551-a23e20a8-04fe-11e8-915d-77395a8f2f9f.png">
</p>
<div align="center"> 図5. サイクロイド</div>
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
<div align="center"> 図6. 予想したサイクロイド</div>

## アステロイド
アステロイドはこのように表現され、一定の大きさよりは大きくなりません
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35493641-4c4df17e-04f8-11e8-9a2c-3cb79a1245e6.png">
</p>
<div align="center"> 図7. アステロイド </div>
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
<div align="center"> 図8. 予想したアステロイド(たまにyが0にドロップする)</div>

## 対数らせん
対数らせんはこのように表現されます。無限に大きくなるので、媒介変数thetaを一定の大きさでストップします
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35495016-f27ef12a-0501-11e8-885c-7b89344ceb5e.png">
</p>
<div align="center"> 図9. 対数らせん</div>

媒介変数を用いた表現はこのようになります
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/35495436-409791da-0504-11e8-926d-51bd03791d90.png">
</p>

**対数らせんの図** 

<p align="center">
  <img width="350px" src="https://user-images.githubusercontent.com/4949982/35495762-cbd8ee78-0505-11e8-859e-54b1dc345c08.png">
</p>
<div align="center"> 図10. 予想すした対数らせん（微妙に歪んでいる）</div>

## コード説明
**10-prepare.py**  
上記の例で示した図を描くような数字の系列のデータセットを出力します  
以下のファイルが生成されます  
```console
サイクロイド.pkl
アステロイド.pkl
カージオイド.pkl
対数らせん.pkl
リサージュ.pkl
インボリュート.pkl
```
**20-train-asteroid.py**  
アステロイドを学習&予想します  
**20-train-kardio.py**  
カージオイドを学習&予想します  
**20-train-cicloid.py**  
サークロイドを学習&予想します  
**20-train-spiral.py**  
対数らせんを学習&予想します  

## まとめ
- いろいろな媒介変数でないと表現が難しい関数をy = f(x)でない、系列予想の問題設定とすることで簡単に予想することができそうだとわかりました
- とにかく時系列でもなんでも連続した数字として表現できるのであれば、（モデルが十分に大きければ）予想が可能そうです
- 仮定や解析プロセスを挟まずに学習＆予想することができるので、楽です  

## 参考文献
- [1] [magenta.org](https://magenta.tensorflow.org/assets/sketch_rnn_demo/index.html)
- [2] [Universal Function Approximation using TensorFlow](http://deliprao.com/archives/100)
