from django.shortcuts import render,redirect
from base.models import Article_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

# article_data=[
#     {
#         'id':1,
#         'title':'India',
#         'desc': '''India, the world's largest democracy, is known for its rich cultural heritage, diverse traditions, and rapid economic growth. Home to iconic landmarks such as the Taj Mahal and the Himalayas, India is also a hub for technology, agriculture, and spiritual tourism. The country has a deep-rooted history spanning thousands of years, with influences from various dynasties and colonial rule. Indian cuisine, Bollywood, and its festivals, like Diwali and Holi, are globally celebrated.'''
#     },
#     {
#         'id':2,
#         'title':'America',
#         'desc': '''The United States of America is a global superpower, known for its technological advancements, economic influence, and cultural exports. With landmarks such as the Statue of Liberty and the Grand Canyon, the country attracts millions of visitors annually. The USA is home to Silicon Valley, Hollywood, and a diverse population contributing to its cultural richness. Its democratic values, innovation in space exploration, and influence in global politics make it a key player on the world stage.'''
#     },
#     {
#         'id':3,
#         'title':'China',
#         'desc': '''China, the most populous country in the world, is a leader in manufacturing and technological innovation. With a history spanning thousands of years, it is home to the Great Wall, the Forbidden City, and a rapidly growing economy. Traditional Chinese medicine, martial arts, and its rich cuisine, including dishes like Peking duck and dim sum, are widely recognized. China’s Belt and Road Initiative has made it an influential player in global trade and infrastructure development.'''
#     },
#     {
#         'id':4,
#         'title':'Russia',
#         'desc': '''Russia, the largest country in the world by land area, is rich in natural resources and cultural history. It is known for its contributions to space exploration, classical literature, and architectural wonders like the Kremlin and Saint Basil's Cathedral. Russia has a long and complex history, from the Tsarist era to the Soviet Union and its present geopolitical significance. The country is famous for its ballet, vodka, and vast landscapes, including Siberia’s harsh winters.'''
#     },
#     {
#         'id':5,
#         'title':'Indonesia',
#         'desc': '''Indonesia, an archipelago of over 17,000 islands, is famous for its biodiversity, tropical beaches, and cultural diversity. It is home to Bali, Komodo dragons, and one of the world's largest Muslim populations. The country has a rich history of trade and cultural exchange due to its strategic location. Indonesia’s rainforests are among the most biodiverse on the planet, and its cuisine, including nasi goreng and satay, is loved worldwide.'''
#     },
#     {
#         'id':6,
#         'title':'Brazil',
#         'desc': '''Brazil, the largest country in South America, is famous for its Amazon rainforest, vibrant culture, and football legacy. Rio de Janeiro’s Christ the Redeemer and the annual Carnival festival are among its most famous attractions. The country is also a major producer of coffee and a leader in renewable energy sources. Brazil’s music, including samba and bossa nova, is known globally, and its diverse ecosystems make it a hotspot for ecotourism.'''
#     },
#     {
#         'id':7,
#         'title':'Japan',
#         'desc': '''Japan, known for its technological innovation and ancient traditions, is a country of contrasts. From the bustling city of Tokyo to the historic temples of Kyoto, Japan seamlessly blends modernity with heritage. The country is a leader in robotics, automobile manufacturing, and animation (anime). Japan’s culinary scene, featuring sushi, ramen, and tempura, is world-renowned. It is also home to Mount Fuji and traditional practices like tea ceremonies and sumo wrestling.'''
#     },
#     {
#         'id':8,
#         'title':'Germany',
#         'desc': '''Germany, a leader in engineering and innovation, is known for its efficiency, rich history, and contributions to science and philosophy. It boasts landmarks such as the Brandenburg Gate and the Black Forest. Germany played a pivotal role in both World Wars and is now one of the strongest economies in Europe. Oktoberfest, precision engineering (such as BMW and Mercedes-Benz), and its strong environmental policies define modern Germany.'''
#     },
#     {
#         'id':9,
#         'title':'Australia',
#         'desc': '''Australia, known for its stunning landscapes, is home to the Great Barrier Reef, vast deserts, and unique wildlife. Its major cities, including Sydney and Melbourne, are known for their high quality of life and cultural diversity. Australia is famous for its indigenous heritage, outdoor lifestyle, and sports culture, particularly cricket and rugby. The country is also a major exporter of minerals and has a strong commitment to environmental conservation.'''
#     },
#     {
#         'id':10,
#         'title':'South Africa',
#         'desc': '''South Africa is a country of incredible diversity, from its wildlife-filled national parks to its rich history of overcoming apartheid. It is known for Table Mountain, Kruger National Park, and its thriving wine industry. The country has three capital cities and is one of Africa’s largest economies. South Africa’s culture is shaped by its mix of African, European, and Asian influences, with vibrant music, dance, and art traditions.'''
#     }
# ]

@login_required(login_url='user_login')
def home(request):

    if request.method == 'POST':
        title_data = request.POST.get('title')
        desc_data = request.POST.get('desc')

        if title_data and desc_data:
            Article_model.objects.create(title=title_data, desc=desc_data)

    data = Article_model.objects.all().order_by('-id')  

        # search 

    querry=request.GET.get('querry')
    if querry :
        search=Article_model.objects.filter(
            Q(title__icontains=querry) | Q(desc__icontains=querry)
        )
    else:
        search=Article_model.objects.all()

    context = {
        'data': data,
        'search':search
    }



    return render(request, 'home.html', context)


@login_required(login_url='user_login')
def read(request,pk):

    data=Article_model.objects.get(id=pk)

    return render(request, 'read.html', {'data': data})


@login_required(login_url='user_login')
def update(request,pk):

    update_article=Article_model.objects.get(id=pk)

    if request.method =='POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']

        if title_data and desc_data:
            update_article.title=title_data
            update_article.desc=desc_data
            update_article.save()
            return redirect('home')


    return render(request,'update.html',{'data':update_article})



@login_required(login_url='user_login')
def delete(request,pk):

    article_data=Article_model.objects.get(id=pk)

    article_data.delete()

    return redirect('home')

    
def event(request):
    return render(request,'event.html')


@login_required(login_url='user_login')
def create(request):

    if request.method=='POST':
        title_data = request.POST.get('title')
        desc_data = request.POST.get('desc')

        Article_model.objects.create(title=title_data, desc=desc_data)
        return redirect('home')
    
    return render(request,'create.html')

@login_required(login_url='user_login')
def news(request):
    return render(request,'news.html')

@login_required(login_url='user_login')
def user_profile(request):
    return render(request,'user_profile.html')



@login_required(login_url='user_login')
def updateprofile(request):
    user = request.user

    if request.method == 'POST':
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']

        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')  

    return render(request, 'updateprofile.html', {'user': user})


def about(request):
    return render(request,'about.html')
