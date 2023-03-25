import os
import requests

bearer_token = "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTI0NTY2NDU4MjY2NjE2MzEzNDQiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzU5MDcyLCJleHAiOjE2Nzk4NDU0NzIsImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.lH2rY_zILhUHsq2M7a-nvMHdGc-S566rLsdgbAE0F2MeC6FqCG4s_QfFlBrdqOYnojg9gVCPgB3foF7ZI6e3HvrQGZhyDVcyGpjo8OMdUlsreLQQSNlRWjvpxea4H_H9Rtv73nHd1_A_y93um8uxvCfrnENf5MHqPEVpYHED_T_qfJ1f8rxGCpUXeYFDUoJG3BUZ3VDDV1Ed4lPFczzG3jq1QQl1upLwVIPmmrOqHpu3N_iKziWjS9isxoiK550BYjGNEysQ6Js131r6bOQ3X_0tZk_uhBfHhmmZDdsptQ7aWuPFGrhsks_Qz05U4pLrg3GQRtR0UOkJ3CQmPVVA5w"

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

payload = {
    "videoDimension": {"height": 1080, "width": 1920},
    "scenes": [
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://www.musicinminnesota.com/wp-content/uploads/2021/02/Michael-Jackson-live.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>Michael Joseph Jackson was an American singer, songwriter, dancer, and philanthropist. Dubbed the 'King of Pop', he is regarded as one of the most significant cultural figures of the 20th century.</speak>",
                            "transcript_type": "ssml_limited",
                        },
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://i.hurimg.com/i/hdn/75/0x0/63807b4d4e3fe0216cfc0529.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>In 1982, Michael released, Thriller, which spent months at the top of the Billboard 200 charts... Cause this is thriller, thriller night...  </speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>Check out Michael's wikipedia to know more about him. Thank you, have a great day.</speak>",
                            "transcript_type": "ssml_limited",
                        },
                        "kind": "Spokesperson",
                    },
                },
            ]
        },
    ],
    "title": "Into to MJ",
    "thumbnailUrl": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
}
headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(f"CAMPAIGN_ID= {response.text}")
