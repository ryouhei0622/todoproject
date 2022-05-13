from django.db import models

# Create your models here.

#選択肢（CHOICE）の宣言を行う
#tuple型で宣言する　('<プログラム上で使用される名前>','<実際に表示される名前>')
#基本的に選択肢はベタがきせずに他の場所に宣言する
CHOICE = (('danger', 'hight'),('warning','normal'),('primary','low'))

#クラスの宣言方法はおまじないとして考える　
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        #choicesを設定することによって選択肢を与えてそこから選ばせる事ができる
        #一般的にchoicesに与える選択肢の変数は大文字にする(ex. CHOICE)
        choices = CHOICE
    )
    #DataFieldは日付を受け取るメソッド, 詳しくは公式ドキュメントへGO
    duedate = models.DateField()

    def __str__(self):
        return self.title

