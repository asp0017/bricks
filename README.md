# bricks

# :link: Install Instruction #

1. Install [Git](https://git-scm.com/)

    - https://backlog.com/git-tutorial/tw/

    - https://miahsuwork.medium.com/%E7%AC%AC%E4%BA%8C%E9%80%B1-git-%E6%9C%AC%E5%9C%B0%E7%AB%AF%E8%88%87%E9%81%A0%E7%AB%AF%E6%93%8D%E4%BD%9C-github-78eec4537179

2. Download [Tomcat](https://tomcat.apache.org/)

3.開啟cmd(命令提示字元)輸入以下指令碼

`cd (your folder path)`

`git init`

`git remote add 本地端名稱 https://github.com/WAFFLE900/bricks.git`

*`origin` 通常被預設成本地端名稱，可以改成自己喜歡的名稱

GitHub共用教學網站：

[GitHub共用教學網站](https://saffranblog.coderbridge.io/2020/12/01/github-collaboration/)

[GitHub共用教學網站1](https://medium.com/tsungs-blog/day13-git-github%E6%93%8D%E4%BD%9C-304ad94a1c6a)

[GitHub共用教學網站2](https://www.freecodecamp.org/chinese/news/git-rename-branch-how-to-change-a-local-branch-name/)

[上傳下載整合教學](https://gitbook.tw/chapters/github/fail-to-push)

[上傳下載整合教學2](https://www.796t.com/content/1549601292.html)

[GitHub上傳指令1](https://w3c.hexschool.com/git/b9be5b1e)

[GitHub上傳指令2](https://ithelp.ithome.com.tw/articles/10266697)

[GitHub本地端帳號登入](https://blog.csdn.net/weixin_43215322/article/details/109405983)

# :file_folder: Upload Files #

open your cmd(命令提示字元)

`cd (your folder path)`

`git add .` *加入所在資料夾內所有檔案
或 `git add 檔案名稱` *加入該檔案或資料夾

`git commit -m 版本名稱` *建立新版本

`git pull --rebase 本地端名稱 master` *將檔案及資料夾從遠端拉下來本地端整合

`git push -u origin master` *將整合好的檔案及資料夾上傳到遠端

# :file_folder: Download Files #

In your computer's folder, use the command below :

`cd (your folder path)`

`git pull 本地端名稱 master`

then you can refresh the data weekly to download file from GitHub.

### If it has a conflict during the download HW

You can try

`cd (your folder path)`

`git add .`

`git commit -m "write some message"`

`git merge master`

then pull again.

# 🌐 後端網站 #

https://docs.netlify.com/configure-builds/file-based-configuration/

*Pythonanywhere*

網址:

https://www.pythonanywhere.com/

教學:

https://ithelp.ithome.com.tw/articles/10308084?sc=rss.qu


# 📓 Django學習資源 #

Template語法：

https://ithelp.ithome.com.tw/articles/10212469

# 🤥 雜七雜八 #
網址：

https://app.netlify.com/sites/profound-strudel-3890fa/overview

教學：

[用 Netlify 佈署前端網頁 (一)](https://ithelp.ithome.com.tw/articles/10256925)

[用 Netlify 佈署前端網頁 (二)](https://ithelp.ithome.com.tw/articles/10257115)

[用 Netlify Functions 佈署 Line Bot](https://ithelp.ithome.com.tw/articles/10257235)

[探索 Netlify Functions 的暫存空間](https://ithelp.ithome.com.tw/articles/10257364?sc=rss.qu)

[用 Netlify 整合前後端服務](https://ithelp.ithome.com.tw/articles/10257884?sc=pt)

npm安裝使用教學:

https://ithelp.ithome.com.tw/articles/10234060

nodejs安裝:
https://nodejs.org/en/download/

netlify cli安裝雜七雜八:

https://www.youtube.com/watch?v=n_KASTN0gUE

https://blog.csdn.net/DMLong_x/article/details/111191599

dijango vs. netlify

https://www.netlify.com/blog/2016/04/08/a-step-by-step-guide-cactus-on-netlify/#netlifystart

https://www.reddit.com/r/django/comments/colbdd/is_it_possible_to_host_a_django_app_in_netlify/

https://answers.netlify.com/t/support-guide-can-i-run-a-web-server-http-listener-and-or-database-at-netlify/3078

超簡易教學:

https://bojne.medium.com/%E4%B8%89%E6%AD%A5%E9%A9%9F%E7%94%A8-netlify-%E8%BC%95%E9%AC%86%E6%9E%B6%E7%B6%B2%E7%AB%99-67d65ce135f6

netlify簡介

https://blog.alantsai.net/posts/2018/07/migrate-blog-to-ssg-demo-devops-8-netlify-free-static-site-hosting-service

前端佈署

https://www.youtube.com/watch?v=oiV7jz_56cA

其他資源+雜七雜八

https://jimmyswebnote.com/static-web-pages-vs-dynamic-web-pages/

https://techmoon.xyz/000webhost/


