~~~
开发一个网站
-前端开发：HTML、CSS、JavaScript
-Web框架：接受请求并处理
-MySQL数据库：存储数据地方
~~~

# 1.前端开发-标签

用户(浏览器)解析网站返回的字符串\
## 1.1 head标签`<head></head>`

内部配置

~~~html
<head>
    <meta charset="UTF-8">
    <title>Web_Test</title>
</head>
~~~

### 1.1.1 编码

~~~html
<meta charset="UTF-8">
~~~

### 1.1.2 title

~~~html
<title>Web_Test</title>
~~~

![image-20220804113118859](D:\Notes\code\web\log_img\image-20220804113118859.png)

## 1.2 body标签`<body></body>`

内容

~~~html
<body>
    ...
</body>
~~~

### 1.2.1 标题`<h1></h1>`

~~~html
<h1>一级标题</h1>
...
<h6>六级标题</h6>
~~~

### 1.2.2 `<div>`和`<span>`

~~~html
<div>
    内容
</div>

<span>内容</span>
~~~

* `<div>`块级标签，一个人占一整行。

* `<span>`内联(行内)标签，自己多大就占多少。

~~~html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Web_Test</title>
    </head>
    <body>
        <h1>Title1 Test</h1>
        <h2>Title2 Test</h2>
        <div>div test</div>
        <span>span</span>
        <span>test</span>
    </body>
</html>
~~~

![image-20220804115155656](D:\Notes\code\web\log_img\image-20220804115155656.png)

### 1.2.3 超链接`<a></a>`

* 跳转到其他的网站

~~~html
<a href="https://www.bilibili.com/">点击跳转</a>
~~~

* 跳转到自己网站的其他地址

~~~html
<a href="http://127.0.0.1:5000/show/info">点击跳转</a>
<a href="/show/info">点击跳转</a>
~~~

~~~html
# 当前页面打开
<a href="网址">点击跳转</a>

# 新标签页打开
<a href="网址" target="_blank">点击跳转</a>
~~~

### 1.2.4 图片`<img />`

~~~html
<img src="图片地址" />
~~~

* 直接显示别人的图片地址（可能有防盗链）

~~~html
<img src="图片地址" />
~~~

* 显示自己的图片：

~~~html
——自己项目中创建：static目录，图片要放在static中
<img src="/static/xxx.png" />
~~~

关于设置图片的高度和宽度：

~~~html
<img style="height:100px; width:100px;" src="图片地址" />
<img style="height:10%; width:10%;" src="图片地址" />
~~~

## 小结

* 学习的标签

~~~html
- 块级标签
    <h1></h1>
    <div></div>
- 行内标签
    <span></span>
    <a></a>
    <img />
~~~

* 嵌套

~~~html
<div>
    <span></span>
</div>
~~~

~~~html
<a href="网址" target="_blank">
	<img src="图片地址">
</a>
~~~

## 1.2.5 列表

~~~html
# 无序号
<ul>
    <li>xxx</li>
    <li>xxx</li>
    <li>xxx</li>
    <li>xxx</li>
</ul>
~~~

~~~html
# 有序号
<ol>
    <li>xxx</li>
    <li>xxx</li>
    <li>xxx</li>
    <li>xxx</li>
</ol>
~~~

![image-20220804145017158](D:\Notes\code\web\log_img\image-20220804145017158.png)

## 1.2.6 表格

~~~html
<table border="1">
    <thead>
        <tr>
            <th>ID</th>
            <th>name</th>
            <th>age</th> 
        </tr>
    </thead>
    
    <tbody>
        <tr>
            <td>1</td>
            <td>Tim</td>
            <td>22</td> 
        </tr>
        <tr>
            <td>2</td> 
            <td>Tim</td>
            <td>22</td>
        </tr>
        <tr>
            <td>3</td> 
            <td>Tim</td>
            <td>22</td>
        </tr>
        <tr>
            <td>4</td> 
            <td>Tim</td>
            <td>22</td>
        </tr>
    </tbody>
</table>
~~~

![image-20220804145653934](D:\Notes\code\web\log_img\image-20220804145653934.png)

## 1.2.7 input系列（7个）

~~~html
<input type="text" />
<input type="password" />
<input type="file" />
# 单选框
<input type="radio" name="n1">Yes
<input type="radio" name="n1">No
# 复选框
<input type="checkbox">篮球
<input type="checkbox">足球
<input type="checkbox">乒乓球
# 按钮
<input type="button" value="提交">  -- 普通按钮
<input type="submit" value="提交">  -- 提交表单
~~~

## 1.2.8 下拉框

~~~html
# 单选
<select>
    <option>北京</option>
    <option>上海</option>
    <option>深圳</option>
</select>
# 多选(按住shift)
<select multiple>
    <option>北京</option>
    <option>上海</option>
    <option>深圳</option>
</select>
~~~

## 1.2.10 多行文本

~~~html
<textarea rows="3"></textarea> # 默认3行
~~~

