from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import UploadCSVForm
import csv
from .models import ArtData
from django.shortcuts import get_object_or_404

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():

            csv_file = request.FILES['file']
            if not csv_file.name.endswith('.csv'):
                return HttpResponse("This is not a CSV file!")
            
            file_data = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(file_data, delimiter=';')
            for row in reader:
                artdata = ArtData()
                for column, value in row.items():
                    print(f'{column}: {value}')
                    setattr(artdata, column.replace("\ufeff", ""), value.strip())
                    artdata.save()
                
            return HttpResponse("File uploaded and processed successfully!")
    else:
        form = UploadCSVForm()
    return render(request, 'import.html', {'form': form})

class ArtDataListView(ListView):
    model = ArtData
    template_name = 'artdata_list.html'
    context_object_name = 'artdata_list'


def artdata_detail(request, id):
    artdata = get_object_or_404(ArtData, id=id)
    return render(request, 'artdata_detail.html', {'artdata': artdata})

def artdata_search(request):
    query = request.GET.get('query', '')
    query = query.strip().replace("+", "")
    artdata_list = ArtData.objects.filter(datierung__icontains=query) | ArtData.objects.filter(id__icontains=query) | ArtData.objects.filter(namen_und_beiwoerter__icontains=query)
    return render(request, 'artdata_list.html', {'artdata_list': artdata_list, 'dynasty': query})