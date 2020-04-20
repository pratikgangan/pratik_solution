import glob, os
import requests
import json

#listing all the jason files in current foloder  


# Opening JSON file 

def movieMetadata(i):
    
    f = open('C:/Users/Help/Source/Repos/pratik_solution2/movies/'+i) 




    # returns JSON object as 
    # a dictionary 
    df2 = json.load(f) 
    id=df2['imdbId']

    # Closing file 
    f.close() 
    response=requests.get('http://www.omdbapi.com/?i='+id+'&apikey=68fd98ab')
    df1=(response.json())


 
    #new json payload
    ab={}
    #transformations
    ab['Plot']=df1['Plot']
    ab['Title']=df1['Title']
    ab['Runntime']=df2['duration']
    

    tempd={}
    templ=[]
    tempd2={}
    for i,j in df2['userrating'].items():
      tempd[i]=str(j)

# print(d)
    for i,j in tempd.items():    
      tempd2['Source']=str(i)
      tempd2['Value']=str(j)
      templ.append(tempd2)
      tempd2=tempd2.copy()
       
    ab['Ratings']= df1['Ratings']+templ


    ab['Actors']=df1['Actors'].split(', ') 
    ab['Director']=df1['Director'].split(', ') 
    ab['Writer']=df1['Writer'].split(', ')
    ab['Year']=df1['Year']
    ab['Released']=df1['Released']
    ab['Genre']=df1['Genre']
    ab['Language']=df1['Language']
    ab['Country']=df1['Country']
    ab['Awards']=df1['Awards']
    ab['Metascore']=df1['Metascore']
    ab['imdbRating']=df1['imdbRating']
    ab['imdbVotes']=df1['imdbVotes']
    ab['imdbID']=df1['imdbID']
    ab['Type']=df1['Type']
    ab['DVD']=df1['DVD']
    ab['BoxOffice']=df1['BoxOffice']
    ab['Production']=df1['Production']
    ab['Website']=df1['Website']
    ab['Response']=df1['Response']
    ab['id']=df2['id']
    ab['languges']=df2['languages']
    print(ab)   
    return ab

