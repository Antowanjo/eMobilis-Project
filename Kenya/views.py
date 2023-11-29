from django.shortcuts import render


def about(request):
    return render(request, 'Kenya/about.html')

def category(request):
    return render(request, 'Kenya/category.html')

def contact(request):
    return render(request, 'Kenya/contact.html')


def internship_detail(request, internship_id):
    # You can implement logic here to fetch internship details based on the internship_id
    # For example: internship = Internship.objects.get(id=internship_id)
    return render(request, 'Kenya/internship-detail.html', {'internship_id': internship_id})

def internship_list(request):
    # You can implement logic here to fetch a list of internships
    # For example: internships = Internship.objects.all()
    return render(request, 'Kenya/internship-list.html', {'internships': []})

def testimonial(request):
    return render(request, 'Kenya/testimonial.html')

def home(request):
    return render(request, 'Kenya/index.html')


