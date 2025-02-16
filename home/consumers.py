from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':'connected from django channels'}))
    
    def receive(self, text_data):
        print("TEXT DATA", text_data)
        self.send(text_data=json.dumps(text_data))

    def disconnect(self):
        pass

    