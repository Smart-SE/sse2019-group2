#モデルとスコアリング関数を読み込み
load("./scoring_model.Rdata")

#wavファイル読み込み時のwarningを表示させない
options(warn=-1)

#必要パッケージの準備
if(!require("seewave")){install.packages("seewave")}
if(!require("tuneR")){install.packages("tuneR")}
library(seewave)
library(tuneR)

#暫定スコアリング関数
scoring.performance = function(filepath, beat = 100){
  target.data = readWave(filepath)
  target.spec_1 = spec.ar(target.data@left[1:(length(target.data)/2)], plot=F)
  target.model = c(scale(target.spec_1$spec[1:250]))
  
  max.index = 0
  max.cor = 0
  for(i in (1:9)[-8]){
    tmp.cor = cor(model[,i], target.model)
    if(tmp.cor > max.cor){
      max.cor = tmp.cor
      max.index = i
    }
  }
  
  if(max.cor>0.9){
    base.score.pre = ceiling(max.index / 3)
    if(base.score.pre == 1){base.score = 100}
    if(base.score.pre == 2){base.score = 60}
    if(base.score.pre == 3){base.score = 20}
    
    score = round(exp(-(1-max.cor)*30)*20+(base.score-20))
    
  }else{
    score = floor(100 * max.cor + 10)
  }
  return(score)
}


scoring.performance(commandArgs(trailingOnly=TRUE)[2], commandArgs(trailingOnly=TRUE)[1])

