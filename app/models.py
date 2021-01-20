from app import handler, line_bot_api, app, static_tmp_path
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

import datetime
import json
import os
import sys
import tempfile
from utils.query import *
from flask import Flask, request, abort, send_from_directory


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text

    if text == '我的labelr檔案':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            response = login(event.source.user_id)
            if(response):
                print(profile)
                totalFinished = sum(list(response.values()))
                bubble = BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url=profile.picture_url,
                    size='full',
                    aspect_ratio='1:1',
                    aspect_mode='cover'
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        # title
                        TextComponent(text=profile.display_name, weight='bold', size='xl', align= "center"),
                        # info
                        BoxComponent(
                            layout='vertical',
                            margin='lg',
                            spacing='sm',
                            contents=[
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='總共完成{}項任務'.format(totalFinished),
                                            align= "center",
                                            color='#aaaaaa',
                                            weight='bold',
                                            size='md',
                                            flex=1
                                        ),
                                    ],
                                ),
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='分類任務',
                                            align= "center",
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=3
                                        ),
                                        TextComponent(
                                            text=str(response['CLAS']),
                                            wrap=True,
                                            align= "center",
                                            color='#666666',
                                            size='sm',
                                            flex=3
                                        )
                                    ],
                                ),
                                BoxComponent(
                                    layout='baseline',
                                    spacing='sm',
                                    contents=[
                                        TextComponent(
                                            text='NER任務',
                                            align= "center",
                                            color='#aaaaaa',
                                            size='sm',
                                            flex=3
                                        ),
                                        TextComponent(
                                            text=str(response['NER']),
                                            align= "center",
                                            wrap=True,
                                            color='#666666',
                                            size='sm',
                                            flex=3,
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
                footer=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        ButtonComponent(
                            style='primary',
                            height='sm',
                            action=URIAction(label='我的Labelr檔案', uri="https://line-label.herokuapp.com/Profile")
                        )
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="我的Labelr檔案", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )
            
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile API without user ID"))
    elif text == '任務清單':
        response = get_all_tasks()
        if(response):
            carousels = []
            print(response)
            for task in response:
                if(task['taskType'] == 'classification'):
                    carousels.append(CarouselColumn(thumbnail_image_url='https://i.imgur.com/vphbdKm.jpg',
                                        title=task['taskTitle'],text="委託人: {}".format(task['taskOwnerName']),
                                        actions=[PostbackAction(label='開始任務', data='action=startTask&taskId={}'.format(task['taskId']))]))
            image_carousel_template = CarouselTemplate(columns=carousels)
            template_message = TemplateSendMessage(
                alt_text='所有任務', template=image_carousel_template)
            line_bot_api.reply_message(event.reply_token, template_message)
    elif text == '關於作者':
        # url = request.url_root + '/static/profile.jpg'
        url = 'https://i.imgur.com/vi9vaYc.jpg'
        app.logger.info("url=" + url)
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url=url,
                size='full',
                aspect_ratio='20:15',
                aspect_mode='cover',
            ),
            body=BoxComponent(
                layout='vertical',
                margin='md',
                contents=[
                    # title
                    TextComponent(
                        text='陳漢威 Frank',
                        size='xl',
                        weight='bold',
                        flex=1
                    ),
                    TextComponent(text='工作經驗', weight='bold', color='#aaaaaa', size='lg', margin='xl'),
                    # work experience
                    BoxComponent(
                        layout='horizontal',
                        margin='xl',
                        contents=[
                            BoxComponent(
                                layout='vertical',
                                contents=[ImageComponent(size='sm', url='https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Microsoft_logo_-_2012_%28vertical%29.svg/663px-Microsoft_logo_-_2012_%28vertical%29.svg.png')],
                                width="40px",
                                height="40px"
                            ),
                            BoxComponent(
                                layout='vertical',
                                margin='xl',
                                contents=[
                                    TextComponent(text='Microsoft Consulting Services', size='md', offsetStart='10px', weight='bold', color='#999999'),
                                    TextComponent(text='Software Develop Intern', size='md', offsetStart='10px', color='#999999')
                                ]
                            )
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xl',
                        contents=[
                            BoxComponent(
                                layout='vertical',
                                contents=[ImageComponent(size='sm', url='https://i.imgur.com/VGqXUXl.png')],
                                width="40px",
                                height="40px"
                            ),
                            BoxComponent(
                                layout='vertical',
                                margin='xl',
                                contents=[
                                    TextComponent(text='Logiscool', size='md', offsetStart='10px', weight='bold', color='#999999'),
                                    TextComponent(text='Technical Assistant', size='md', offsetStart='10px', color='#999999')
                                ]
                            )
                        ]
                    ),
                    BoxComponent(
                        layout='horizontal',
                        margin='xl',
                        contents=[
                            BoxComponent(
                                layout='vertical',
                                contents=[ImageComponent(size='sm', url='https://i.imgur.com/pNonon4.png')],
                                width="40px",
                                height="40px"
                            ),
                            BoxComponent(
                                layout='vertical',
                                margin='xl',
                                contents=[
                                    TextComponent(text='PT.ICE Messenger', size='md', weight='bold', offsetStart='10px', color='#999999'),
                                    TextComponent(text='Android Intern', size='md', offsetStart='10px', color='#999999')
                                ]
                            )
                        ]
                    )
                ]
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=PostbackAction(label='更多專案經歷', data='action=projectExperience&taskId=0')
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=PostbackAction(label='聯絡方式', data='action=contact&taskId=0')
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="關於作者", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'quota':
        quota = line_bot_api.get_message_quota()
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='type: ' + quota.type),
                TextSendMessage(text='value: ' + str(quota.value))
            ]
        )
    elif text == 'quota_consumption':
        quota_consumption = line_bot_api.get_message_quota_consumption()
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='total usage: ' + str(quota_consumption.total_usage)),
            ]
        )
    elif text == 'push':
        line_bot_api.push_message(
            event.source.user_id, [
                TextSendMessage(text='PUSH!'),
            ]
        )
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Do it?', actions=[
            MessageAction(label='Yes', text='Yes!'),
            MessageAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'buttons':
        buttons_template = ButtonsTemplate(
            title='My buttons sample', text='Hello, my buttons', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping'),
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'carousel':
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='hoge1', title='fuga1', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping')
            ]),
            CarouselColumn(text='hoge2', title='fuga2', actions=[
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
            ]),
        ])
        template_message = TemplateSendMessage(
            alt_text='Carousel alt text', template=carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'image_carousel':
        image_carousel_template = ImageCarouselTemplate(columns=[
            ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
                                action=DatetimePickerAction(label='datetime',
                                                            data='datetime_postback',
                                                            mode='datetime')),
            ImageCarouselColumn(image_url='https://via.placeholder.com/1024x1024',
                                action=DatetimePickerAction(label='date',
                                                            data='date_postback',
                                                            mode='date'))
        ])
        template_message = TemplateSendMessage(
            alt_text='ImageCarousel alt text', template=image_carousel_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'flex':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://example.com/cafe.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Brown Cafe', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Shinjuku, Tokyo',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='CALL', uri='tel:000000'),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='WEBSITE', uri="https://example.com")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'flex_update_1':
        bubble_string = """
        {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip3.jpg",
                "position": "relative",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "1:1",
                "gravity": "center"
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
                        "type": "text",
                        "text": "Brown Hotel",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#ffffff"
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                          {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                          },
                          {
                            "type": "icon",
                            "size": "sm",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                          },
                          {
                            "type": "text",
                            "text": "4.0",
                            "size": "sm",
                            "color": "#d6d6d6",
                            "margin": "md",
                            "flex": 0
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "¥62,000",
                        "color": "#a9a9a9",
                        "decoration": "line-through",
                        "align": "end"
                      },
                      {
                        "type": "text",
                        "text": "¥42,000",
                        "color": "#ebebeb",
                        "size": "xl",
                        "align": "end"
                      }
                    ]
                  }
                ],
                "position": "absolute",
                "offsetBottom": "0px",
                "offsetStart": "0px",
                "offsetEnd": "0px",
                "backgroundColor": "#00000099",
                "paddingAll": "20px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "SALE",
                    "color": "#ffffff"
                  }
                ],
                "position": "absolute",
                "backgroundColor": "#ff2600",
                "cornerRadius": "20px",
                "paddingAll": "5px",
                "offsetTop": "10px",
                "offsetEnd": "10px",
                "paddingStart": "10px",
                "paddingEnd": "10px"
              }
            ],
            "paddingAll": "0px"
          }
        }
        """
        message = FlexSendMessage(alt_text="hello", contents=json.loads(bubble_string))
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
    elif text == 'quick_reply':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text='Quick reply',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="label1", data="data1")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="label2", text="text2")
                        ),
                        QuickReplyButton(
                            action=DatetimePickerAction(label="label3",
                                                        data="data3",
                                                        mode="date")
                        ),
                        QuickReplyButton(
                            action=CameraAction(label="label4")
                        ),
                        QuickReplyButton(
                            action=CameraRollAction(label="label5")
                        ),
                        QuickReplyButton(
                            action=LocationAction(label="label6")
                        ),
                    ])))
    elif text == 'link_token' and isinstance(event.source, SourceUser):
        link_token_response = line_bot_api.issue_link_token(event.source.user_id)
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='link_token: ' + link_token_response.link_token)
            ]
        )
    elif text == 'insight_message_delivery':
        today = datetime.date.today().strftime("%Y%m%d")
        response = line_bot_api.get_insight_message_delivery(today)
        if response.status == 'ready':
            messages = [
                TextSendMessage(text='broadcast: ' + str(response.broadcast)),
                TextSendMessage(text='targeting: ' + str(response.targeting)),
            ]
        else:
            messages = [TextSendMessage(text='status: ' + response.status)]
        line_bot_api.reply_message(event.reply_token, messages)
    elif text == 'insight_followers':
        today = datetime.date.today().strftime("%Y%m%d")
        response = line_bot_api.get_insight_followers(today)
        if response.status == 'ready':
            messages = [
                TextSendMessage(text='followers: ' + str(response.followers)),
                TextSendMessage(text='targetedReaches: ' + str(response.targeted_reaches)),
                TextSendMessage(text='blocks: ' + str(response.blocks)),
            ]
        else:
            messages = [TextSendMessage(text='status: ' + response.status)]
        line_bot_api.reply_message(event.reply_token, messages)
    elif text == 'insight_demographic':
        response = line_bot_api.get_insight_demographic()
        if response.available:
            messages = ["{gender}: {percentage}".format(gender=it.gender, percentage=it.percentage)
                        for it in response.genders]
        else:
            messages = [TextSendMessage(text='available: false')]
        line_bot_api.reply_message(event.reply_token, messages)
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title='Location', address=event.message.address,
            latitude=event.message.latitude, longitude=event.message.longitude
        )
    )


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


