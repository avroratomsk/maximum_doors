def admin_service_page(request):
  try:
    service_page = ServicePage.objects.get()
  except:
    service_page = ServicePage()
    service_page.save()

  if request.method == "POST":
    form_new = ServicePage(request.POST, request.FILES, instance=service_page)
    if form_new.is_valid():
      form_new.save()
      return redirect("admin")
    else:
      return render(request, "serv/serv_settings.html", {"form": form_new})

  service_page = HomeTemplate.objects.get()

  form = HomeTemplateForm(instance=service_page)
  context = {
    "form": form,
    "service_page":service_page
  }

  return render(request, "static/home_page.html", context)