from django.shortcuts import render
from django.views import generic
from .forms import PostForm, CommentForm
from .models import Post
from django.shortcuts import render, get_object_or_404




# Create your views here.
class CommentList(generic.ListView):
    #queryset = Post.objects.filter(status=1).order_by('-update_date') #status publised to be shown
    template_name = 'comment_list.html'


	def post_detail(request, slug):
		template_name = 'post_detail.html'
		post = get_object_or_404(Post, slug=slug)
		comments = post.comments.filter(active=True)
		new_comment = None
		# Comment posted
		if request.method == 'POST':
			comment_form = CommentForm(data=request.POST)
			if comment_form.is_valid():

				# Create Comment object but don't save to database yet
				new_comment = comment_form.save(commit=False)
				# Assign the current post to the comment
				new_comment.post = post
				# Save the comment to the database
				new_comment.save()
		else:
			comment_form = CommentForm()

		return render(request, template_name, {'post': post,
											'comments': comments,
											'new_comment': new_comment,
											'comment_form': comment_form})


def post_detail(request, slug):
		template_name = 'post_detail.html'
		post = get_object_or_404(Post, slug=slug)
		comments = post.comments.filter(active=True)
		new_comment = None
		# Comment posted
		if request.method == 'POST':
			comment_form = CommentForm(data=request.POST)
			if comment_form.is_valid():

				# Create Comment object but don't save to database yet
				new_comment = comment_form.save(commit=False)
				# Assign the current post to the comment
				new_comment.post = post
				# Save the comment to the database
				new_comment.save()
		else:
			comment_form = CommentForm()

		return render(request, template_name, {'post': post,
											'comments': comments,
											'new_comment': new_comment,
											'comment_form': comment_form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment/comment_write.html', {'form': form})