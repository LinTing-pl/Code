import pymysql
from django.shortcuts import render, redirect
from sims import models


# Create your views here.
# 学生信息列表处理函数


def index(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students': students})


# def index(request):
#     conn = pymysql.connect(host="localhost", user="root", passwd="Linting201314", db="sms", charset='utf8')
#     with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
#         cursor.execute("SELECT id,student_no,student_name FROM sims_student")
#         students = cursor.fetchall()
#     return render(request, 'student/index.html', {'students': students})


# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'student/add.html')
    else:
        student_no = request.POST.get('student_no', '')
        student_name = request.POST.get('student_name', '')
        models.Student.objects.create(student_no=student_no, student_name=student_name)
        return redirect('../')


# def add(request):
#     if request.method == 'GET':
#         return render(request, 'student/add.html')
#     else:
#         student_no = request.POST.get('student_no', '')
#         student_name = request.POST.get('student_name', '')
#         conn = pymysql.connect(host="localhost", user="root", passwd="Linting201314", db="sms", charset='utf8')
#         with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
#             cursor.execute("INSERT INTO sims_student (student_no,student_name) "
#                            "values (%s,%s)", [student_no, student_name])
#             conn.commit()
#         return redirect('../')


def search(request):
    info = request.POST.get("info", "")
    if not info:
        return redirect('../')
    students = models.Student.objects.filter(student_no__contains=info) | models.Student.objects.filter(
        student_name__contains=info)
    return render(request, 'student/index.html', {'students': students})


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        student = models.Student.objects.get(id=id)  # 先查询
        return render(request, 'student/edit.html', {'student': student})
    else:
        id = request.POST.get("id")
        student_no = request.POST.get('student_no', '')
        student_name = request.POST.get('student_name', '')
        student = models.Student.objects.get(id=id)
        student.student_name = student_name
        student.student_no = student_no
        student.save()
        return redirect('../')


# def edit(request):
#     if request.method == 'GET':
#         id = request.GET.get("id")
#         conn = pymysql.connect(host="localhost", user="root", passwd="Linting201314", db="sms", charset='utf8')
#         with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
#             cursor.execute("SELECT id,student_no,student_name FROM sims_student where id =%s", [id])
#             student = cursor.fetchone()
#         return render(request, 'student/edit.html', {'student': student})
#     else:
#         id = request.POST.get("id")
#         student_no = request.POST.get('student_no', '')
#         student_name = request.POST.get('student_name', '')
#         conn = pymysql.connect(host="localhost", user="root", passwd="Linting201314", db="sms", charset='utf8')
#         with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
#             cursor.execute("UPDATE sims_student set student_no=%s,student_name=%s where id =%s",
#                            [student_no, student_name, id])
#             conn.commit()
#         return redirect('../')

# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    models.Student.objects.filter(id=id).delete()
    return redirect('../')
# def delete(request):
#     id = request.GET.get("id")
#     conn = pymysql.connect(host="localhost", user="root", passwd="Linting201314", db="sms", charset='utf8')
#     with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
#         cursor.execute("DELETE FROM sims_student WHERE id =%s", [id])
#         conn.commit()
#     return redirect('../')
