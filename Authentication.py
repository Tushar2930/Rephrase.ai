import requests
import os
import sys

bearer_token = "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTI0NTY2NDU4MjY2NjE2MzEzNDQiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzU5MDcyLCJleHAiOjE2Nzk4NDU0NzIsImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.lH2rY_zILhUHsq2M7a-nvMHdGc-S566rLsdgbAE0F2MeC6FqCG4s_QfFlBrdqOYnojg9gVCPgB3foF7ZI6e3HvrQGZhyDVcyGpjo8OMdUlsreLQQSNlRWjvpxea4H_H9Rtv73nHd1_A_y93um8uxvCfrnENf5MHqPEVpYHED_T_qfJ1f8rxGCpUXeYFDUoJG3BUZ3VDDV1Ed4lPFczzG3jq1QQl1upLwVIPmmrOqHpu3N_iKziWjS9isxoiK550BYjGNEysQ6Js131r6bOQ3X_0tZk_uhBfHhmmZDdsptQ7aWuPFGrhsks_Qz05U4pLrg3GQRtR0UOkJ3CQmPVVA5w"

campaign_id = "kXkl2ZTm8OF0pyBeBAgpbuvmyUsk0B"

url = f"https://personalized-brand.api.rephrase.ai/v2/campaign/kXkl2ZTm8OF0pyBeBAgpbuvmyUsk0B"

headers = {
    "accept": "application/json",
    "Authorization": bearer_token
}

response = requests.get(url, headers=headers)

print(response.text)
