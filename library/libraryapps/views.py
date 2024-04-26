from django.shortcuts import render
from django.http import HttpResponse
from libraryapps.models import Books,Issuedbooks,LibraryMember,Availablebooks,DeletedBooks
from django.template import loader
from django.shortcuts import get_object_or_404
from datetime import datetime,timedelta
from django.utils import timezone
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')
def adduser(request):
    return render(request,'adduser.html')

def addmember(request):
    if request.method=='POST':
        uname=request.POST['username']
        mail=request.POST['email']
        member=LibraryMember(username=uname,email=mail)
        member.save()
        return HttpResponse("Member Added Succesfully")
    else:     
        return HttpResponse("Failed")

def back(request):
    return render(request,'home.html')

def addbooks(request):
    return render(request,'addbooks.html',{})

def availbooks(request):
    booklist=Availablebooks.objects.all().values()
    template=loader.get_template('viewbooks.html')
    context={
        'booklist':booklist,
    }
    return  HttpResponse(template.render(context,request))


def addbookitems(request):
    if request.method=='POST':
        bid=request.POST['bookid']
        bname=request.POST['bookname']
        authname=request.POST['authorname']
        bookdetails=Books(bookID=bid,bookname=bname,authorname=authname)
        bookdetails.save()
        available_book_details = Availablebooks(bookID=bid, bookname=bname, authorname=authname)
        available_book_details.save()
        return HttpResponse("Books Added Succesfully")
    else:     
        return HttpResponse("Failed")


def issuebooks(request):
    return render(request,'issuebooks.html')

def issuedetails(request):
    if request.method == 'POST':
        bid = request.POST['bookid']
        username = request.POST['username']
        email = request.POST['email']
        issuedate_str = request.POST['issuedate']
        issuedate = datetime.strptime(issuedate_str, '%Y-%m-%d').date()
        returndate = issuedate + timedelta(10)
        today_date = timezone.now().date()
        dailydate = today_date
        try:
            member = LibraryMember.objects.get(username=username, email=email)
            book = Books.objects.get(bookID=bid)

            # Create an entry in Issuedbooks model
            issuebook = Issuedbooks.objects.create(
                bookID=book,
                username=member,
                email=member,
                issuedate=issuedate,
                returndate=returndate,
                dailydate=dailydate
            )

            # Delete the book details from Availablebooks model
            available_book = Availablebooks.objects.get(bookID=bid)
            DeletedBooks.objects.create(
                bookID=available_book.bookID,
                bookname=available_book.bookname,
                authorname=available_book.authorname
            )
            available_book.delete()

            # Send return reminder email
            days_until_return = (returndate - dailydate).days
            if days_until_return <= 9:
                subject = 'Return Reminder for Book ID {}'.format(bid)
                message = 'Dear {}, please return the book with ID {} by {}.'.format(username, bid, returndate)
                send_mail(subject, message, 'kalaivanin2510@gmail.com', [email])

            return HttpResponse("Issued details saved")
        except LibraryMember.DoesNotExist:
            return HttpResponse("Library member does not exist")
        except Books.DoesNotExist:
            return HttpResponse("Book does not exist")
        except Availablebooks.DoesNotExist:
            return HttpResponse("Book is not available for issue")
        except Exception as e:
            return HttpResponse("An error occurred: {}".format(str(e)))
    else:
        return HttpResponse("Invalid request method")
    
def viewissuedbooks(request):
    issuedlist=Issuedbooks.objects.all().values('bookID__bookID', 'username__username', 'username__email', 'issuedate', 'returndate')
    template=loader.get_template('viewissuedbooks.html')
    context={
        'issuedlist':issuedlist,
    }
    return  HttpResponse(template.render(context,request))
        
def deletebooks(request):
    return render(request, 'deletebooks.html')

  
def deleteparticularbook(request):
    if request.method == 'POST':
        bid = request.POST.get('bookID')
        try:
            book = Availablebooks.objects.get(bookID=bid)
            Books.objects.filter(bookID=bid).delete()
            DeletedBooks.objects.create(bookID=book.bookID, bookname=book.bookname, authorname=book.authorname)
            book.delete()
            return HttpResponse("Successfully deleted")
        except Books.DoesNotExist:
            return HttpResponse("Invalid book ID")
           
def returnbookpage(request):
    return render(request,'returnbooks.html')

def returnbooks(request):
    if request.method == 'POST':
        bid = request.POST.get('bookID')
        try:
            book = DeletedBooks.objects.get(bookID=bid)
            if Issuedbooks.objects.filter(bookID=bid).exists():
                # Check if the book already exists in Availablebooks
                existing_book = Availablebooks.objects.filter(bookID=bid)
                if not existing_book:
                    # Create a new entry in Availablebooks model
                    Availablebooks.objects.create(
                        bookID=book.bookID, 
                        bookname=book.bookname, 
                        authorname=book.authorname
                    )

                # Delete the book from DeletedBooks model
                book.delete()

                # Delete the book from Issuedbooks model
                Issuedbooks.objects.filter(bookID=bid).delete()

                return HttpResponse("Book returned successfully")
            else:
                return HttpResponse("Book is not issued yet")
        except DeletedBooks.DoesNotExist:
            return HttpResponse("Invalid book ID")
    else:
        return HttpResponse("Invalid request method")


  
    

#  pjdzzpdsqwhywpma