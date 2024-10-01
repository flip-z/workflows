# This is the new issue main function. Expects environment variables from the github action.
import os

# Get the issue details from environment variables
issue_title = os.getenv('ISSUE_TITLE')
issue_body = os.getenv('ISSUE_BODY')
issue_url = os.getenv('ISSUE_URL')



# This should probably expect a specific issue format? Some sort of UDM?
# 
# Example usage
print(f"Issue Title: {issue_title}")
print(f"Issue Body: {issue_body}")
print(f"Issue URL: {issue_url}")
