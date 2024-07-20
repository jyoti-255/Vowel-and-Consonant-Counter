from django.shortcuts import render

def home(request):
    if request.POST.get("txt"):
        txt = request.POST.get("txt")
        vc, cc = 0, 0
        for t in txt:
            if t.isalpha():
                if t in "AEIOUaeiou":
                    vc += 1
                else:
                    cc += 1
        msg = "Vowels: " + str(vc) + ", Consonants: " + str(cc)
        return render(request, "home.html", {"msg": msg, "txt": txt})
    else:
        return render(request, "home.html")
