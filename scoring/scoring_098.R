#モデルとスコアリング関数を読み込み
load("./scoring_model.Rdata")

#wavファイル読み込み時のwarningを表示させない
options(warn=-1)

#必要パッケージの準備
if(!require("seewave")){install.packages("seewave")}
if(!require("tuneR")){install.packages("tuneR")}
library(seewave)
library(tuneR)

scoring.performance(commandArgs(trailingOnly=TRUE)[2], commandArgs(trailingOnly=TRUE)[1])

