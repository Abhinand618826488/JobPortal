from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class JobView(View):
    def get(self, request):
        jobs = [
            {
                "id": 101,
                "job_title": "Python Developer",
                "company": "ABC Technologies",
                "location": "Kochi",
                "job_type": "Full Time",
                "salary": 25000,
                "experience": "Fresher",
                "description": "Looking for a Python developer",
                "is_active": True
            },
            {
                "id": 102,
                "job_title": "Web Developer",
                "company": "XYZ Solutions",
                "location": "Kochi",
                "job_type": "Internship",
                "salary": 10000,
                "experience": "Fresher",
                "description": "Looking for a web developer",
                "is_active": True
            }
        ]
        return JsonResponse(jobs, safe=False)

class CompanyView(View):
    def get(self, request):
        companies = [
            {
                "id": 201,
                "company_name": "ABC Technologies",
                "location": "Kochi",
                "email": "abc@gmail.com",
                "website": "www.abc.com",
                "description": "Software development company"
            },
            {
                "id": 202,
                "company_name": "XYZ Solutions",
                "location": "Trivandrum",
                "email": "xyz@gmail.com",
                "website": "www.xyz.com",
                "description": "IT and consulting company"
            },
            {
                "id": 203,
                "company_name": "TechWorld",
                "location": "Bangalore",
                "email": "tech@gmail.com",
                "website": "www.techworld.com",
                "description": "Technology and web development company"
            }
        ]
        return JsonResponse(companies, safe=False)
