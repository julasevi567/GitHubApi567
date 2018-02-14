#Imports
import requests
import json

"""
This function will return a list of repositores that belong to a specific user
Input - String
Output - List
"""
def getUserRepos(userName):
    link = "https://api.github.com/users/" + userName + "/repos"
    userData = requests.get(link)
    repositories = json.loads(userData.text)
    userRepos = []
    
    #Loop through nodes getting repository name, handle error of invalid username
    for repository in repositories:
        try:
            userRepos.append(repository.get("name"))
        except:
            userRepos = []
         
    return userRepos
    
"""
This function will return a count of how many commits an indivudal repo containts
Input -  String, String
Output - Int
"""
def getCommitCount(userName, repoName):
    link = "https://api.github.com/repos/" + userName + "/" + repoName + "/commits"
    repoData = requests.get(link)
    commits = json.loads(repoData.text)
    commitCount = len(commits)

    return commitCount
        
"""
Main function that lists all the repos and lists each commit count given a specific
github user name.
"""
if __name__ == "__main__":
    #Ask username
    userName = raw_input("Enter Github username: ")

    #Get repos associated with given username
    userRepos = getUserRepos(userName)

    #Print usernamer
    print("User: " + userName)
    #Loop through associated repos printing name and their commit count
    for repository in userRepos:
        commitCount = getCommitCount(userName, repository)
        print("Repo: " + repository + " Number of Commits: " + str(commitCount))


