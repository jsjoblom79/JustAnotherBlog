from django.shortcuts import render

posts = [
    {
        "author": "Jane Smith",
        "title": "Introduction to Python Programming",
        "content": "Python is a versatile programming language known for its simplicity and readability. This post explores the basics of Python syntax and its applications.",
        "date_posted": "2025-01-15"
    },
    {
        "author": "John Doe",
        "title": "Advanced Data Structures in Python",
        "content": "This article dives into complex data structures like trees and graphs, and how to implement them efficiently in Python.",
        "date_posted": "2025-02-10"
    },
    {
        "author": "Emily Johnson",
        "title": "Web Development with Django",
        "content": "Django is a high-level Python web framework. This post covers setting up a Django project and building a simple web application.",
        "date_posted": "2025-03-22"
    },
    {
        "author": "Michael Brown",
        "title": "Machine Learning with Python",
        "content": "Learn how to use Python libraries like scikit-learn and TensorFlow to build machine learning models for real-world problems.",
        "date_posted": "2025-04-18"
    },
    {
        "author": "Sarah Davis",
        "title": "Automating Tasks with Python Scripts",
        "content": "Automation can save time and reduce errors. This guide shows how to write Python scripts to automate repetitive tasks.",
        "date_posted": "2025-05-30"
    }
]
def home(request):
    context = {
        'posts': posts,

    }
    return render(request, 'blog/blog_index.html', context)

def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'blog/about_us.html', context)