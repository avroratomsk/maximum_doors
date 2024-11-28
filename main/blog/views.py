from django.shortcuts import render

from blog.models import BlogSettings, Post, BlogCategory

def blog(request):
  posts = Post.objects.all()
  category = BlogCategory.objects.all()
  print(category)
  print(posts)

  try:
    setup = BlogSettings.objects.get()
  except:
    setup = BlogSettings()
  
  context = {
    "posts": posts,
    "categorys": category,
  }
  return render(request, "pages/blog/blog.html", context)

def category_post(request, category_slug):
  category = get_objects_or_404(BlogCategory, slug=category_slug)
  return render(request, "pages/blog/blog_category.html")

def post(request, category_slug, slug):
    category = BlogCategory.objects.all()
    post = Post.objects.filter(slug=slug, category=category)
    viewed_articles = request.session.get('viewed_articles', [])
    
    # Проверяем, просматривал ли пользователь эту статью ранее.
    if slug not in viewed_articles:
      # Увеличиваем счетчик просмотров, если статья просматривается впервые.
      article.view_count += 1
      article.save()

      # Добавляем идентификатор статьи в список просмотренных.
      viewed_articles.append(slug)

      # Обновляем сессию, сохраняя в ней обновленный список.
      request.session['viewed_articles'] = viewed_articles


    context = {
        "categorys": category,
        "post": post,
    }

    return render(request, "pages/blog/blog_detail.html", context)