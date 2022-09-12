from django.contrib import admin
from django.urls import path
from web_api import models
from django.shortcuts import render 
from django import forms 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
   csv_upload =  forms.FileField()



class ModelAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls+urls
    
    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\r\n")

            for x in csv_data:
                fields = x.split(",")
                if len(fields)==7:
                    sub = models.Subject.objects.update_or_create( 
                        subject = str(fields[6]).capitalize(),
                        )
                    cdn = models.cdnProvider.objects.update_or_create( 
                        title = str(fields[5]).capitalize(),
                        )
                    s_id = models.Subject.objects.get(subject = fields[6].capitalize())
                    c_id = models.cdnProvider.objects.get(title = fields[5].capitalize())
                    created = models.Site.objects.create(
                        title_En = str(fields[0]),
                        title_Fa = str(fields[1]),
                        URL = str(fields[2]),
                        IP = str(fields[3]),
                        location = str(fields[4]).upper(),
                        cdn_provider = c_id
                        )
                    site = models.Site.objects.get(URL = str(fields[2]))
                    site.subject.add(s_id)
                
            url = reverse('admin:index')
            return HttpResponseRedirect(url)
        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)




admin.site.register(models.Site,ModelAdmin)
admin.site.register(models.Subject,)
admin.site.register(models.SubjectSite,)
admin.site.register(models.QualityOfService,)
admin.site.register(models.cdnProvider,)

