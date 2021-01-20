# Label Lab LINE Chatbot

<img src="https://i.imgur.com/jZSiyQv.png" alt="logo" width="150">

## Finished product
**LINE ID:** @124ybfnk

**QR Code:**

![](https://i.imgur.com/4wL4PB2.png)

## Motivation

Taiwan now has many SME(Small and Medium Enterprise) are active in developing or searching for AI solutions to enhance their work. But tend to suffer from the scarcity of data. And the data annotation is not a long-term need for the company.
We believe crowdsourcing can solve this problem. With so many mobile users and limitless trivial time they have, it can be huge productivity if they contribute to data labeling.

With LINE Chatbot, we can easily develop a service for mobile users to help local businesses labeling the data they needed. And this project is a showcase of how we can do it in the LINE Chatbot application.


## Sturcture

Using Python [Flask](http://flask.pocoo.org/) framework and [LINE Messaging API SDK for Python](https://github.com/line/line-bot-sdk-python) for fast development of this application chatbot. 
The service back-end deployed on Heroku server and using webhook for Messaging API connection.
The service has another server for the maintenance of the restful API that connect to the Database (Mongo DB). The related back-end codes are in [LabelLab-Backend](https://github.com/frank93011/LabelLab-Backend).

### Files usage
In ```./app```:
* ```__init__.py``` define the Flask app object and global variables.
* ```models.py``` are the implementation of each event handler to react for user behaviors.
* ```routes.py ``` deals with request and api connection exceptions.

In ```./utils```:
* ```query.py``` define the requests to the back-end server.
* ```flex_objects.py``` seals the json string for flex message styling.


## Reference

* [LINE Messaging API SDK for Python](https://github.com/line/line-bot-sdk-python)
* [Flask KitchenSink examlpe](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-kitchensink)
* [Messaging API Documents](https://developers.line.biz/en/docs/messaging-api/)
* [Flex Message Simulator](https://developers.line.biz/flex-simulator/)
