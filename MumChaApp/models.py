from django.db import models

#アカウントテーブル

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/user/', null=True, blank=True)
    comment = models.TextField(max_length=200, null=True)

    #ユーザー名を表示する
    def __str__(self):
        return self.name

    #フォロー人数を表示するfollow関数を定義
    def follow_nums(self):
        return len(Follow.objects.filter(owner=self.user_id))
    
    #フォロワー人数を表示するfollower_nums関数を定義
    def follower_nums(self):
        return len(Follow.objects.filter(follow_target=self.user_id))

#投稿テーブル
class Post(models.Model):
    content = models.TextField(max_length=200, null=True)
    post_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to="images/post/", null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

#フォローテーブル
class Follow(models.Model):
    follow_id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'do_follow_user')
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'accept_follow_user')

#いいねテーブル
class Favorite(models.Model):
    fav_id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.ForeignKey(Post, on_delete=models.CASCADE)