<html lang="ko">
<head>
    <meta charset="UTF-8">

    <!-- Boot strap -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <style>
        .content{
            height: 75%;
        }
        .messageDiv{
            margin-top: 20px;
            margin-bottom: 50px;
        }
        .toDoDiv{

        }
        .custom-btn{
            font-size: 10px;
        }
        .panel-footer{
            height:10%;
            color:gray;
        }
    </style>

    <title>Twitter Image Search Engine</title>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="page-header">
                <h1>To-do List <small>KPOP IDOLS</small></h1>
            </div>
        </div>
        <div class="content">
            <div class="messageDiv">
                <form action="./search/" method="POST">{% csrf_token %}
                    <div class="input-group">
                        <input id="groupContent" name="groupContent" type="text" class="form-control" placeholder="Group">
                        <input id="nameContent" name="nameContent" type="text" class="form-control" placeholder="Name">
                        <input id="dateContent" name="dateContent" type="text" class="form-control" placeholder="Date(YYMMDD)">
                        <span class="input-group-btn">
                            <button class="btn btn-default" type="submit">검색</button>
                        </span>
                    </div>
                </form>
            </div>

            <div class="toDoDiv">
                <ul class="list-group">
                    {% for todo in todos %}
                    {% if todo.isDone == False %}
                    <form action="./doneTodo/" method="GET">
                        <div class="input-group" name='todo1'>
                            <li class="list-group-item">{{ todo.content }}</li>
                            <input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>
                            <span class="input-group-addon">
                                <button type="submit" class="custom-btn btn btn-danger">완료</button>
                            </span>
                        </div>
                    </form>
                    {% else %}
                    {% endif %}
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
</body>
</html>