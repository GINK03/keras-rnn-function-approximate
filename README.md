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

