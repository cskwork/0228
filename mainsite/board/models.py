from django.db import models
from datetime import date
from django.contrib.auth.models import User #Blog author or commenter
from django.urls import reverse

STATUS = (
    (0,"임시저장"),
    (1,"글 게시")
)

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 255 , verbose_name="제목")
	slug = models.SlugField(max_length=200, unique=True, verbose_name="URL명칭")
	#Post has one write, writer has many posts
	writer = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts', verbose_name="글쓴이")
	content = models.TextField(max_length = 5000, verbose_name="내용")
	create_date = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
	update_date = models.DateTimeField(auto_now= True, verbose_name="수정일")
	status = models.IntegerField(choices=STATUS, default=0, verbose_name="게시상태")
	allow_comments = models.BooleanField('댓글 허용 여부', default=True)

	class Meta:
		ordering = ["-update_date"]

	# String for representing the Model object.
	def __str__(self):
		return self.title	
	"""
	Returns the url to access a particular blog-author instance.
	"""
	def get_absolute_url(self):
		return reverse('post_detail', args=[str(self.id)])

# class Comment(models.Model):
#     post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body, self.name)