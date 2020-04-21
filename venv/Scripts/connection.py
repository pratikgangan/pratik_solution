import glob, os
import requests
import json

#listing all the jason files in current foloder  


# Opening JSON file 

def movieMetadata(i):
    
    f = open('C:/Users/Help/Source/Repos/pratik_solution2/movies/'+i+'.json') 




    # returns JSON object as 
    # a dictionary 
    df2 = json.load(f) 
    id=df2['imdbId']

    # Closing file 
    f.close() 
    response=requests.get('http://www.omdbapi.com/?i='+id+'&apikey=68fd98ab')
    df1=(response.json())


 
    #new json payload
    merged={}
    #transformations
    merged['Plot']=df1['Plot']
    merged['Title']=df1['Title']
    merged['Runntime']=df2['duration']
    

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
       
    merged['Ratings']= df1['Ratings']+templ


    merged['Actors']=df1['Actors'].split(', ') 
    merged['Director']=df1['Director'].split(', ') 
    merged['Writer']=df1['Writer'].split(', ')
    merged['Year']=df1['Year']
    merged['Released']=df1['Released']
    merged['Genre']=df1['Genre']
    merged['Language']=df1['Language']
    merged['Country']=df1['Country']
    merged['Awards']=df1['Awards']
    merged['Metascore']=df1['Metascore']
    merged['imdbRating']=df1['imdbRating']
    merged['imdbVotes']=df1['imdbVotes']
    merged['imdbID']=df1['imdbID']
    merged['Type']=df1['Type']
    merged['DVD']=df1['DVD']
    merged['BoxOffice']=df1['BoxOffice']
    merged['Production']=df1['Production']
    merged['Website']=df1['Website']
    merged['Response']=df1['Response']
    merged['id']=df2['id']
    merged['languges']=df2['languages']
    print(merged)   
    return merged

