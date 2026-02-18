from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})


def index2(request, val1=0):
    try:
        # محاولة تحويل val1 إلى عدد صحيح
        val1 = int(val1)
        return HttpResponse(f"value1 = {val1}")
    except ValueError:
        return HttpResponse("Error: Expected an integer, but received a non-integer value.")

def viewbook(request, bookId):
    # تعريف الكتاب الأول
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble'}
    
    # تعريف الكتاب الثاني
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    # تحديد الكتاب بناءً على معرّف الكتاب
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2

    # تمرير الكتاب إلى القالب
    context = {'book': targetBook}
    
    # عرض تفاصيل الكتاب باستخدام القالب
    return render(request, 'bookmodule/show.html', context)