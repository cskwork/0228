from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
#from django.views.generic.edit import FormMixin


# Create your views here.
def board(request):
	#return HttpResponse("hello")
	return render(request, 'board.html') 

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-update_date') #status publised to be shown
    template_name = 'post_list.html'



from comments.forms import CommentForm

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'
	form_class = CommentForm
	
	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		comment_form = CommentForm()
		context['comment_form'] = comment_form
		return context

		pk = self.kwargs.get('pk')
		slug = self.kwargs.get('slug')	
		#context = super(PostDetail, self).get_context_data(**kwargs)
		#context['form'] = CommentForm(initial={'post': self.object})
		return context

	def get_success_url(self):
		return reverse('post_detail', kwargs={'pk': self.object.id})
	
	def post(self, request, *args, **kwargs):
		new_comment = PostComment(content=request.POST.get('content'),
								writer=self.request.user,
								post_connected=self.get_object())
		new_comment.save()
		return self.get(self, request, *args, **kwargs)
	
	@property
	def number_of_comments(self):
		return PostComment.objects.filter(post_connected=self).count()
		# post = get_object_or_404(Post, id=pk, slug=slug)  
		# comments = post.comments.filter(active=True)
		# new_comment = None


		# if self.request.method == 'POST':
		# 	comment_form = CommentForm(data=request.POST)
		# 	if comment_form.is_valid():

		# 		# Create Comment object but don't save to database yet
		# 		new_comment = comment_form.save(commit=False)
		# 		# Assign the current post to the comment
		# 		new_comment.post = post
		# 		# Save the comment to the database
		# 		new_comment.save()
		# else:
		# 	comment_form = CommentForm()

		# context["post"] = post
		# context["comments"] = comments
		# context["new_comment"] = new_comment
		# context["comment_form"] = comment_form
		# return context

		# return render(request, template_name, {'post': post,
		# 									'comments': comments,
		# 									'new_comment': new_comment,
		# 									'comment_form': comment_form})


		# if stuff.likes.filter(id=self.request.user.id).exists():
		# 	liked = True
		# context["total_likes"] = total_likes
		# context["liked"] = liked
		# return context



	# def post_detail(request, slug):
	# 	print('INNNN')
	# 	template_name = 'post_detail.html'
	# 	post = get_object_or_404(Post, slug=slug)
	# 	comments = post.comments.filter(active=True)
	# 	new_comment = None
	# 	# Comment posted
	# 	if request.method == 'POST':
	# 		comment_form = CommentForm(data=request.POST)
	# 		if comment_form.is_valid():

	# 			# Create Comment object but don't save to database yet
	# 			new_comment = comment_form.save(commit=False)
	# 			# Assign the current post to the comment
	# 			new_comment.post = post
	# 			# Save the comment to the database
	# 			new_comment.save()
	# 	else:
	# 		comment_form = CommentForm()

	# 	return render(request, template_name, {'post': post,
	# 										'comments': comments,
	# 										'new_comment': new_comment,
	# 										'comment_form': comment_form})

#Edit a post
def edit(request, pk, template_name='Crud/edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete post
def delete(request, pk, template_name='Crud/confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})