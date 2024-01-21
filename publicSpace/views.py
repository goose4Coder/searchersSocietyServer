from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(
        request,
        "publicSpacePages/mainPage.html",
    )


def about_us(request):
    return render(request, "publicSpacePages/about.html")
