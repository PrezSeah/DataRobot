**The main purpose of this application is to replicate itself into your GitHub repository.**

# **What does the application do?**

- This web application requests access to the user's GitHub account.
- Then it builds a repository in user's account with its own code.
- Finally with a help of one URL user can replicate existing repository to his own account.

# **How does the application work?**

- Firstly, with a help of OAuth application, our app tries to access the user's GitHub account.
- Then, our app creates a link to repository with a help of the constant name of repository
and user's name (your GitHub username).
- On the last step, our app builds a link for replicating repository and makes a replication - 
again with a help of user's name (your GitHub username) and constant repository name.
- On the homepage you can press the button for redirection to your repository with the replicated code.
