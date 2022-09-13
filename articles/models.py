from zipapp import create_archive
from django.db import models

# create your models!

class Review:
    title = ''
    content = ''
    user = ''

    def __init__(self, content=content, title=title, user=user):
        #인스턴스에 바로 값을 집어넣을 수 있도록 __init__이용해서 self인자(기본)와, 필요한 데이터 인자를 넣어줌.
        #왼쪽이 키값, 오른쪽이 실제 값이 들어오는 변수명.
        self.content = content
        #self의 content = 위에서 들어온 content실제 값.
        self.title = title
        self.user = user

review1 = Review(title="저의 인생영화", content="인생은 아름다워", user="sun")
#review1은, Review클래스 안에, title, content, user가 입력되어 생성된 인스턴스. 
#키와 변수명을 위에서 정의해줬기 때문에 순서가 섞여도 되지만, 정의하지 않은 경우엔 꼭 순서대로 입력해주어야 한다. 가능한 이렇게 사용할것


class Article(models.Model):
    #models.Model 상속, id는 자동으로 만들어짐.
    title = models.CharField(max_length=10)
    #title은, models에서 가져온 글자수 10까지의 field
    content = models.TextField()
    #content는 많은 양의 글자를 받을 수 있는 field
    created_at = models.DateTimeField(auto_now_add=True)
    #created_at은 models의 DateTimeField(날짜 및 시간 필드)를 가져와서, uto_now_add=True(생성시 시각 자동 추가)되도록 하겠다.



