import json

profile = """
    {
    "type": "bubble",
    "size": "mega",
    "hero": {
        "type": "image",
        "url": "https://i.imgur.com/vi9vaYc.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:15"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "陳漢威 Frank",
            "size": "xl",
            "weight": "bold"
        },
        {
            "type": "text",
            "text": "學歷",
            "color": "#787878",
            "size": "lg",
            "weight": "bold",
            "margin": "md"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "2013.7",
                "size": "sm",
                "gravity": "center"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "cornerRadius": "30px",
                    "height": "12px",
                    "width": "12px",
                    "borderColor": "#EF454D",
                    "borderWidth": "2px"
                },
                {
                    "type": "filler"
                }
                ],
                "flex": 0
            },
            {
                "type": "text",
                "text": "國立花蓮高級中學",
                "gravity": "center",
                "flex": 4,
                "size": "sm",
                "weight": "bold"
            }
            ],
            "spacing": "lg",
            "cornerRadius": "30px",
            "margin": "md"
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
                    "type": "filler"
                }
                ],
                "flex": 1
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "filler"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "width": "2px",
                        "backgroundColor": "#B7B7B7"
                    },
                    {
                        "type": "filler"
                    }
                    ],
                    "flex": 1
                }
                ],
                "width": "12px"
            },
            {
                "type": "text",
                "text": " ",
                "gravity": "center",
                "flex": 4,
                "size": "xs",
                "color": "#8c8c8c"
            }
            ],
            "spacing": "lg",
            "height": "20px"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "2016.7",
                    "gravity": "center",
                    "size": "sm"
                }
                ],
                "flex": 1
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "cornerRadius": "30px",
                    "width": "12px",
                    "height": "12px",
                    "borderWidth": "2px",
                    "borderColor": "#6486E3"
                },
                {
                    "type": "filler"
                }
                ],
                "flex": 0
            },
            {
                "type": "text",
                "text": "臺灣大學 資訊管理學系",
                "gravity": "center",
                "flex": 4,
                "size": "sm",
                "weight": "bold"
            }
            ],
            "spacing": "lg",
            "cornerRadius": "30px"
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
                    "type": "filler"
                }
                ],
                "flex": 1
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "filler"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "width": "2px",
                        "backgroundColor": "#6486E3"
                    },
                    {
                        "type": "filler"
                    }
                    ],
                    "flex": 1
                }
                ],
                "width": "12px"
            },
            {
                "type": "text",
                "text": " ",
                "gravity": "center",
                "flex": 4,
                "size": "xs",
                "color": "#8c8c8c"
            }
            ],
            "spacing": "lg",
            "height": "20px"
        },
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "text",
                "text": "2020.7",
                "gravity": "center",
                "size": "sm"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "cornerRadius": "30px",
                    "width": "12px",
                    "height": "12px",
                    "borderColor": "#6486E3",
                    "borderWidth": "2px"
                },
                {
                    "type": "filler"
                }
                ],
                "flex": 0
            },
            {
                "type": "text",
                "text": "臺灣大學 資訊管理學研究所",
                "gravity": "center",
                "flex": 4,
                "size": "sm",
                "weight": "bold"
            }
            ],
            "spacing": "lg",
            "cornerRadius": "30px"
        },
        {
            "type": "separator",
            "margin": "lg"
        },
        {
            "type": "text",
            "text": "工作經歷",
            "color": "#787878",
            "size": "lg",
            "weight": "bold",
            "margin": "xl"
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
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Microsoft_logo_-_2012_%28vertical%29.svg/663px-Microsoft_logo_-_2012_%28vertical%29.svg.png",
                    "aspectMode": "fit",
                    "size": "full"
                }
                ],
                "width": "40px",
                "height": "40px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Microsoft Consulting Services",
                    "weight": "bold",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": "Software Develop Intern",
                    "color": "#999999"
                }
                ],
                "offsetStart": "12px",
                "offsetBottom": "2.5px"
            }
            ],
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
                    "url": "https://i.imgur.com/VGqXUXl.png",
                    "aspectMode": "fit",
                    "size": "full"
                }
                ],
                "width": "40px",
                "height": "40px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "Logiscool",
                    "weight": "bold",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": "Technical Assistant",
                    "color": "#999999"
                }
                ],
                "offsetStart": "12px",
                "offsetBottom": "2.5px"
            }
            ],
            "margin": "md"
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
                    "url": "https://i.imgur.com/pNonon4.png",
                    "aspectMode": "fit",
                    "size": "full"
                }
                ],
                "width": "40px",
                "height": "40px"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "PT.ICE Messenger",
                    "weight": "bold",
                    "color": "#999999"
                },
                {
                    "type": "text",
                    "text": "Android Intern",
                    "color": "#999999"
                }
                ],
                "offsetStart": "12px",
                "offsetBottom": "2.5px"
            }
            ],
            "margin": "md"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "postback",
            "label": "更多專案經歷",
            "data": "action=projectExperience&taskId=0",
            "displayText": "更多專案經歷"
            },
            "height": "sm"
        },
        {
            "type": "separator"
        },
        {
            "type": "button",
            "action": {
            "type": "postback",
            "label": "聯絡方式",
            "data": "action=contact&taskId=0",
            "displayText": "聯絡方式"
            },
            "height": "sm"
        }
        ]
    }
    }
"""
def toAccuracyJson(taskTitle, accuracy):
    bubbleString = """
    {
    "type": "bubble",
    "size": "micro",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "準確程度",
            "color": "#ffffff",
            "align": "start",
            "size": "lg",
            "gravity": "center",
            "weight": "bold"
        },
        {
            "type": "text",
            "text": "{}%",
            "color": "#ffffff",
            "align": "start",
            "size": "xs",
            "gravity": "center",
            "margin": "lg"
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "filler"
                }
                ],
                "width": "{}%",
                "backgroundColor": "#0D8186",
                "height": "6px"
            }
            ],
            "backgroundColor": "#9FD8E36E",
            "height": "6px",
            "margin": "sm"
        }
        ],
        "backgroundColor": "#27ACB2",
        "paddingTop": "19px",
        "paddingAll": "12px",
        "paddingBottom": "16px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "Title"
        }
        ],
        "spacing": "md",
        "paddingAll": "12px"
    },
    "styles": {
        "footer": {
        "separator": false
        }
    }
    }
    """
    ### replace static var to dynamic obj
    bubbleString = bubbleString.replace("{}", str(accuracy * 100)[:3]).replace("Title", taskTitle)
    bubbleJson = json.loads(bubbleString)
    return bubbleJson

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