# Other Message Type
@handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def handle_content_message(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    elif isinstance(event.message, VideoMessage):
        ext = 'mp4'
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
    else:
        return

    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Save content.'),
            TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        ])


@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix='file-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '-' + event.message.file_name
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Save file.'),
            TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        ])


@handler.add(FollowEvent)
def handle_follow(event):
    if isinstance(event.source, SourceUser):
        profile = line_bot_api.get_profile(event.source.user_id)
        response = login(event.source.user_id)
        if(response):
            print(profile)
            totalFinished = sum(list(response.values()))
            bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url=profile.picture_url,
                size='full',
                aspect_ratio='1:1',
                aspect_mode='cover'
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text=profile.display_name, weight='bold', size='xl', align= "center"),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='總共完成{}項任務'.format(totalFinished),
                                        align= "center",
                                        color='#aaaaaa',
                                        weight='bold',
                                        size='md',
                                        flex=1
                                    ),
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='分類任務',
                                        align= "center",
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=3
                                    ),
                                    TextComponent(
                                        text=str(response['CLAS']),
                                        wrap=True,
                                        align= "center",
                                        color='#666666',
                                        size='sm',
                                        flex=3
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='NER任務',
                                        align= "center",
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=3
                                    ),
                                    TextComponent(
                                        text=str(response['NER']),
                                        align= "center",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=3,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    ButtonComponent(
                        style='primary',
                        height='sm',
                        action=URIAction(label='我的Labelr檔案', uri="https://line-label.herokuapp.com/Profile")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="我的Labelr檔案", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    app.logger.info("Got Unfollow event:" + event.source.user_id)


@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Joined this ' + event.source.type))


@handler.add(LeaveEvent)
def handle_leave():
    app.logger.info("Got leave event")


@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'ping':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='pong'))
    elif event.postback.data == 'datetime_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
    elif event.postback.data == 'date_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['date']))
    elif event.postback.data.find("&") != -1:
        action = event.postback.data.split("&")[0][7:]
        taskId = event.postback.data.split("&")[1][7:]
        if(action == "startTask"):
            url, replyItems = startTask(event.source.user_id, taskId)
            line_bot_api.reply_message(
                event.reply_token,
                [ImageSendMessage(url, url),
                    TextSendMessage(text='請問上方圖片屬於哪個類別?',
                    quick_reply=QuickReply(
                        items=replyItems
                    ))
                ]
            )
        
        elif(action == "answerTask"):
            labelId = event.postback.data.split("&")[2][8:]
            answer = event.postback.data.split("&")[3][7:]
            transactionId = None
            if(event.postback.data.find("transactionId") != -1):
                transactionId = event.postback.data.split("&")[4][14:]
            transaction = answerTask(event.source.user_id, taskId ,labelId, answer, transactionId)
            url, replyItems = startTask(event.source.user_id, taskId, transaction['transactionId'])
            line_bot_api.reply_message(
                event.reply_token,
                [   TextSendMessage(text="你的答案是: {}".format(answer)),
                    ImageSendMessage(url, url),
                    TextSendMessage(text='請問上方圖片屬於哪個類別?',
                    quick_reply=QuickReply(
                        items=replyItems
                    ))
                ]
            )
        elif(action == "endTask"):
            labelId = event.postback.data.split("&")[2][8:]
            answer = event.postback.data.split("&")[3][7:]
            transactionId = event.postback.data.split("&")[4][14:]
            response = endTask(event.source.user_id, taskId,transactionId)
            line_bot_api.reply_message(
                event.reply_token,
                [   TextSendMessage(text=answer),
                    TextSendMessage(text='準確度評估為:{}'.format(response['accuracy']))
                ]
            )
        elif(action == "contact"):
            bubble_string = """
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
            message = FlexSendMessage(alt_text="聯絡方式", contents=json.loads(bubble_string))
            line_bot_api.reply_message(
                event.reply_token,
                message
            )

@handler.add(BeaconEvent)
def handle_beacon(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got beacon event. hwid={}, device_message(hex string)={}'.format(
                event.beacon.hwid, event.beacon.dm)))


@handler.add(MemberJoinedEvent)
def handle_member_joined(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got memberJoined event. event={}'.format(
                event)))


@handler.add(MemberLeftEvent)
def handle_member_left(event):
    app.logger.info("Got memberLeft event")


@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)
