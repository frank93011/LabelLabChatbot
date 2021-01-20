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
import utils.flex_objects as flexObj
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
                TextSendMessage(text="目前無法顯示使用者資訊，請稍後再嘗試"))
    elif text == '任務清單':
        response = get_all_tasks()
        if(response):
            carousels = []
            for task in response:
                if(task['taskType'] == 'classification'):
                    carousels.append(CarouselColumn(thumbnail_image_url='https://i.imgur.com/vphbdKm.jpg',
                                        title=task['taskTitle'],text="委託人: {}".format(task['taskOwnerName']),
                                        actions=[PostbackAction(label='開始任務', data='action=startTask&taskId={}'.format(task['taskId']))]))
            image_carousel_template = CarouselTemplate(columns=carousels)
            template_message = TemplateSendMessage(
                alt_text='所有任務', template=image_carousel_template)
            line_bot_api.reply_message(event.reply_token, template_message)
        else:
            send_error_message()
    elif text == '關於作者':
        url = 'https://i.imgur.com/vi9vaYc.jpg'
        app.logger.info("url=" + url)
        bubble_string = flexObj.profile
        message = FlexSendMessage(alt_text="關於作者", contents=json.loads(bubble_string))
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
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
        else:
            print("login failed")
        url = 'https://i.imgur.com/vi9vaYc.jpg'
        app.logger.info("url=" + url)
        bubble_string = flexObj.profile
        message = FlexSendMessage(alt_text="關於作者", contents=json.loads(bubble_string))
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
    if event.postback.data.find("&") != -1:
        action = event.postback.data.split("&")[0][7:]
        taskId = event.postback.data.split("&")[1][7:]
        if(action == "startTask"):
            url, replyItems = startTask(event.source.user_id, taskId)
            if(url):
                line_bot_api.reply_message(
                    event.reply_token,
                    [
                        TextSendMessage(text='請點選按鈕協助進行以下圖片的標註，如欲結束標記請按「結束作答」的按鈕'),
                        ImageSendMessage(url, url),
                        TextSendMessage(text='請問上方圖片屬於哪個類別?',
                        quick_reply=QuickReply(
                            items=replyItems
                        ))
                    ]
                )
            else:
                send_error_message()
        
        elif(action == "answerTask"):
            labelId = event.postback.data.split("&")[2][8:]
            answer = event.postback.data.split("&")[3][7:]
            transactionId = None
            if(event.postback.data.find("transactionId") != -1):
                transactionId = event.postback.data.split("&")[4][14:]
            transaction = answerTask(event.source.user_id, taskId ,labelId, answer, transactionId)
            if(transaction):
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
            else:
                send_error_message()
        elif(action == "endTask"):
            labelId = event.postback.data.split("&")[2][8:]
            answer = event.postback.data.split("&")[3][7:]
            transactionId = event.postback.data.split("&")[4][14:]
            response = endTask(event.source.user_id, taskId,transactionId)
            if(response):
                bubbleJson = flexObj.toAccuracyJson(response['taskTitle'], response['accuracy'])
                flexMessage = FlexSendMessage(alt_text="準確度", contents=bubbleJson)

                line_bot_api.reply_message(
                    event.reply_token,
                    [   TextSendMessage(text=answer),
                        flexMessage
                    ]
                )
            else:
                send_error_message()
        elif(action == "contact"):
            bubble_string = flexObj.contact
            message = FlexSendMessage(alt_text="聯絡方式", contents=json.loads(bubble_string))
            line_bot_api.reply_message(
                event.reply_token,
                message
            )
        elif(action == "projectExperience"):
            bubble_string = flexObj.projectExperience
            message = FlexSendMessage(alt_text="專案經歷", contents=json.loads(bubble_string))
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


### reply internal error:
def send_error_message():
    line_bot_api.reply_message(
                    event.reply_token,
                    [   TextSendMessage(text="伺服器錯誤，請再幾分鐘後嘗試!")
                    ]
                )