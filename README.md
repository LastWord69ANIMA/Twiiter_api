# Twiiter_api
私が始めて個人的に書いたコードです。リポジトリの中では一番古いモノとなっています。

~~※2023/08/25 追記~~
~~actionが長らくエラーとなっていましたが、その原因として~~
~~・workflowで実行するyamlにて実行するファイル名が間違っていた~~
~~・実行するファイルのパスが（公開する以上）セキュリティとして*としていたため、当リポジトリでは意図通りに実行されていない~~
~~ことが判明しました。~~

# 2024/3/11 追記
上記エラーの原因として「twitterからxへの移行に伴う、apiの有料化やその後の無料化などの騒動」に起因するapiの仕様変更と存じています。
~~今後はxのapi仕様に従い、作り直そうと存じます。また、その際、.env等を上手く活用し、伏せ字･･･例えば、`CHANNEL_ACCESS_TOKEN = "****"`等をわざわざ載せることなくデプロイしたいと思っています。~~

また、当リポジトリは実際に動かしていた方ではないです（動かしていた方は非公開）。

# 2024/3/21 追記
https://programming-zero.net/how-to-start-twitter-api-basic-and-free/
https://programming-zero.net/twitter-api-process/
https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api

以上より、使用していた**Standard(旧無料プラン)の機能であった他ユーザーのツイート取得が、Free(現無料プラン)では不可**ということが判明しました。

※3番目のリンクにあるTweet caps - Pull が APIのGETリクエストに該当するかと思われます。

　1,2番目のリンクにて、Freeプランにてgetリクエストを行うと、403エラー（内容は有効なkeyとtokenを使用せよ）が出力される旨が記載されています。

 　･･･実際、ターミナルにて、ファイルを実行すると同様の記載がでました。

![スクリーンショット of terminal execute serch_tweets1.py](https://images.microcms-assets.io/assets/7ac15f6666c24a5f88467fd874441472/b22c21e0c00b42ac91114c6211cd6f62/x_api%E3%81%AE%E9%96%8B%E7%99%BA%E4%B8%AD%E6%AD%A2.png)

よって、エラーの原因は「apiの有料化にまつわる騒動」と断定、また、当計画は凍結します。
