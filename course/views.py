from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from course.models import coursePost, coursePage

def courseHome(request):
    #fetching post from database
    posts = coursePost.objects.all().order_by('-pk')
    data = {'posts':posts}

    return render(request, "course/postcourse.html", data)


def post(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        image = request.FILES["image"]
        date = request.POST.get('date', '')
        user = request.user
        print(user, title, description, image, date, end='\n')
        post_obj = coursePost(title=title, description=description, image=image, date=date, user=user)
        post_obj.save()
        messages.success(request, 'Showed')
        return redirect('/course')

    else:
        messages.error(request, 'wrong')
        return redirect('/course')

def userCourse(request, username):
    user = User.objects.filter(username=username)
    if user:
        course = Course.objects.get(user=user[0])
        bio = course.bio
        conductedcourse = course.conductedcourse
        enrolledcourse = course.enrolledcourse
        data = {'user_obj':user, 'bio':bio, 'conductedcourse':conductedcourse, 'enrolledcourse':enrolledcourse}


    return redirect(request, "course/postcourse.html", data)

def delCourse(request, courseId):

    course = coursePost.objects.filter(pk=courseId)
    image_path = course[0].image.url
    course.delete()
    messages.info(request, "Post Deleted")
    return redirect('/course')
