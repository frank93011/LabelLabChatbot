
contact = """
    {
    "type": "bubble",
    "size": "kilo",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "我的聯絡方式",
                "color": "#ffffff",
                "size": "xl",
                "flex": 4,
                "weight": "bold"
            }
            ]
        }
        ],
        "paddingAll": "20px",
        "backgroundColor": "#0367D3",
        "spacing": "md",
        "height": "70px",
        "paddingTop": "22px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/MpxFCZL.png",
                    "size": "40px",
                    "animated": false,
                    "align": "start",
                    "position": "relative",
                    "flex": 3
                }
                ],
                "width": "60px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "postback",
                    "label": "Gmail",
                    "data": "action=mailAddress&taskId=0",
                    "displayText": "frankchen93011@gmail.com"
                    },
                    "style": "primary",
                    "color": "#E65C4F",
                    "margin": "none",
                    "height": "sm"
                }
                ]
            }
            ]
        },
        {
            "type": "separator",
            "margin": "lg"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/c5UR2dY.png",
                    "size": "40px",
                    "animated": false,
                    "action": {
                    "type": "uri",
                    "label": "Linkedin",
                    "uri": "https://www.linkedin.com/in/frank93011/"
                    },
                    "align": "start",
                    "position": "relative",
                    "flex": 3
                }
                ],
                "width": "60px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "Linkedin",
                    "uri": "https://www.linkedin.com/in/frank93011/"
                    },
                    "style": "primary",
                    "color": "#2867B2",
                    "margin": "none",
                    "height": "sm"
                }
                ]
            }
            ],
            "margin": "lg"
        },
        {
            "type": "separator",
            "margin": "lg"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/JHWlajw.png",
                    "size": "40px",
                    "animated": false,
                    "action": {
                    "type": "uri",
                    "label": "github",
                    "uri": "https://github.com/frank93011"
                    },
                    "align": "start",
                    "position": "relative",
                    "flex": 3
                }
                ],
                "width": "60px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "Github",
                    "uri": "https://github.com/frank93011"
                    },
                    "style": "primary",
                    "color": "#24292e",
                    "margin": "none",
                    "height": "sm"
                }
                ]
            }
            ],
            "margin": "lg"
        }
        ]
    }
    }
"""
projectExperience = """
    {
    "type": "carousel",
    "contents": [
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://i.imgur.com/CcCbPNw.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "320:213",
            "action": {
            "type": "uri",
            "label": "DeepInstaGram",
            "uri": "https://github.com/frank93011/DeepInstaGram",
            "altUri": {
                "desktop": "https://github.com/frank93011/DeepInstaGram"
            }
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "IG貼文性格分析與行銷受眾分群",
                "weight": "bold",
                "size": "md",
                "wrap": true
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "python",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#4B8BBE",
                    "width": "60px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Web",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#323330",
                    "width": "45px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "margin": "md"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "wrap": true,
                        "color": "#8c8c8c",
                        "size": "xs",
                        "flex": 5,
                        "text": "Categorize the common style people posts on instagram → find the matching brands that we can recommand to them."
                    }
                    ]
                }
                ]
            }
            ],
            "spacing": "sm",
            "paddingAll": "13px"
        }
        },
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://i.imgur.com/M7ebioK.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "320:213",
            "action": {
            "type": "uri",
            "label": "JIE",
            "uri": "https://github.com/frank93011/JIE",
            "altUri": {
                "desktop": "https://github.com/frank93011/JIE"
            }
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "BERT日文投標文件資料擷取",
                "weight": "bold",
                "size": "md",
                "wrap": true
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "python",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#4B8BBE",
                    "width": "60px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "jupyter",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#da5b0b",
                    "width": "60px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "margin": "md"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "wrap": true,
                        "color": "#8c8c8c",
                        "size": "xs",
                        "flex": 5,
                        "text": "Extracting different types of information with limited labeled data.Using variation of BERT QA models with stacking structure. "
                    }
                    ]
                }
                ]
            }
            ],
            "spacing": "sm",
            "paddingAll": "13px"
        }
        },
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://i.imgur.com/InbLjjS.png",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "320:213",
            "action": {
            "type": "uri",
            "label": "Face_Mask_Detector",
            "uri": "https://github.com/frank93011/Face_Mask_Detector",
            "altUri": {
                "desktop": "https://github.com/frank93011/Face_Mask_Detector"
            }
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "口罩辨識系統",
                "weight": "bold",
                "size": "md",
                "wrap": true
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "python",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#4B8BBE",
                    "width": "60px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "OpenCV",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#FFD43B",
                    "width": "66px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "margin": "md"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Implementation of face mask detector which can quickly be deployed on local camera based on MTCNN and resnet18.",
                        "wrap": true,
                        "color": "#8c8c8c",
                        "size": "xs",
                        "flex": 5
                    }
                    ]
                }
                ]
            }
            ],
            "spacing": "sm",
            "paddingAll": "13px"
        }
        },
        {
        "type": "bubble",
        "size": "kilo",
        "hero": {
            "type": "image",
            "url": "https://i.imgur.com/RqwKCUz.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "320:213",
            "action": {
            "type": "uri",
            "label": "NB-4U",
            "uri": "https://github.com/frank93011/NB-4U-trial",
            "altUri": {
                "desktop": "https://github.com/frank93011/NB-4U-trial"
            }
            }
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "text": "NB-4U 3D Game ",
                "weight": "bold",
                "size": "md",
                "wrap": true
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Unity",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#222c37",
                    "width": "60px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "C#",
                        "size": "xs",
                        "color": "#ffffff",
                        "flex": 0,
                        "align": "center",
                        "gravity": "center",
                        "weight": "bold",
                        "offsetTop": "2.5px"
                    }
                    ],
                    "backgroundColor": "#9a4993",
                    "width": "35px",
                    "height": "25px",
                    "cornerRadius": "5px",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "margin": "md"
                }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "wrap": true,
                        "color": "#8c8c8c",
                        "size": "xs",
                        "flex": 5,
                        "text": "Design an Unity based 3D platform game. Representing our school and Winning 2 major award in Creative Game Design Award in 2018."
                    }
                    ]
                }
                ]
            }
            ],
            "spacing": "sm",
            "paddingAll": "13px"
        }
        }
    ]
    }
"""